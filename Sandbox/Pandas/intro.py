import pandas as pd

x=[1,2,3,4,5]

myvar=pd.Series(x, index=['raz', 'dwa', 'trzy', 'cztery', 'pięć'])
raz=myvar['raz']

calories={'day1':400, 'day2':320, 'day3':420, 'day4':370}
mycalories=pd.Series(calories)
day1=mycalories['day1']
fewdays=pd.Series(calories, index=['day1', 'day2'])

#########################################################################

data={
    'calories': [400, 320, 450],
    'duration': [50, 35, 40]
}

df1=pd.DataFrame(data)
df2=pd.DataFrame(data, index=['day1', 'day2', 'day3'])

row1=df1.loc[1]
row13=df2.loc[['day1','day3']]

########################################################################

csv=pd.read_csv('data.csv')
whole=csv.to_string()
pd.options.display.max_rows=999

json=pd.read_json('data.json')

head=json.head(10)
tail=json.tail()

json.info()

#########################################################################





