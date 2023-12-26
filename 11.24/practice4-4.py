import pandas as pd
import matplotlib.pyplot as plt
plt.rc('font', family='NanumGothic')

df=pd.read_excel('시도별 전출입 인구수.xlsx', header=0)    

#누락값을 앞 데이터로 채움
df = df.ffill()

#서울에서 다른 지역으로 이동한 데이터만 추출하여 정리
mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'], axis=1)
df_seoul.rename({'전입지별':'전입지'}, axis=1, inplace=True)
df_seoul.set_index('전입지', inplace=True)
print(df_seoul.head())

#서울에서 경기도로 이동한 인구 데이터 값만 선태
sr_one = df_seoul.loc['경기도']

#그림 사이즈 지정(가로 14인치, 세로 5인치)
plt.figure(figsize=(14, 5))

#x축 눈금 라벨 회전하기
plt.xticks(rotation='vertical')

#x, y축 데이터를 plot함수에 입력
plt.plot(sr_one.index, sr_one.values)

#판다스 객체를 plot 함수에 입력
plt.plot(sr_one)

plt.title('서울->경기 인구 이동')

plt.xlabel('기간')
plt.ylabel('이동 인구수')

plt.legend(labels=['서울 -> 경기'], loc='best')

plt.show()