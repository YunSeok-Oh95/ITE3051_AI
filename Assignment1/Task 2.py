import pandas as pd
import datetime

#read lottery.csv file
df=pd.read_csv("/Users/yunseok/Desktop/lottery.csv")
df['win']=1

#set the datetime
start_datetime=datetime.datetime(2021,4,17)
min_day=datetime.timedelta(days=7)

#append the fake number in csv
for idx in range(0,959):
    lottery_date=str_datetime=datetime.datetime.strftime(start_datetime,"%Y.%m.%d")
    fake_data = {'round': 959-idx, 'date': lottery_date, 'first': 1, 'second': 2, 'third': 3, 'fourth': 4, 'fifth': 5,
                 'sixth': 6, 'bonus': 7, 'win': 0}
    idx=2*idx+1
    temp1=df[df.index<idx]
    temp2=df[df.index>=idx]
    df=temp1.append(fake_data,ignore_index=True).append(temp2,ignore_index=True)
    start_datetime=start_datetime-min_day


#print the result
print(df)
df.to_csv("/Users/yunseok/Desktop/changelottery.csv",header=True,index=False)#extract to csv file