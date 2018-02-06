import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# reading in text file
df = pd.read_csv("/Users/Tony/Dropbox/SRMP_shared/IRTF_SpeX (SRMP) - Dec_1224.tsv", sep="\t", comment="#", header=0)
df1 = pd.read_csv("/Users/Tony/Dropbox/SRMP_shared/IRTF_SpeX (SRMP) - SpeX_Jul4.tsv", sep="\t", comment="#", header=0)
df2 = pd.read_csv("/Users/Tony/Dropbox/SRMP_shared/IRTF_SpeX (SRMP) - Feb28.tsv", sep="\t", comment="#", header=0)
# df4 = pd.read_csv("/Users/Tony/Dropbox/SRMP_shared/BDKP.txt", sep="\s+", comment="#", header=0,
#                   names=['RA', 'DEC', 'J', 'K', 'PMRA', 'PMDEC', 'Vtan', 'SpT'], error_bad_lines=False)
# # error bad lines remove the lines that had 9 columns instead of 8
# df3 = pd.read_csv("/Users/Tony/Dropbox/SRMP_shared/LSPM2.txt", sep="\s+", comment="#", header=2,
#                   names= ['_RAJ2000', '_DEJ2000', 'pm', 'pmRA', 'pmDE', 'Jmag', 'Kmag'])
dfLSPM =pd.read_csv("/Users/Tony/Dropbox/SRMP_shared/LSPM-WISE-Table.txt", sep="\s+", comment="#", header=0, names=
['name', 'PM', 'W1', 'W1e', 'W2', 'W2e' , 'W3', 'W3e','W4', 'W4e', 'Jmag', "Jmage", 'Hmag','Hmage', "Kmag", 'Kmage'])
dfBDKP3A =pd.read_csv("/Users/Tony/Dropbox/SRMP_shared/BDKP3A.txt", sep="\s+", comment="#", header=None, names=
[ 'Name', 'Lgn', 'sptn', 'pmn', 'Jn', 'Jne', 'Hn', 'Hne', 'Kn', 'Kne', 'w1n', 'w1ne', 'w2n', 'w2ne', 'w3n', 'w3ne', 'w4n', 'w4ne'])
# dfBDKP3B =pd.read_csv("/Users/Tony/Dropbox/SRMP_shared/BDKP3B.txt", sep="\s+", comment="#", header=0, names=
# [ 'Name', 'Lgn', 'sptn', 'pmn', 'Jn', 'Jne', 'Hn', 'Hne', 'Kn', 'Kne', 'w1n', 'w1ne', 'w2n', 'w2ne', 'w3n', 'w3ne', 'w4n', 'w4ne'])
df4 = pd.read_csv("/Users/Tony/Dropbox/SRMP_shared/IRTF_SpeX (SRMP) - March 05.tsv", sep="\t", comment="#", header=0)
df5 = pd.read_csv("/Users/Tony/Dropbox/SRMP_shared/IRTF_SpeX (SRMP) - March 06.tsv", sep="\t", comment="#", header=0)
df6 = pd.read_csv("/Users/Tony/Dropbox/SRMP_shared/IRTF_SpeX (SRMP) - March04.tsv", sep="\t", comment="#", header=0)

# slicing data/removing columns (NAN)
df4 = df4.drop(df4.index[5:8])
df5 = df5.drop(df5.index[8:106])

# creating data frame for only files I need
df_rpm = df[['NAME', 'J', "J_err", "H", "H_err", "K", "K_err", "W1", "W1_err", 'Total Proper Motion',"2MASS Date",
             "WISE Date"]]
df1_rpm = df1[['NAME', 'J', "J_err", "H", "H_err", "K", "K_err", "W1", "W1_err", 'Total Proper Motion', "2MASS Date",
               "WISE Date"]]
df2_rpm = df2[['NAME', 'J', "J_err", "H", "H_err", "K", "K_err", "W1", "W1_err", 'Total PM b', "2MASS Date",
               "WISE Date"]]
df4_rpm = df4[['NAME', 'J', "J_err", "H", "H_err", "K", "K_err", "W1", "W1_err", 'Total Proper Motion', "2MASS Date",
               "WISE Date", "Designation"]]
df5_rpm = df5[['NAME', 'J', "J_err", "H", "H_err", "K", "K_err", "W1", "W1_err", 'Total Proper Motion', "2MASS Date",
               "WISE Date", "Designation"]]
df6_rpm = df6[['NAME', 'J', "J_err", "H", "H_err", "K", "K_err", "W1", "W1_err", 'Proper Motion b', "2MASS Date",
               "WISE Date", "Designation"]]

# rename
df2_rpm = df2_rpm.rename(columns={'Total PM b': 'Total Proper Motion', 'Total PM b': 'Total Proper Motion'})
df6_rpm = df6_rpm.rename(columns={'Proper Motion b': 'Total Proper Motion', 'Proper Motion b': 'Total Proper Motion'})
# combining files
frames = [df_rpm, df1_rpm, df2_rpm, df4_rpm, df5_rpm, df6_rpm]
result2 = pd.concat(frames)
# replace the Zero and start numbering the data
ignore_index = False
result2 = pd.concat(frames, ignore_index= True)


# Fixing Data
o=dfLSPM[(dfLSPM['PM'] < 0)]
dfLSPM = dfLSPM[dfLSPM.PM !=-0.163]
dfBDKP3A = dfBDKP3A[dfBDKP3A.Kn !=-100.000]
dfBDKP3A=dfBDKP3A[(dfBDKP3A['pmn'] > 0)]

# adding columns
result2["RPM J"] = result2["J"]+5*np.log10(result2["Total Proper Motion"]/1000)+5
result2["J-K color"] = result2["J"]-result2["K"]
dfLSPM['J-K Color'] = dfLSPM["Jmag"]-dfLSPM["Kmag"]
dfLSPM['RPM J'] = dfLSPM["Jmag"]+5*np.log10(dfLSPM['PM'])+5
dfBDKP3A['J-K Color'] = dfBDKP3A['Jn']-dfBDKP3A['Kn']
dfBDKP3A['RPM J'] = dfBDKP3A["Jn"]+5*np.log10(dfBDKP3A["pmn"])+5



# looking at points on J
q = result2[(result2['RPM J'] > 20)]
w = result2[(result2['J-K color'] > 2)]
e = result2[(result2["J-K color"] < 0)]
# adding the points together
frames4 = [ q, w, e ]
m = pd.concat(frames4)

# removing the duplicates
n = m.drop_duplicates(subset=['RPM J'], keep="first")


# Plotting J mag graph
plt.scatter(result2["J-K color"], result2["RPM J"], c="red", s=20, zorder=6,label='Our Data')
plt.scatter(dfLSPM["J-K Color"], dfLSPM["RPM J"], c="green", s=1, label="LSPM-Wise")
plt.scatter(dfBDKP3A["J-K Color"], dfBDKP3A["RPM J"], c="blue", s=1, label='BDKP3A')
plt.scatter(m["J-K color"], m["RPM J"], c="Yellow", s=20, zorder=6,label='Outliers')
plt.title("RPM J Graph", fontsize=15)
plt.xlabel("J-K color", fontsize=13)
plt.ylabel("RPM_J", fontsize=13)
plt.gca().invert_yaxis()
ax = plt.subplot(111)

# Creating Legend inside
ax.legend()
plt.show()


# Saving Figure
plt.savefig("/Users/Tony/Dropbox/SRMP_shared/RPM J(TZ) Graph")




# Turning outliers into txt
n.to_csv(r'/Users/Tony/Dropbox/SRMP_shared/J(TZ).txt', header=12, index=100, sep='\t', mode='a')


