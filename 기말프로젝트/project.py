import pandas as pd
import matplotlib.pyplot as plt
plt.rc('font', family='NanumGothic')

df = pd.read_excel('./연도별 배출량.xlsx',header = 1)

#결측값이 있는 열 제거
df.drop(df.columns[2], axis=1, inplace=True)
df.drop(df.columns[8], axis=1, inplace=True)

#1번째 열(연도)를 인덱스로 설정
df = df.rename(columns={df.columns[0]:'year'})

df.set_index(df.columns[0], inplace=True)
df = df.sort_values(by='year')

#연도별 총 오염물질 배출량
df3 = df.transpose()
df3['sum'] = df3.sum(axis=1)
df4 = df3[['sum']]
df4.plot(kind='barh')
plt.title('연도별 오염물질 합계')


df2 = df[['NOx','VOCs']]
df2.plot(kind = 'line')
plt.title('주요 오염물질 연도별 추이')
plt.xlabel('연도')
plt.ylabel('오염물질 합계')
plt.show()