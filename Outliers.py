import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


df9 = pd.read_csv("/Users/Tony/Dropbox/SRMP_shared/W_1(TZ).txt", sep="\t", comment="#", header=0)
df8 = pd.read_csv("/Users/Tony/Dropbox/SRMP_shared/J(TZ).txt", sep="\t", comment="#", header=0)
df10 = pd.read_csv("/Users/Tony/Dropbox/SRMP_shared/Outliers.txt", sep="\t", comment="#", header=0)
df11 = pd.read_csv("/Users/Tony/Dropbox/SRMP_shared/Outliers(TZ).txt", sep="\t", comment="#", header=0)
df10 = df10.rename(columns={'NAME': 'NAME'})
df11 = df11.rename(columns={'NAME': 'NAME'})

frames5 = [ df8, df9 ]
l = pd.concat(frames5)
z = l.drop_duplicates(subset=['NAME'], keep="first")
c = l.drop_duplicates(subset=['NAME'], keep=False)


# 2Mass Desgin and Date

# Del Columns

df12 = df11.drop(df11.columns[[0, 2]], axis=1)
# Reordering the Columns
z = z[['NAME', "Designation"]]






# comparing my data to other


frames6 = [df10, df12]
m = pd.concat(frames6)

mk = m.drop_duplicates(subset=['NAME'], keep="first")
md = m.drop_duplicates(subset=['NAME'], keep=False)


