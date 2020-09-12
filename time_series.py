import matplotlib.pyplot as plt
import matplotlib.dates as pltdates
import pandas as pd
import seaborn as sns
import numpy as np
import datetime
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv',parse_dates=['date'])
df = df.set_index(pd.DatetimeIndex(df['date']))

# df_cleaned = df.loc[df['value'] > df['value'].quantile(0.025)]
# df = df_cleaned.loc[df['value'] < df['value'].quantile(0.975)]
# Clean data
df = df.loc[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot

    df_copy = df.copy(True)
    plt.figure(figsize=(15,5))
    dates = df_copy['date']

    x_values = [d.date() for d in dates]
    y_values = df_copy['value']

    ax = plt.gca()

    formatter = pltdates.DateFormatter("%Y-%m")
    ax.xaxis.set_major_formatter(formatter)

    locator = pltdates.MonthLocator((1,7))
    ax.xaxis.set_major_locator(locator)

    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

    plt.plot(x_values, y_values)

    fig = plt.gcf()

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_cleaned1 = df.copy(True)
    df_cleaned1['year'] = df_cleaned1.index.year
    df_cleaned1['month'] = df_cleaned1.index.month
    df_bar = df_cleaned1.groupby(['year','month'])['value'].mean().to_frame().reset_index() 

    months_bars = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: [],
        10: [],
        11: [],
        12: []  
    }

    years = [2016, 2017, 2018, 2019]
    months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    month_colors = ['#76B8DA','#CE76DA','#A276DA','#DA76A9','#76DA7F','#DAAF76','#76C3DA','#D4DA76','#B976DA','#76D9DA','#DA768D','#DA76D4']

    barWidth = 0.03
    plt.figure(figsize=(20,15))

    for year in years:
        for month in months:
            bar = months_bars.get(month)
            data = df_bar.loc[(df_bar['year'] == year) & (df_bar['month']  == month)]
            if data.empty == True:
                data_val = 0.0  
            else:
                data_val = data.iloc[0]['value']    
            bar.append(data_val)
      

    x_index = np.arange(len(months_bars.get(1)))
    for month in months:
        bar = months_bars.get(month)
        if month < 5:
            adjust = -6 + month
        else:
            adjust = month - 6
        plt.bar(x_index+(adjust*barWidth), bar, color=month_colors[month-1], width=barWidth, edgecolor='white', label=month_names[month-1])

    
    plt.xlabel('Years', fontweight='bold')
    plt.xticks([r + barWidth/2 for r in range(len(months_bars.get(1)))], ['2016', '2017', '2018', '2019'], rotation=90)
    plt.ylabel('Average Page Views', fontweight='bold')
    plt.legend(title='Months')
    
    fig = plt.gcf()

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True, drop=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    fig, ax = plt.subplots(1,2, figsize=(20,8))

    sns.boxplot(x="year", y="value", data=df_box, ax=ax[0]).set(xlabel='Year', ylabel='Page Views', title='Year-wise Box Plot (Trend)')
    sns.boxplot(x="month", y="value", data=df_box, ax=ax[1], order=months).set(xlabel="Month", ylabel = "Page Views", title='Month-wise Box Plot (Seasonality)')


    fig = plt.gcf()


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
