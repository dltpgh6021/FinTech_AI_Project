# Day 1. Pandas 기초 (iloc, rolling) 및 시각화

 > TIL (Today I Learned)
 > - FinanceDataReader를 통한 주식 데이터 수집
 > - 수집된 데이터의 로컬 저장
 > - 주피터 환경에서 Pandas를 활용한 시계열 데이터 결측치 확인 및 전처리
 > - Matplotlib을 활용한 주가 추세선 시각화
 > - rolling 함수를 이용한 이동평균선 도출
 > - 스케일이 다른 다수 종목의 누적 수익률 정규화 및 비교 분석
 > - 그냥 인덱스가 아닌 iloc를 사용하는 이유

## FinanceDataReader
```py
import FinanceDataReader as fdr
import pandas as pd

symbol = '005930' # 삼성전자 종목 코드
df = fdr.DataReader(symbol, '2023-01-01')
```

fdr.DataReader 함수를 통해 특정 종목의 데이터를 가져올 수 있다. 

fdr.DataReader(종목코드, 시작일)

## 로컬 DB 저장
```py
df.to_csv('samsung_stock_2023_2024.csv)
```
위 to_csv 함수를 통해 df 객체에 저장된 데이터를 csv파일의 형태로 저장할 수 있다. 

## 주피터 환경에서 Pandas를 활용한 시계열 데이터 결측치 확인 및 전처리

주피터 환경은 사용자에게 매우 편리한 환경이다. 

사용자가 중간과정에서의 결과를 출력하고 싶을 때 간단히 출력 가능하며, </br>
줄단위로 실행이 가능하여 한줄 한줄 평가가 가능하다. 

VScode 에서 익스텐션으로 Jupyter 노트북을 설치한 후, 파일 확장자를 .ipynb로 하면 주피터 노트북을 사용 할 수 있다. 

## Matplotlib을 활용한 주가 추세선 시각화
```py
# 1. 이동평균선 데이터 만들기 (Pandas의 rolling 함수를 사용하면 아주 쉽습니다!)
# window=20 은 '최근 20일 치 데이터를 묶어서'라는 뜻이고, mean()은 '평균을 내라'는 뜻입니다.
df['MA20'] = df['Close'].rolling(window=20).mean() # 20일 이동평균선 (약 1달 추세)
df['MA60'] = df['Close'].rolling(window=60).mean() # 60일 이동평균선 (약 3달 추세)

# 2. 도화지 크기 설정
plt.figure(figsize=(12, 6))

# 3. 선 그리기
# 원래 주가(종가)는 배경처럼 연하게 깔아줍니다.
plt.plot(df.index, df['Close'], label='Samsung (Close)', color='lightgray', linewidth=1.5, alpha=0.7)

# 이동평균선을 눈에 띄게 그려줍니다.
plt.plot(df.index, df['MA20'], label='20-Day MA (1 Month)', color='orange', linewidth=2)
plt.plot(df.index, df['MA60'], label='60-Day MA (3 Months)', color='blue', linewidth=2)

# 4. 그래프 꾸미기
plt.title('Samsung Electronics: Price & Moving Averages', fontsize=16, fontweight='bold')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Price (KRW)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend() # 범례 표시 (어떤 선이 어떤 데이터인지)

# 5. 출력!
plt.show()
```

rolling 함수를 통해 20일치의 데이터를 묶는 열(MA20)을 만들고 60일 치 데이터를 묶는 열(MA60)을 만들고, 이를 출력하는 과정임. 

## rolling 함수를 이용한 이동평균선 (20일, 60일) 도출

rolling 함수는 여러 개의 값을 묶어주는 역할을 함. 

```py
arr = [1, 2, 3, 4, 5]

arr.rolling(window=3)
```

위와 같은 코드를 작성하게 되면, arr은 [1, 2, 3], [2, 3, 4], [3, 4, 5]의 값을 리턴하게 됨. 

그리고 이 뒤에 mean()이 붙는다면, 리턴값의 평균을 구하는 형태가 됨.

즉. arr.rolling(window=3).mean()을 한다면 2, 3, 4 가 리턴되는 것임. 

## 스케일이 다른 다수 종목의 누적 수익률 정규화 및 비교 분석

```py
import FinanceDataReader as fdr
import matplotlib.pyplot as plt

# 1. 두 종목 데이터 한 번에 가져오기
# 삼성전자(005930), 현대차(005380)
df_samsung = fdr.DataReader('005930', '2023-01-01')
df_hyundai = fdr.DataReader('005380', '2023-01-01')

# 2. 수익률 계산하기 (가장 핵심!)
# 첫 날(iloc[0])의 종가로 매일의 종가를 나누면, 첫 날을 '1(100%)'로 기준 잡은 누적 수익률이 나옵니다.
samsung_return = df_samsung['Close'] / df_samsung['Close'].iloc[0]
hyundai_return = df_hyundai['Close'] / df_hyundai['Close'].iloc[0]

# 3. 도화지 세팅 및 그래프 그리기
plt.figure(figsize=(12, 6))

# 수익률 선 그리기
plt.plot(samsung_return.index, samsung_return, label='Samsung Electronics', color='blue')
plt.plot(hyundai_return.index, hyundai_return, label='Hyundai Motors', color='green')

# 4. 기준선(원금, 1.0) 긋기
plt.axhline(y=1.0, color='red', linestyle='--', linewidth=1, label='Break-even (Principal)')

# 5. 그래프 꾸미기
plt.title('Cumulative Return Comparison (2023~): Samsung vs Hyundai', fontsize=16, fontweight='bold')
plt.xlabel('Date')
plt.ylabel('Cumulative Return (1.0 = 0%)')
plt.grid(True, alpha=0.5)
plt.legend()

plt.show()
```

우선 삼성전자와 현대차의 주가 그래프를 가져온다. 그리고, 각 데이터를 첫날의 종가로 나누어 준다. 

이렇게 한면 모든 날의 값이 종가의 값을 1으로 기준삼은 상대적인 값이 되기 때문에 주가변화, 즉 누적 수익률을 알아낼 수 있음. 

새로 구한 값을 통해 그래프를 그리면 누적 수익률을 볼 수 있고, 두 개의 주가를 함께 show 했기 때문에 어떤 주식의 수익률이 더 높은지 확인할 수 있음. 

## 그냥 인덱스가 아닌 iloc를 사용하는 이유

iloc의 뜻은 Integer Location임. <br>
말 그대로, 물리적인 순서만 보고 찾으라는 뜻임. 

여기서 df['Close'][0]과 같이 인덱스를 사용하는 것이랑 같지 않냐?? 라는 의문이 생길 수 있음. <br>
여기서 인덱스 0은 파이썬에게 혼동을 줄 수 있어서 사용하면 **안되는** 문법임

여기서 인덱스 0은 순서 0을 말할 수도 있고, 컬럼명이 0인 것을 말할 수도 있기 때문임. 요즘버전에서는 컬럼명이 0인게 없다면서 에러를 뱉음. => 오류 발생

그렇기 때문에 인덱스가 아닌 iloc를 사용하는 것. 