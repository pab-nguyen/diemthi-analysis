import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, date, timedelta

df = pd.read_csv("sobaodanh.csv")
df['Today'] = pd.to_datetime("07/07/2020",format="%d/%m/%Y")
df['Ngày sinh'] = pd.to_datetime(df['Ngày sinh'],format = '%d/%m/%Y',errors='coerce')

df['Age'] = round((df['Today'] - df['Ngày sinh'])/timedelta(days=365))
print(df.head())

fig, ax = plt.subplots()
print(df['Age'].value_counts().to_frame())

# dftoan = df.loc[df['Toán']>-1]

# # fig, ax = plt.subplots()
# # ax.plot(df['Toán'])
# plt.show()