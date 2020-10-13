
# coding: utf-8

# # Module One Discussion: Descriptive Statistics and Plots
# 
# This notebook will take you step-by-step through the calculations required for your Module One discussion post. It is very important to run through the steps in order. Some steps depend on the outputs of earlier steps. Once you have completed the steps in this notebook, be sure to answer the questions about this activity in the discussion for this module.
# 
# Reminder: If you have not already reviewed the discussion prompt, please do so before beginning this activity. That will give you an idea of the questions you will need to answer with the outputs of this script.

# ## Initial post (due Thursday)

# ### Step 1: Preparing the dataset
# This block of Python code will generate the sample data in a Python dataframe that will be used in the calculations later. Your task is to use a website to collect the daily maximum temperature data for your city or zip code for the past fourteen days. Then, input your data in the code below by filling in the Python list. After entering your data in the Python list, click the code section below and hit the **Run** button above.

# In[1]:


# This module will be used to prepare a pandas dataframe and calculate descriptive statistics
import pandas as pd

# input your data in the Python list below. 
# For example, if your temperature data is:  81, 79, 80, 85, 83, 85, 87, 84, 84, 88, 85, 87
# then the step below should be set as:   temperatures = [81, 79, 80, 85, 83, 85, 87, 84, 84, 88, 85, 87]
temperatures = [74, 75, 87, 98, 98, 92, 90, 87, 87, 87, 87, 86, 86, 88]

# prepare a dataframe for temperatures.
temperatures_df = pd.DataFrame(temperatures, columns=['temperature'])

# print temperatures dataframe
print(temperatures_df)


#  

# ### Step 2: Calculating descriptive statistics
# The block of code below will calculate descriptive statistics for the data set you entered. The pandas dataframe has several methods that calculate descriptive statistics. Each method has a comment telling you what that method calculates.
# 
# Click the code section below and hit the **Run** button above.

# In[2]:


# Pandas dataframe has several methods that calculate descriptive statistics. 

# mean
mean = temperatures_df['temperature'].mean()
print("Mean=", round(mean,2))

# median
median = temperatures_df['temperature'].median()
print("Median=", round(median,2))

# variance
variance = temperatures_df['temperature'].var()
print("Variance=", round(variance,2))

# standard deviation
stdeviation = temperatures_df['temperature'].std()
print("Standard Deviation=", round(stdeviation,2))

# describe - a useful function that calculates several different descriptive statistics
statistics = temperatures_df['temperature'].describe()
print("")
print ("Describe method")
print (statistics)


#  

# ### Step 3: Line graph to display trend
# The block of code below will create a line plot of temperature data. You will use the matplotlib.pyplot submodule to create the line chart. 
# 
# Click the code section below and hit the **Run** button above.  
# NOTE: If the graph is not created, click the code section and hit the **Run** button again.

# In[4]:


import matplotlib.pyplot as plt

# line chart
plt.plot(temperatures_df['temperature']) # plot

# setting a title for the plot, x-axis and y-axis
plt.title('Line plot of temperature data', fontsize=20) 
plt.xlabel('day')
plt.ylabel('temperature')

# show the plot
plt.show()


#  

# ### Step 4: Side-by-side boxplots to compare distributions
# The block of code below will create side-by-side boxplots of your temperature data and the temperature data from another location called "Zion". Boxplots can be used to visually compare data distributions. In this code block, you will use the seaborn module in Python to create a side-by-side boxplot. 
# 
# The temperature data for Zion will be generated automatically in the code section below. You are not required to know how this data was generated. Note that the temperature data for Zion will be unique to you.
# 
# Click the code section below and hit the **Run** button above.  
# NOTE: If the graph is not created, click the code section and hit the **Run** button again.

# In[ ]:


import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import random

# creates temperature data for Zion. You don't need to know how this data is created. 
# The temperature data created for Zion will be unique to you. 
mean = random.randint(temperatures_df['temperature'].min(),temperatures_df['temperature'].max())
std_deviation = random.randint(round(temperatures_df['temperature'].std(),0),round(2*temperatures_df['temperature'].std(),0))
zion_temperatures = np.random.normal(mean, std_deviation, 25)
zion_temperatures = pd.DataFrame(zion_temperatures, columns=['temperature'])

# side-by-side boxplots require the two dataframes to be concatenated and require a variable identifying the data
temperatures_df['id'] = 'my_data'
zion_temperatures['id'] = 'zion_data'
both_temp_df = pd.concat((temperatures_df, zion_temperatures))

# sets a title for the plot, x-axis, and y-axis
plt.title('Boxplot for comparison', fontsize=20) 

# prepares the boxplot
sns.boxplot(x="id",y="temperature",data=both_temp_df)

# shows the plot
plt.show()


# ## End of initial post
# Attach the html output to your initial post in the Module One discussion. The HTML output can be downloaded by clicking **File**, then **Download as**, then **HTML**. Be sure to answer all questions about this activity in the Module One discussion.

#  

# ## Follow-up posts (due Sunday)
# Return to the Module One discussion to answer the follow-up questions in your response posts to other students. There are no Python scripts to run for your follow-up posts.
