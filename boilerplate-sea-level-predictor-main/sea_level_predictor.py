
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    print(df.head(10))
    # Create scatter plot
    plt.scatter(
        data= df,
        x= 'Year',
        y= 'CSIRO Adjusted Sea Level'
                )

    regress = linregress(df['Year'],
               df['CSIRO Adjusted Sea Level'])

    slope = regress.slope
    intercept = regress.intercept

    Years = range(1880 , 2051)
    Years2 = range(2000, 2051)
    sea_levels = [slope * year + intercept for year in Years]

    df2000 = df[df['Year'] >= 2000]

    regress2000 = linregress(df2000['Year'],
                             df2000['CSIRO Adjusted Sea Level'])

    slope2000 = regress2000.slope
    intercept2000 = regress2000.intercept
    
    sea_levels2000 = [slope2000 * year + intercept2000 for year in Years2]
    
    
    # Create first line of best fit
    plt.plot(
             Years,
             sea_levels
    )

    # Create second line of best fit
    plt.plot(
             Years2,
             sea_levels2000

    )

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()