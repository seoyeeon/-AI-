import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 가상의 데이터를 생성
environment_data = pd.DataFrame({
    'Factory': ['Factory_A', 'Factory_B', 'Factory_C','Factory_D','Factory_E','Factory_F','Factory_G','Factory_H','Factory_I','Factory_J'],
    'Emission': [10984, 15421, 4634, 5123, 9246, 3421, 3367, 7235, 13705, 6508],  # 가상의 오염물질 배출량 (환경 변수에 영향을 받는 값)
    'Environment': [2.1, 1.3, 5.0, 5.2, 7.5, 4.3, 4.7, 2.5, 8.9, 3.4]             # 가상의 환경 변수
})

# 수집된 데이터 인덱스 설정 및 출력
environment_data.set_index(environment_data.columns[0],inplace=True)
print(environment_data)

# 수집 데이터 정렬
environment_data = environment_data.sort_values(by='Emission')

# 두 개의 축을 이용하여 데이터 시각화
ax1 = environment_data['Emission'].plot(kind='bar',figsize=(15,8),width=0.7,color='red')
ax2 = ax1.twinx()
ax2.plot(environment_data.index, environment_data.Environment, marker='o',markersize=15,linestyle='None', color='blue',label='Environment')
ax1.set_ylim(0,20000)
ax2.set_ylim(0,10)
ax1.set_xlabel('Factory')
ax1.set_ylabel('Emission')
ax2.set_ylabel('Environment')
ax1.set_xticklabels(environment_data.index, rotation=0)
plt.title('Emission and Environmentfor Each Factory', size=20)

ax1.legend(loc='upper left', bbox_to_anchor=(0.01, 0.99))
ax2.legend(loc='upper left', bbox_to_anchor=(0.01, 0.94)) # 범례 설정

plt.show()

min_emission_index = environment_data['Emission'].idxmin()
min_environment_value = environment_data.loc[min_emission_index, 'Environment']

# 모든 행의 Environment 값을 최소값으로 대체
environment_data['Environment'] = min_environment_value

print(environment_data)

# 파일로 저장 (빅데이터 사용의 코드화)
environment_data.to_csv('environment_data.csv')

#-----------------------------------------------------------------#

# # 개선된 환경 변수를 바탕으로 다음 공정 진행
# # 빅데이터에 저장된 데이터를 가져와 전처리 진행
# df = pd.read_csv('environment_data.csv')
# df.set_index(df.columns[0],inplace=True)

# # 새로운 환경 변수를 random을 이용하여 4.7에서 파생되는 오차 환경 값으로 치환
# new_environment_values = np.round(np.random.uniform(low=4.7 - 1.5, high=4.7 + 1.5, size=len(df)), 2)
# df['Environment'] = new_environment_values

# # 가정된 최상의 환경 변수 값에서 실제 환경 변수 값의 차이로 각 행의 배출량 결정
# df['Emission'] = 3000 + np.abs(4.55 - df['Environment']) * 2500

# # 새로운 데이터의 정렬
# df = df.sort_values(by='Emission')
# print(df)

# # 두 개의 축을 이용하여 다음 공정 데이터 시각화
# ax1 = df['Emission'].plot(kind='bar',figsize=(15,8),width=0.7,color='red')
# ax2 = ax1.twinx()
# ax2.plot(df.index, df.Environment, marker='o',markersize=15,linestyle='None', color='blue',label='Environment')
# ax1.set_ylim(0,20000)
# ax2.set_ylim(0,10)
# ax1.set_xlabel('Factory')
# ax1.set_ylabel('Emission')
# ax2.set_ylabel('Environment')
# ax1.set_xticklabels(df.index, rotation=0)
# plt.title('Emission and Environmentfor Each Factory', size=20)

# ax1.legend(loc='upper left', bbox_to_anchor=(0.01, 0.99))
# ax2.legend(loc='upper left', bbox_to_anchor=(0.01, 0.94)) # 범례 설정

# plt.show()

# # 이후 모든 행의 Environment 값을 최소값으로 대체하여 빅데이터에 저장, 반복


