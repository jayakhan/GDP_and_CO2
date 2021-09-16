import pandas as pd
import matplotlib.pyplot as plt

wdi = pd.read_csv("https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv")
print(wdi.head())

wdi_limited = wdi.loc[:,['Mortality rate, infant (per 1,000 live births)', 'GDP per capita (constant 2010 US$)', 'Country Name']]
print(wdi_limited.head())

plt.scatter('Mortality rate, infant (per 1,000 live births)', 'GDP per capita (constant 2010 US$)', data=wdi_limited)
plt.xlabel('Mortality rate, infant (per 1,000 live births)')
plt.ylabel('GDP per capita (constant 2010 US$)')
plt.show()



if __name__ == "__main__":
    pass
