import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, date, timedelta
import os

os.chdir("C:/Users/nguyen_phan/Downloads/Data Science Projects/diemthi-analysis")
df = pd.read_csv("sobaodanh.csv")

df = df.sort_values(by='Ngày sinh')


df['Ngày sinh'] = pd.to_datetime(df['Ngày sinh'],format = '%d/%m/%Y',errors='coerce')
df = df.sort_values(by='Ngày sinh')


df['Today'] = pd.to_datetime("07/07/2020",format="%d/%m/%Y")
df['Age'] = round((df['Today'] - df['Ngày sinh'])/timedelta(days=365))
fig, ax = plt.subplots()
age = df['Age'].value_counts().rename_axis('age').reset_index(name='counts')

# plt.bar(age.loc[age["age"]>16].iloc[:,0],age.loc[age["age"]>16].iloc[:,1])
# df['Age'].value_counts().plot(ax=ax, kind='bar')

#histogram for people over 19 years old
n, bins, patches = plt.hist(df.loc[-df["Age"].isin([17,18,19])]["Age"],bins=int(max(age["age"]) - min(age["age"])))
xticks = [(bins[i+1] + value)/2 for i, value in enumerate(bins[:-1])]
xticks_labels = ["{:.0f}".format(value) for i, value in enumerate(bins[:-1])]
plt.xticks(xticks, labels = xticks_labels)
for i, value in enumerate(n):
    if value > 0:
        plt.text(xticks[i], value+5, int(value), ha='center',fontsize=8)
plt.show()