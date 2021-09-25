import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np
import seaborn as sns 

# data=pd.read_csv("excel_vnm.csv")
# price=np.array(data["<CloseFixed>"])

# price=price[::-1]
# vol=np.array(data['<Volume>'])
# vol=vol[::-1]
# vol1=np.array(data['<LowFixed>'])
# T=22
# #ret=(price[T:]-price[:-T])/price[:T]
# plt.plot(price)
# plt.plot(vol,color="red")
# plt.plot(vol1)
# plt.legend()
# plt.show()
# import pandas
# Carpentries link for gapminder data
data_url = 'http://bit.ly/2cLzoxH'
#load gapminder data from url as pandas dataframe
gapminder = pd.read_csv(data_url)
print(gapminder.head(3))
gapminder_us = gapminder[gapminder.country=="United States"]
# create figure and axis objects with subplots()
# fig,ax=plt.subplots()
# ax.plot(gapminder_us.year, gapminder_us.lifeExp, marker="o")
# ax.set_xlabel("year")
# ax.set_ylabel("lifeExp")
# ax.plot(gapminder_us.year, gapminder_us["gdpPercap"], marker="o")
# plt.show()

# create figure and axis objects with subplots()
fig,ax = plt.subplots()
# make a plot
ax.plot(gapminder_us.year, gapminder_us.lifeExp, color="red", marker="o")
# set x-axis label
ax.set_xlabel("year",fontsize=14)
# set y-axis label
ax.set_ylabel("lifeExp",color="red",fontsize=14)
# twin object for two different y-axis on the sample plot
ax2=ax.twinx()
# make a plot with different y-axis using second axis object
ax2.plot(gapminder_us.year, gapminder_us["gdpPercap"],color="blue",marker="o")
ax2.set_ylabel("gdpPercap",color="blue",fontsize=14)
plt.show()
# save the plot as a file
fig.savefig('two_different_y_axis_for_single_python_plot_with_twinx.jpg',
            format='jpeg',
            dpi=100,
            bbox_inches='tight')