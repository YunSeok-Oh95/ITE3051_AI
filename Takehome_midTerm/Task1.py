import pandas as pd
import numpy as np

#read csv file
df = pd.read_csv('/Users/yunseok/Downloads/ite351-takehome-midterm/2018-06-trade.csv')
#justify quantities2 as side=0 Buy EOS, side=1 Sell EOS, using 4-digit floating number
df['quantities']=np.where(df['side']==1, round(df['quantity']*(-1),4),round(df['quantity']*1,4))
#
df['quantities2']=df['quantities'].cumsum()
df['profit']=df['amount'].cumsum()
condition=(df['quantities2']>-5)&(df['quantities2']<5)
print(df[condition])