import pandas as pd
import numpy as np
#read 2018-06-trade.csv file
df=pd.read_csv("/Users/yunseok/Downloads/ite351-takehome-midterm 2/2018-06-trade.csv")
df1=pd.read_csv("/Users/yunseok/Downloads/ite351-takehome-midterm 2/2018-06-01-orderbook.csv")
df2=pd.read_csv("/Users/yunseok/Downloads/ite351-takehome-midterm 2/2018-06-02-orderbook.csv")
#change 'timestamp' str to time format
df['timestamp']=pd.to_datetime(df['timestamp'])
df1['timestamp']=pd.to_datetime(df1['timestamp'])
df1['timestamp']=df1['timestamp'].astype('datetime64[s]')
df2['timestamp']=pd.to_datetime(df2['timestamp'])
df2['timestamp']=df2['timestamp'].astype('datetime64[s]')
df=df.drop(['quantity','fee','amount'],axis=1)
#insert the Mid-Price Column
Mid_price=[]
for i in range(0,377):
    condition1 = (df1['timestamp'] == df['timestamp'][i])
    df1_1=df1[condition1]
    df1_2=df1_1[(df1_1['type']==1)]
    df1_3=df1_2[(df1_2['price']==df1_2['price'].min())]
    df1_4=df1_1[(df1_1['type']==0)]
    df1_5=df1_4[(df1_4['price']==df1_4['price'].min())]
    val1=(df1_3.iloc[0][0]+df1_5.iloc[0][0])/2
    Mid_price.append(val1)
for j in range(377,1089):
    condition2 = (df2['timestamp'] == df['timestamp'][800])
    df2_1 = df2[condition2]
    df2_2 = df2_1[(df2_1['type'] == 1)]
    df2_3 = df2_2[(df2_2['price'] == df2_2['price'].min())]
    df2_4 = df2_1[(df2_1['type'] == 0)]
    df2_5 = df2_4[(df2_4['price'] == df2_4['price'].min())]
    val2 = (df2_3.iloc[0][0] + df2_5.iloc[0][0]) / 2
    Mid_price.append(val2)
#average quantity of all level for Sell -> type 1
askQ1_condition=(df1['type']==1)
askQ2_condition=(df2['type']==1)
askQty1=np.average(df1[askQ1_condition]['quantity'])
askQty2=np.average(df2[askQ2_condition]['quantity'])
askQty=(askQty1+askQty2)/2
#average quantity of all level for Buy -> type 0
bidQ1_condition=(df1['type']==0)
bidQty1=np.average(df1[bidQ1_condition]['quantity'])
bidQ2_condition=(df2['type']==0)
bidQty2=np.average(df2[bidQ2_condition]['quantity'])
bidQty=(bidQty1+bidQty2)/2
#average price of all level for Sell -> type 1
askP1_condition=(df1['type']==1)
askPx1=np.average(df1[askP1_condition]['price'])
askP2_condition=(df2['type']==1)
askPx2=np.average(df2[askP2_condition]['quantity'])
askPx=(askPx1+askPx2)/2
#average price of all level for Buy -> type 0
bidP1_condition=(df1['type']==1)
bidPx1=np.average(df1[bidP1_condition]['price'])
bidP2_condition=(df2['type']==1)
bidPx2=np.average(df2[bidP2_condition]['quantity'])
bidPx=(bidPx1+bidPx2)/2
book_price = (((askQty*bidPx)/bidQty) + ((bidQty*askPx)/askQty)) / (bidQty+askQty)

df['midprice'] = Mid_price
df['bfeature']= book_price-df['midprice']
df['alpha']=df['midprice']*df['bfeature']*0.004
df=df[['timestamp','price','midprice','bfeature','alpha','side']]
print(df)