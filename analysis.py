import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, date, timedelta
import os

#extract the file
os.chdir("C:/Users/nguyen_phan/Downloads/Data Science Projects/diemthi-analysis")
df = pd.read_csv("sobaodanh.csv")

#change 'dob' column values to datetime
df['dob'] = pd.to_datetime(df['dob'],format = '%d/%m/%Y',errors='coerce')
df = df.sort_values(by='dob')

#find age of exam takers at the time they take the test
df['Today'] = pd.to_datetime("07/07/2020",format="%d/%m/%Y")
df['Age'] = round((df['Today'] - df['dob'])/timedelta(days=365))
fig, ax = plt.subplots()
age = df['Age'].value_counts().rename_axis('age').reset_index(name='counts')


#histogram for people over 19 years old
n, bins, patches = plt.hist(df.loc[-df["Age"].isin([17,18,19])]["Age"],bins=int(max(age["age"]) - min(age["age"])))
xticks = [(bins[i+1] + value)/2 for i, value in enumerate(bins[:-1])]
xticks_labels = ["{:.0f}".format(value) for i, value in enumerate(bins[:-1])]
plt.xlabel("Age")
plt.ylabel("Count")
plt.xticks(xticks, labels = xticks_labels)
for i, value in enumerate(n):
    if value > 0:
        ax.text(xticks[i], value+5, int(value), ha='center',fontsize=8)


#Subjects
fig, ax = plt.subplots()
a = df[df.iloc[:,2:13]>-1].iloc[:,2:13].count().to_frame()
df[df.iloc[:,2:13]>-1].iloc[:,2:13].count().plot(ax=ax,kind="bar")
for i, value in enumerate(a[0]):
    plt.text(i, value+1000, int(value), ha='center',fontsize=8)
plt.title("Number of exam takers")
plt.xlabel("Subjects")
plt.ylabel("Count")

#First and Last Name
df['lastname'] = df['fullname'].str.split(" ").str[0]
df ['firstname'] = df["fullname"].str.split(" ").str[-1]
fig, ax = plt.subplots()
df["lastname"].value_counts().nlargest(10).plot(kind="barh" ).invert_yaxis()
plt.xlabel("Count")
plt.title("Top 10 last names")

fig, ax = plt.subplots()
df["firstname"].value_counts().nlargest(15).plot(kind="barh").invert_yaxis()
plt.xlabel("Count")
plt.title("Top 15 first names")


plt.show()

