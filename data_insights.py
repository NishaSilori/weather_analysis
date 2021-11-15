from importing_dataset import data
print(data.head(2))
print(data['Wind Speed_km/h'].nunique())
print(data['Wind Speed_km/h'].unique())
print(data['Weather'].value_counts())
print(data[data.Weather=="Clear"])
print(data.groupby('Weather').get_group('Clear'))
print(data.head(2))
print(data[data['Wind Speed_km/h']==4])
print(data.isnull().sum())
print(data.notnull().sum())
print(data.rename(columns={"Weather" : "Weather_condition"},inplace= True))
print(data.Visibility_km.mean())
print(data.Press_kPa.std())
print(data['Rel Hum_%'].var())
print(data[data['Weather_condition'].str.contains('Snow')])
print(data[(data['Wind Speed_km/h']>24) & (data['Visibility_km']==25)])
print(data.groupby('Weather_condition').mean())
print(data.groupby('Weather_condition').min())
print(data.groupby('Weather_condition').max())
print(data[data.Weather_condition=='Fog'])
print(data[(data.Weather_condition =='Clear') | (data.Visibility_km > 40)])
print(data[(data.Weather_condition=="Clear") & (data['Rel Hum_%']> 50) | (data.Visibility_km> 40)])













