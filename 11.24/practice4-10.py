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

#서울에서 '충청남도', '경상북도', '강원도'로 이동한 인구데이터 값만 선택
col_years = list(map(str, range(1970, 2018)))
df_3 = df_seoul.loc[['충청남도', '경상북도', '강원도'], col_years]

#스타일 서식 지정
plt.style.use('ggplot')

#그래프 객체 생성(figure에 1개의 서브 플롯 생성)
fig = plt.figure(figsize=(20, 5))
ax = fig.add_subplot(1, 1, 1)

#axe객체에 plot 함수로 그래프 출력
ax.plot(col_years, df_3.loc['충청남도',:], marker='o',
        markerfacecolor='green', markersize=10, color='olive',
        linewidth=2, label='서울 -> 충남')
ax.plot()