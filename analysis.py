import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("sobaodanh.csv")
df.head()

# dftoan = df.loc[df['Toán']>-1]
# dftoan.value_counts().plot(kind ='bar')
# # fig, ax = plt.subplots()
# # ax.plot(df['Toán'])
# plt.show()