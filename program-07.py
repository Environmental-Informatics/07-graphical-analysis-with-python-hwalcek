#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Due March 6, 2020
Created on Wed Mar  4 17:02:38 2020
by Hannah Walcek
Assignment 07 - Graphical Analysis with Python

Loads earthquake data from csv into dataframe earthquake_df and produces
six plots.
"""
#importing necessary packages
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import pylab

earthquake_df = pd.read_table('all_month.csv', sep=',')
#removing rows where mag is NaN
earthquake_df = earthquake_df[earthquake_df['mag'].notna()]

#histogram of earthquake magnitude with bin width of 1 and range of 0 to 10
plt.hist(earthquake_df['mag'], 
         bins=list(range(0, 11))) #must end at 11 to include 10
plt.title('Histogram of Earthquake Magnitude')
plt.ylabel('Occurrence')
plt.xlabel('Magnitude')
plt.savefig('hist.png')
plt.close()

#KDE plot for magnitude
density = stats.gaussian_kde(earthquake_df['mag']) #creating density
x = np.arange(0., 11, .05) #setting range and width
plt.plot(x, density(x)) #plotting x and density of x
plt.title('Kernel Density Plot of Earthquake Magnitude')
plt.ylabel('Probability')
plt.xlabel('Magnitude')
plt.savefig('kde.png')
plt.close()

#latitude versus longitude for all earthquakes
plt.scatter(x=earthquake_df['longitude'], 
            y=earthquake_df['latitude'], 
            s=2, c='blue') #setting point size and color
plt.title('Earthquake Distribution')
plt.ylabel('Latitude')
plt.xlabel('Longitude')
plt.savefig('lat_v_lon.png')
plt.close()

#cumulative distribution plot of earthquake depths
values, base = np.histogram(earthquake_df['depth'],  #making histogram
                            bins=len(list(range(0,11))))
cumulative = np.cumsum(values) #cumulative sum of values
plt.plot(base[:-1], cumulative, c ='blue') #plotting cumulative sum
plt.title('Cumulative Distribution Plot of Earthquake Depths')
plt.ylabel('Count')
plt.xlabel('Depth (km)')
plt.savefig('cdf.png')
plt.close()

#scatter plot of earthquake magnitude with depth
plt.scatter(x=earthquake_df['mag'], 
            y=earthquake_df['depth'], 
            s=2, c='red')
plt.title('Earthquake Depth vs. Magnitude')
plt.ylabel('Depth (km)')
plt.xlabel('Magnitude')
plt.savefig('mag_v_depth.png')
plt.close()

#Q-Q plot of earthquake magnitudes
stats.probplot(earthquake_df['mag'], dist="norm", plot=pylab) #normal dist
plt.title('Q-Q Plot of Earthquake Magnitudes')
plt.ylabel('Quantiles')
plt.xlabel('Theoretical Quantiles')
plt.savefig('qq.png')
plt.close()
