import pandas as pd
import numpy as np
a='bios.csv'

#d=pd.read_csv(a)
#print(d.head())
#print(d.columns)
#print(d['born_date'])
#print(d.loc[1:3,'born_date'])
#print(d[d['born_country'].isin(['USA'])&(d['name'].str.startswith('Keith'))])
#print(d[d['height_cm']>170][['name','height_cm']])
#print(d[['height_cm','name','born_country']])
#print(d['name'])
e={'name':['A','B','C'],'age':[22,23,33],'marks':[33,77,88]}
f=pd.DataFrame(e)
print(f)
print(f.loc[0:2])
print(f.columns)
print(f.dtypes)
print(f.shape)
print(f[['name','marks']])
print(f['marks']>85)
f['passed']=np.where(f['marks']>40,f['marks'],0)
print(f.sort_values(['marks'],ascending=False))
f=f.rename(columns={'marks':'score'})
g=f['score'].mean()
print(f)
print(g)
h='pand.csv'
i=pd.read_csv(h)
#print(i.columns
#print(i.isna())
#print(i.isna().sum())
#print(i.fillna(1000))
#print(i.fillna(i.mean))
#print(i.isna().sum())
#print(i.fillna(i['Calories'].interpolate))

print(f.groupby(['passed'])['score'].mean())
k=pd.merge(i,a,left='NOC',right='NOC',how='left')
print(k)

#i=i.fillna()
