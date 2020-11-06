import matplotlib.pyplot as plt
import pandas as pd

URL_DATASET = r'https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv'
df1 = pd.read_csv(URL_DATASET)
df_india = df1[df1['Country'] == 'India']
df_india.plot(kind = 'bar', x = 'Date', y = 'Confirmed', color = 'blue')
ax1 = plt.gca()
df_india.plot(kind = 'bar', x = 'Date', y = 'Deaths', color = 'red', ax = ax1)
plt.show()
