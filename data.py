import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
file_path = '한국전력거래소_시간별 전력수요량_20211231.csv'
supply = pd.read_csv(file_path, encoding='CP949')
print(supply)
print(supply.columns)
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
     13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
y = supply['날짜']
print(y.head())
# plt.bar(x,y)
# plt.xlabel('시각')
# plt.ylabel('전력수요')
