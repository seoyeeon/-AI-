import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# 개선된 환경 변수를 바탕으로 다음 공정 진행
# 빅데이터에 저장된 데이터를 가져와 전처리 진행
df = pd.read_csv('environment_data.csv')
df.set_index(df.columns[0],inplace=True)

# 새로운 환경 변수를 random을 이용하여 4.7에서 파생되는 오차 환경 값으로 치환
new_environment_values = np.round(np.random.uniform(low=4.7 - 1.5, high=4.7 + 1.5, size=len(df)), 2)
df['Environment'] = new_environment_values

# 가정된 최상의 환경 변수 값에서 실제 환경 변수 값의 차이로 각 행의 배출량 결정
df['Emission'] = 3000 + np.abs(4.55 - df['Environment']) * 2500

# 새로운 데이터의 정렬
df = df.sort_values(by='Emission')
print(df)

# 두 개의 축을 이용하여 다음 공정 데이터 시각화
ax1 = df['Emission'].plot(kind='bar',figsize=(15,8),width=0.7,color='red')
ax2 = ax1.twinx()
ax2.plot(df.index, df.Environment, marker='o',markersize=15,linestyle='None', color='blue',label='Environment')
ax1.set_ylim(0,20000)
ax2.set_ylim(0,10)
ax1.set_xlabel('Factory')
ax1.set_ylabel('Emission')
ax2.set_ylabel('Environment')
ax1.set_xticklabels(df.index, rotation=0)
plt.title('Emission and Environmentfor Each Factory', size=20)

ax1.legend(loc='upper left', bbox_to_anchor=(0.01, 0.99))
ax2.legend(loc='upper left', bbox_to_anchor=(0.01, 0.94)) # 범례 설정

plt.show()

# 이후 모든 행의 Environment 값을 최소값으로 대체하여 빅데이터에 저장, 반복
