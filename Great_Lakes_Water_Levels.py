"""
To use this notebook for your in-class assignment, you will need these 
files, which you shoujld have downloaded:
* mhu.csv -- Lake Michigan and Lake Huron
* sup.csv -- Lake Superior
* eri.csv -- Lake Erie
* ont.csv -- Lake Ontario

As instructed in the in-class activity notebook for today, you are 
only expected to complete one PART below. Do not worry if your group 
is not big enough to finish all parts below, but if you have extra 
time, you're welcome to do so.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# PART 1
# Using the Michigan/Huron Dataset, plot the Water Level, the second 
# column, as a function of time years



# PART 2
# Using the Superior Dataset, plot the Water Level, the second column, 
# as a function of time years

sup_data = pd.read_csv("sup.csv")
water_level = sup_data["lake levels"]
time = sup_data["year"]

plt.plot(time, water_level)
plt.xlabel = "Year"
plt.ylabel = "water_level (unit)"
plt.show()

# PART 3
# Using the Erie Dataset, plot the Water Level, the second column, 
# as a function of time years

import matplotlib.pyplot as plt
import pandas as pd

erie = pd.read_csv('ERIE.csv')

plt.plot(erie.iloc[:, 0], erie.iloc[:, 1])
plt.title('Erie water levels')
plt.xlabel('time')
plt.ylabel('water level')
plt.grid()

# PART 4
# Using the Ontario Dataset, plot the Water Level, the second column, 
# as a function of time years
ontario_data=pd.read_csv("ont.csv")
years=ontario_data['year']
water_level=ontario_data['Lake Ontario annual averages']

plt.plot(years, water_level)
plt.xlabel("Years")
plt.ylabel("Water Level")


# PART 5
# Using the Michigan/Huron and Superior Datasets, plot the 
# Michigan/Hurion Water Level vs Superior Water Level to see if there 
# is any correlation between the water levels.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
mich_huron_water_level = pd.read_csv("mhu.csv", skiprows = 1)
superior_water_level = pd.read_csv("sup.csv",skiprows = 1)
mich_huron_water_level = mich_huron_water_level.iloc[:,1]
superior_water_level = superior_water_level.iloc[:,1]
plt.scatter(mich_huron_water_level,superior_water_level)
plt.title('Michigan/Huron Water Level vs Superior Water Level')
plt.xlabel('Michigan/Huron Water Level')
plt.ylabel('Superior Water Level')
plt.show()


# PART 6
# Using the Michigan/Hurion and Erie Datasets, plot the 
# Michigan/Huron Water Level vs Erie Water Level to see if there is 
# any correlation between the water levels.



# PART 7
# Using the Superior and Ontario Datasets, plot the Superior Water 
# Level vs Ontario Water Level to see if there is any correlation 
# between the water levels.


