'''
금융 AI 포트폴리오를 만들것임. 

그러기 위해 첫번째로 **데이터 수집** 을 먼저 수행함. 

우선, 삼성전자의 과거 주가 데이터를 파이썬으로 직접 불러오겠다. 
'''

import FinanceDataReader as fdr
import pandas as pd

# 1. 삼성전자(종목코드:005930)의 2023년부터 현재까지의 데이터를 가져온다. 
# 종목코드는 6자리 숫자로 된 문자열을 입력해야 함. 
symbol = '005930'
df = fdr.DataReader(symbol, '2023-01-01')

# 2. 데이터가 잘 들어왔는지 상위 5줄만 확인해봄. 
print("--- 삼성전자 주가 데이터 상위 5행 ---")
print(df.head())

# 3. 데이터의 전반적인 정보를 확인. (데이터 개수, 컬럼 타입 등)
print("\n --- 데이터 정보 확인 ---")
df.info()

'''
Open : 시가
High : 고가
Low : 저가
Close : 종가 - 분석할때 보통 많이 사용함. 
Volume : 거래량 - 얼마나 많이 사고팔았는지
Change : 대비 - 전날 대비 등락률
'''

# 4. 수집한 데이터를 csv 파일로 저장해둔다. (나중에 불러오기 편하게)
df.to_csv('samsung_stock_2023_2024.csv')
print("\n 파일 저장이 완료되었습니다: samsung_stock_2023_2024.csv")