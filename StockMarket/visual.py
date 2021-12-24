from matplotlib import pyplot as plt
import numpy as np
import seaborn as sb
from statsmodels.graphics.tsaplots import plot_acf
import pandas as pd
import plotly.express as px

'''
n this step, we’ll load the data and examine its header. In the dataset:

The “High” column represents the highest price in a day.
The “Low” column represents the lowest price in a day.
The “VWAP” column represents the volume-weighted average price.
VWAP = \frac{\sum(Volume * Price)}{\sum(Volume)}
​∑(Volume)
​
​∑(Volume∗Price)
​​ 

The “Volume” column represents the volume of the data.
'''
df = pd.read_csv("../dataset.csv", parse_dates=["Date"])
df.head()

'''We’ll now preprocess the data to make later analysis easier. For this, set the “Date” column as an index. This will make it bold-faced.

Then, filter the dates from 2008-05-26 to 2021-04-30. We can now convert an index to an ordinary column of the data frame.
'''
df.set_index("Date", drop=False, inplace=True)
df.head()
df.index.is_monotonic, df.index.is_unique
new_idx = pd.date_range("2008-05-26", "2021-04-30", freq="1D")
df = df.reindex(new_idx)
df.head()

'''Plot the volume of each day by using the Seaborn and plotly.express library.
'''

sb.set_theme()
sb.set(rc={'figure.figsize':(15,8)})
fig = px.line(df, x='Date', y="Volume")
fig.show()

'''Plot the highest price for each day using the plotly.express library.'''

fig = px.line(df, x='Date', y="High")
fig.show()

'''In a moving average, we consider a subset of data and calculate its average. In stock market analysis, the moving average smooths out short-term price fluctuations, and filters out the noise (outlier data that could confuse the model). This results in a clearer picture of the price trend as compared to the raw data.

Here is the formula to calculate the simple moving average (SMASMA):

SMA = \sum∑\frac{(Price,n)}{n}
​n
​
​(Price,n)
​​ '''
df_sma=df.copy()
df_sma['SMA_10']=df_sma.VWAP.rolling(10, min_periods=1).mean()
df_sma['SMA_20']=df_sma.VWAP.rolling(20, min_periods=1).mean()

plt.plot(df_sma['Date'], df_sma['VWAP'], color='blue')
plt.plot(df_sma['Date'],df_sma['SMA_10'], color='red')
plt.plot(df_sma['Date'],df_sma['SMA_20'], color='green')
plt.show()

'''The measure of autocorrelation represents the relationship between the current value of a variable with its past value. We can use it to check whether the elements in the time series data are positively correlated, negatively correlated, or independent of each other.

In this exercise, analyze the prices from the past to the recent time frame. You can use the autocorrelation function (ACFACF) at lag kk, denoted as ρk, shown below:

ρk = \frac{s_k}{s_0}
​s
​0
​​ 
​
​s
​k
​​ 
​​ 

Here, s​k​​ = cov(s​i​​, s​i+k​​) for any ii. The variance of the time series is s0​​. A plot of ρk against kk is known as a correlogram.'''
df.isnull().sum()
df['VWAP'].interpolate(method='linear',axis=0,inplace=True)
plot_acf(df['VWAP'], lags=50)
plt.show()

'''Heat maps use colored cells at different time frames to represent the intensity of the first variable of interest, such as price, temperature, rainfall, and so on. In this plot, analyze the prices of the stock at different time frames.'''
df_temp=df.copy()
df_temp['day'] = df_temp.index.day
df_temp['month'] = df_temp.index.month
df_temp['year'] = df_temp.index.year

df_m=df_temp.groupby(['month', 'year']).mean()
df_m
df_m=df_m.unstack(level=0)
fig, ax = plt.subplots(figsize=(11, 9))
sb.heatmap(df_m['VWAP'])
plt.show()

