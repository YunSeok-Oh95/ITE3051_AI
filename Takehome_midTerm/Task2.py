import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#read csv file
df=pd.read_csv("/Users/yunseok/Downloads/ite351-takehome-midterm 2/2018-06-trade.csv")
df['timestamp']=pd.to_datetime(df['timestamp'])
df['TS']=df['timestamp'].dt.hour
#set buy_list and sell_list
buy_list=[]
for i in range(0,24):
    condition=(df["TS"]==i)&(df['side']==0)
    t1=df[condition]
    cnt=t1['quantity'].count()
    buy_list.append(cnt)
sell_list=[]
for j in range(0,24):
    condition2=(df["TS"]==j)&(df['side']==1)
    t2=df[condition2]
    cnt2=t2['quantity'].count()
    sell_list.append(cnt2)
#draw a graph
x=np.arange(0,24)
y_1=sell_list
y_2=buy_list
plt.plot(x,y_1,label='Hourly sell transaction',color='red',alpha=1,marker='o')
plt.plot(x,y_2,label='Hourly buy transaction',color='blue',alpha=1,marker='o')
plt.xlabel('timestamp_hour',fontsize=12)
plt.title("Hourly transaction count",fontsize=15)
plt.legend()
plt.show()
