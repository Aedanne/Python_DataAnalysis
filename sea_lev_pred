import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    plt.scatter(x, y)


    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(x, y)    

    x1=pd.DataFrame({'Year':[i for i in range(df['Year'].min(), 2050)]})
    plt.plot(x1['Year'], intercept + slope*x1, 'r', label='First line of best fit')


    # Create second line of best fit
    df_2000 = df.loc[(df['Year'] >= 2000)]
    df_2000 = df_2000.copy(True)
    x_2000 = df_2000['Year']
    y_2000 = df_2000['CSIRO Adjusted Sea Level']  
    slope_2000, intercept_2000, r_value_2000, p_value_2000, std_err_2000 = linregress(x_2000, y_2000)

    x1=pd.DataFrame({'Year':[i for i in range(df_2000['Year'].min(), 2050)]})
    plt.plot(x1['Year'], intercept_2000 + slope_2000*x1, 'm', label='Second line of best fit')  

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level') 
    # plt.show() 

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
