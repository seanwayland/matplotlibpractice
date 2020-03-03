#!/usr/bin/env python
# coding: utf-8
# ## Observations and Insights
#
# ## Dependencies and starter code
# In[1]:

# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as st


# Study data files
mouse_metadata = "data/Mouse_metadata.csv"
study_results = "data/Study_results.csv"


# Read the mouse data and the study results
mouse_metadata = pd.read_csv(mouse_metadata)
study_results = pd.read_csv(study_results)
print(mouse_metadata.groupby('Mouse ID').count())


# Combine the data into a single dataset
ds = pd.merge(mouse_metadata, study_results, how="left", on=["Mouse ID"])


print(fourFive)


#print(ds)
# Generate a summary statistics table of mean, median, variance, standard deviation, and SEM of the tumor volume for each regimen

dsMean = pd.DataFrame(ds.groupby("Drug Regimen").mean())
dsMean = dsMean['Tumor Volume (mm3)']
dsMedian = pd.DataFrame(ds.groupby("Drug Regimen").median())
dsMedian = dsMedian['Tumor Volume (mm3)']
dsVar = pd.DataFrame(ds.groupby("Drug Regimen").var())
dsVar = dsVar['Tumor Volume (mm3)']
dsStd = pd.DataFrame(ds.groupby("Drug Regimen").std())
dsStd = dsStd['Tumor Volume (mm3)']
dsSem = pd.DataFrame(ds.groupby("Drug Regimen").sem())
dsSem = dsSem['Tumor Volume (mm3)']

dsStats = pd.DataFrame([dsMean,dsMedian,dsVar,dsStd,dsSem],index=['mean','Median','Var','Std','SEM'])
#print(dsStats)

# ## Summary statistics

# In[2]:

# ## Bar plots

# In[3]:

# Generate a bar plot showing number of data points for each treatment regimen using pandas


dsCount = ds.groupby("Drug Regimen").count()
dsCount['data points'] = dsCount['Mouse ID']
ax = dsCount.plot.bar(y = "data points")

# In[4]:

# Generate a bar plot showing number of data points for each treatment regimen using pyplot

#plt.bar(dsCount, x = 'Drug Regimen', y = 'data points', align='center', alpha=0.5)
labels = dsCount.index.tolist()
#print(labels)

plt.bar(labels, dsCount['Mouse ID'])
plt.title('Data Points by Drug Regimen')
#plt.show()

# ## Pie plots

# In[5]:
# Generate a pie plot showing the distribution of female versus male mice using pandas

SexCount = mouse_metadata.groupby("Sex").count()
SexCount['sex'] = SexCount['Mouse ID']

print(SexCount)
#plot = SexCount.plot.pie(y='sex')


# In[6]:

# Generate a pie plot showing the distribution of female versus male mice using pyplot

pie = plt.pie(SexCount['sex'])
plt.show()

# ## Quartiles, outliers and boxplots

# In[7]:

# Calculate the final tumor volume of each mouse across four of the most promising treatment regimens. Calculate the IQR and quantitatively determine if there are any potential outliers. 

fourFive = ds[ds['Timepoint']==45]

# get all mice for each drug
# Capomulin, Ramicane, Infubinol, and Ceftamin

# In[8]:

# Generate a box plot of the final tumor volume of each mouse across four regimens of interest

# ## Line and scatter plots

# In[9]:

# Generate a line plot of time point versus tumor volume for a mouse treated with Capomulin

# In[10]:

# Generate a scatter plot of mouse weight versus average tumor volume for the Capomulin regimen

# In[11]:

# Calculate the correlation coefficient and linear regression model for mouse weight and average tumor volume for the Capomulin regimen

# In[ ]:




