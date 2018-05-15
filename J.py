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

#new object
df7 = pd.read_csv("/Users/Tony/Dropbox/SRMP_shared/IRTF_SpeX (SRMP) - Weirdo.tsv", sep="\t", comment="#", header=0)
df8 = pd.read_csv("/Users/Tony/Dropbox/SRMP_shared/IRTF_SpeX (SRMP) - From Daniel.tsv", sep="\t", comment="#", header=0)

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
df7_rpm = df7[['NAME', 'J', "J_err", "H", "H_err", "K", "K_err", "W1", "W1_err", 'Total Proper Motion', "2MASS Date",
               "WISE Date", "Designation"]]
df8_rpm = df8[['NAME', 'J', "J_err", "H", "H_err", "K", "K_err", "W1", "W1_err", 'Total Proper Motion', "2MASS Date",
               "WISE Date", "Designation"]]


# rename
df2_rpm = df2_rpm.rename(columns={'Total PM b': 'Total Proper Motion', 'Total PM b': 'Total Proper Motion'})
df6_rpm = df6_rpm.rename(columns={'Proper Motion b': 'Total Proper Motion', 'Proper Motion b': 'Total Proper Motion'})
# combining files
ourdata = [df_rpm, df1_rpm, df2_rpm, df4_rpm, df5_rpm, df6_rpm]


# replace the Zero and start numbering the data
ourdata = pd.concat(ourdata, ignore_index= True)
ourdata = ourdata.drop(59)

# Fixing Data
o=dfLSPM[(dfLSPM['PM'] < 0)]
dfLSPM = dfLSPM[dfLSPM.PM !=-0.163]
dfBDKP3A = dfBDKP3A[dfBDKP3A.Kn !=-100.000]
dfBDKP3A=dfBDKP3A[(dfBDKP3A['pmn'] > 0)]

# adding columns
ourdata["RPM J"] = ourdata["J"]+5*np.log10(ourdata["Total Proper Motion"]/1000)+5
ourdata["J-K color"] = ourdata["J"]-ourdata["K"]
dfLSPM['J-K Color'] = dfLSPM["Jmag"]-dfLSPM["Kmag"]
dfLSPM['RPM J'] = dfLSPM["Jmag"]+5*np.log10(dfLSPM['PM'])+5
dfBDKP3A['J-K Color'] = dfBDKP3A['Jn']-dfBDKP3A['Kn']
dfBDKP3A['RPM J'] = dfBDKP3A["Jn"]+5*np.log10(dfBDKP3A["pmn"])+5
df7_rpm["RPM J"] = df7_rpm["J"]+5*np.log10(df7_rpm["Total Proper Motion"]/1000)+5
df7_rpm["J-K color"] = df7_rpm["J"]-df7_rpm["K"]
df8_rpm["RPM J"] = df8_rpm["J"]+5*np.log10(df8_rpm["Total Proper Motion"]/1000)+5
df8_rpm["J-K color"] = df8_rpm["J"]-df8_rpm["K"]

#combine the background
frames5 = [dfLSPM, dfBDKP3A]
nm = pd.concat(frames5)

# looking at points on J
q = ourdata[(ourdata['RPM J'] > 20)]
w = ourdata[(ourdata['J-K color'] > 2)]


# adding the points together
OutlierOurData = [ q, w]
OutlierOurData = pd.concat(OutlierOurData)


# removing the duplicates
OutlierOurData = OutlierOurData.drop_duplicates(subset=['RPM J'], keep="first")


#removing duplicate 1800
df8_rpm = df8_rpm.drop(43)
#adding Spt type to Daniel's data
df8_rpm['Spt'] =['g','f','f','g','f','b','b','g','sd','b','f','f','f','f','f','g','f','b','g','g','sd','b','b','b','b','f','f'
    ,'f','b','b','b','f','g','sd','sd','f','f','b','f','f','f','f','f','f','f']

Gamma = df8_rpm[df8_rpm['Spt']=='g']
Beta = df8_rpm[df8_rpm['Spt']=='b']
Feild = df8_rpm[df8_rpm['Spt']=='f']
SubDwarf = df8_rpm[df8_rpm['Spt']=='sd']

Plot = [ourdata, df8_rpm]
Plot = pd.concat(Plot)


# Plotting J mag graph
fig=plt.figure()
ax1 = fig.add_subplot(111)
plt.scatter(OutlierOurData["J-K color"], OutlierOurData["RPM J"], c="#FF3030", s=25, zorder=100,label='Outliers')
plt.scatter(df7_rpm["J-K color"][0], df7_rpm["RPM J"][0], c="indigo", s=200, zorder=800, marker='*', label='J044+0228')
plt.scatter(df7_rpm["J-K color"][1], df7_rpm["RPM J"][1], c="#005200", s=200, zorder=800, marker='*', label='J2012+6726')
plt.scatter(df7_rpm["J-K color"][2], df7_rpm["RPM J"][2], c="yellow", s=200, zorder=800, marker='*', label='J2116+1555')
plt.scatter(Plot["J-K color"], Plot["RPM J"], c="#1874CD", s=20, zorder=6,label='Our Data')
plt.scatter(nm["J-K Color"], nm["RPM J"], c="#AEB3BF", alpha=0.25,s=1.5, label="Standard")
#plt.scatter(Gamma["J-K color"], Gamma["RPM J"], c="purple", alpha=1,s=25, label="Gamma")
#plt.scatter(Beta["J-K color"], Beta["RPM J"], c="orange", alpha=1,s=25, label="Beta")
#plt.scatter(Feild["J-K color"], Feild["RPM J"], c="yellow", alpha=1,s=25, label="Field")
#plt.scatter(SubDwarf["J-K color"], SubDwarf["RPM J"], c="green", alpha=1,s=25, label="Subdwarf")
plt.xlabel("$J-K$", fontsize=13)
plt.ylabel("H$_J$", fontsize=13)
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(2)
plt.gca().invert_yaxis()
ax = plt.subplot(111)
# Creating Legend inside
ax.legend(frameon=False)
plt.show()


# Saving Figure
plt.tight_layout()
plt.savefig("/Users/Tony/Dropbox/SRMP_shared/Poster_RPM_J_Graph3")



# Turning outliers into txt
n.to_csv(r'/Users/Tony/Dropbox/SRMP_shared/J(TZ).txt', header=12, index=100, sep='\t', mode='a')

m = m[(m["J-K color"] > 2.121)]

