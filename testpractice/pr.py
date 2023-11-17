import pandas as pd

df = pd.read_csv('./auto-mpg.csv', header = None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
              'acceleration', 'model year', 'origin', 'name']
print(df)
print(df.mean(numeric_only=True))
import pandas as pd

df = pd.read_csv('./auto-mpg.csv', header = None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
              'acceleration', 'model year', 'origin', 'name']
print(df.mean(numeric_only = True))
print('\n')
print(df['mpg'].mean())
print(df.mpg.mean())
print('\n')
print(df[['mpg', 'weight']].mean())

print(df.median(numeric_only = True))
print('\n')
print(df.mpg.median())