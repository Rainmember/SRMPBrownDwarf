from astropy.io import fits
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#install astro py

# then open the file with hdul
hdul = fits.open('/Users/Tony/Dropbox/SRMP_shared/IRTF-From-Daniel/FINISH151206_0044+0228.fits')
# check the header
#hdul.info()
#third bracket is error, 2nd flux, 1st wavelength
data = hdul[0].data

#Creating blank DF
df = pd.DataFrame()
#Creating new columns
df['Wavelength'] = data[0]
df["Flux"] = data[1]
df['Error'] = data[2]

df1 = df[(df['Wavelength'] >= 0.82)]
df2 = df1[(df1['Wavelength'] >= 1.86)&(df1['Wavelength'] <= 1.9)]

#getting rid of unwanted points
#df2["Flux"].argmax()
df1 = df1.drop(df.index[497])
df1 = df1.drop(df.index[496])
df1 = df1.drop(df.index[494])
df1 = df1.drop(df.index[495])
df1 = df1.drop(df.index[498])
df1 = df1.drop(df.index[499])
#Graphing
fig=plt.figure()
fig.set_size_inches(10, 6.45)
ax1 = fig.add_subplot(111)
plt.plot(df1["Wavelength"], df1["Flux"], c='indigo' ,zorder=100)
plt.xlabel("Wavelength ($\mu m$)", fontsize=25)
plt.ylabel("Flux ($erg\ s^{-1} cm^{-2} A^{-1}$)", fontsize=25)

for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)

ax1.tick_params(axis="both", which="major", labelsize=20, width=1.1, length=8)
ax1.annotate("2MASS J0044+0228",xy=(1.96,1.15*10**(-16)), fontsize=20)
ax1.annotate("Splat SpT: L6$\gamma$",xy=(1.96,1.075*10**(-16)), fontsize=20)
ax1.annotate("UTK SpT: L7",xy=(1.96,1.0*10**(-16)), fontsize=20)
ax1.annotate("J",xy=(1.15,1.9*10**(-17)), fontweight="bold", fontsize=20)
ax1.annotate("H",xy=(1.65,1.9*10**(-17)), fontweight="bold", fontsize=20)
ax1.annotate("K",xy=(2.2,1.9*10**(-17)), fontweight="bold", fontsize=20)

plt.xlim([0.7, 2.6])
plt.ylim([-4*10**(-18), 1.25*10**(-16)])
plt.tight_layout()

plt.savefig("/Users/Tony/Dropbox/SRMP_shared/0440+0228.png")

