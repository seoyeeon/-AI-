import pandas as pd

df = pd.read_csv('stock-data.csv')

df['new_Date'] = pd.to_datetime(df['Date'])
df.set_index('new_Date', inplace=True)

print(df.head())
print('\n')
print(df.index)

#날짜 인덱스를 이용하여 데이터 선택하기
df_y = df.loc['2018']   #특정 연도 자료
print(df_y.head())
print('\n')
df_ym = df.loc['2018-07']
print(df_ym)
print('\n')
df_ymd = df.loc['2018-07-02']
print(df_ymd)
print('\n')
df_ym_cols = df.loc['2018-07', 'Start':'High']
print(df_ym_cols)
print('\n')
# df_ymd_range = df.loc['2018-06-20':'2018-06-25'] -> 23,24일이 비어서 오류남
# df_ymd_range = df[(df.index >= '2018-06-20') & (df.index <= '2018-06-25')]
#로 대신 써준다
# print(df_ymd_range)
print('\n')
df_ymd_list = df.loc[['2018-06-20', '2018-06-25']]
print(df_ymd_list)
print('\n')