import pandas as pd

pr_m = pd.period_range(start='2019-01-01',
                       end=None,
                       periods=3,
                       freq='M')
print(pr_m)
print('\n')

ts_he = pd.date_range('2019-01-01', periods=6, 
                      freq='H',
                      tz='Asia/Seoul')
print(ts_he)
print('\n')

ts_3h = pd.date_range('2019-01-01', periods=6,
                      freq='3H',
                      tz='Asia/Seoul')
print(ts_3h)
