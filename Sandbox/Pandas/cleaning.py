import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('data1.csv')
new_df=df.dropna()
df.dropna(inplace=True)

df2=pd.read_csv('data1.csv')
df2.fillna(130, inplace=True)
df2['Calories'].fillna(130, inplace=True)

df3=pd.read_csv('data1.csv')
mean=df2['Calories'].mean()
df3['Calories'].fillna(mean, inplace=True)

df4=pd.read_csv('data1.csv')
median=df2['Calories'].median()
df4['Calories'].fillna(median, inplace=True)

df5=pd.read_csv('data1.csv')
mode=df2['Calories'].mode()[0]
df5['Calories'].fillna(mode, inplace=True)

###################################

df6=pd.read_csv('data1.csv')
df6['Date']=pd.to_datetime(df6['Date'])
df6.dropna(subset=['Date'], inplace=True)

df6.loc[7,'Duration']=45

for x in df6.index:
    if df6.loc[x, 'Duration']>120:
        df6.loc[x, 'Duration']=120

df7=pd.read_csv('data1.csv')

for x in df7.index:
    if df7.loc[x, 'Duration']>120:
        df7.drop(x, inplace=True)

###########################################

df7.duplicated()
df7.drop_duplicates(inplace=True)

##########################################

df8=pd.read_csv('data.csv')
df8.corr()

#######################################

df8.plot(kind='scatter', x='Duration', y='Calories')
plt.show()

df8.plot(kind='scatter', x='Duration', y='Maxpulse')
plt.show()

df8['Duration'].plot(kind='hist')
plt.show()

print()