import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from time import sleep

URL_DATASET = r'https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv'
df = pd.read_csv(URL_DATASET, usecols = ['Date', 'Country', 'Confirmed'])
list_dates = df['Date'].unique()
fig, ax = plt.subplots(figsize=(15, 8))
list_countries = ['India', 'China', 'US', 'Italy', 'Spain']
list_colors = ['orange', 'red', 'blue', 'green', 'yellow']

def plot_bar(some_date):
    df2 = df[df['Date'].eq(some_date)]
    ax.clear()
    df3 = df2[df2['Country'].isin(list_countries)]
    sleep(0.2)
    return ax.barh(df3['Country'], df3['Confirmed'], color= list_colors)

my_anim = FuncAnimation(fig = fig, func = plot_bar,
                    frames= list_dates, blit=True,
                    interval=20)

path_mp4 = r'G:\Personal Projects\Covid-19 Data Analysis using Pandas and Matplotlib\population_covid2.html'  
my_anim.save(filename = path_mp4, writer = 'ffmpeg',
             fps=30,
             extra_args= ['-vcodec', 'libx264', '-pix_fmt', 'yuv420p'])
plt.show()
