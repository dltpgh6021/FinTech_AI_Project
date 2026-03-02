import pandas as pd
import matplotlib.pyplot as plt

# 1. 아까 저장해둔 csv 파일을 불러온다. 
# parse_dates = True를 하면 'Data' 컬럼을 단순한 글자가 아닌 '날짜' 형식으로 똑똑하게 인식한다. 
df = pd.read_csv('samsung_stock_2023_2024.csv', index_col='Date', parse_dates=True)

# 2. 도화지(그래프 창)의 크기를 설정한다 (가로12 세로6)
plt.figure(figsize=(12,6))

# 3. 꺾은선 그래프 그리기
# x축은 날짜, y축은 종가로 설정한다. 
plt.plot(df.index, df['Close'], label='Samsung (Close Price)', color='blue', linewidth=1.5)

# 4. 그래프 예쁘게 꾸미기
plt.title('Samsung electronics Stock Price (2023~)', fontsize=16, fontweight='bold')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Price (KRW)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

# 5. 완성된 그래프 출력
plt.show()