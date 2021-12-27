import pandas as pd
from collections import Counter

#read lottery.csv file
df=pd.read_csv("/Users/yunseok/Desktop/lottery.csv")

num_list=list(df['first'])+list(df['second'])+list(df['third'])+list(df['fourth'])+list(df['fifth'])+list(df['sixth'])

count = Counter(num_list)
common_num_45 = count.most_common(45)

for i in range(0, 45):
    print(str(common_num_45[i][0])+" -> "+str(common_num_45[i][1])+" times")