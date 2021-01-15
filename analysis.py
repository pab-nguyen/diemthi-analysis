import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, date, timedelta
import os

os.chdir("C:/Users/nguyen_phan/Downloads/Data Science Projects/diemthi-analysis")
df = pd.read_csv("sobaodanh.csv")

df = df.sort_values(by='Ngày sinh')

print(df.head(10))

df['Ngày sinh'] = pd.to_datetime(df['Ngày sinh'],format = '%d/%m/%Y',errors='coerce')
df = df.sort_values(by='Ngày sinh')

df.loc["Ngày sinh" != ]
print(df.head(10))