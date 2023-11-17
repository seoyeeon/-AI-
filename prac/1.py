import pandas as pd
import numpy as np

df = pd.read_csv('./auto-mpg.csv', header=None)
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower',
              'weight', 'acceleration', 'model year', 'origin', 'name']
df['horsepower'].replace('?', np.nan, inplace=True)
df.dropna(subset=['horsepower'], axis = 0, inplace=True)
df['horsepower'] = df['horsepower'].astype('float')

count, bin_dividers = np.histogram(df['horsepower'], bins=3)
print(count, bin_dividers)

bin_names = ['저출력', '보통출력', '고출력']
df['hp_bin'] = pd.cut(x=df['horsepower'], 
                      bins = bin_dividers, labels=bin_names,
                      include_lowest=True)
print(df[['horsepower', 'hp_bin']].head(15))

from sklearn import preprocessing

label_encoder=preprocessing.LabelEncoder()
onehot_encoder=preprocessing.OneHotEncoder()

onehot_labeled = label_encoder.fit_transform(df['hp_bin'].head(15))
print(onehot_labeled)

onehot_reshaped = onehot_labeled.reshape(len(onehot_labeled), 1)
print(onehot_reshaped)

onehot_fitted = onehot_encoder.fit_transform(onehot_reshaped)
print(onehot_fitted)