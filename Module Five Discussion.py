
# coding: utf-8

# # Module Five Discussion: Correlation and Simple Linear Regression
# 
# This notebook contains the step-by-step directions for your Module Five discussion. It is very important to run through the steps in order. Some steps depend on the outputs of earlier steps. Once you have completed the steps in this notebook, be sure to answer the questions about this activity in the discussion for this module.
# 
# Reminder: If you have not already reviewed the discussion prompt, please do so before beginning this activity. That will give you an idea of the questions you will need to answer with the outputs of this script.
# 

# ## Initial post (due Thursday)
# _____________________________________________________________________________________________________________________________________________________

# ### Step 1: Generating cars dataset
# This block of Python code will generate the sample data for you. You will not be generating the dataset using numpy module this week. Instead, the dataset will be imported from a CSV file. To make the data unique to you, a random sample of size 30, without replacement, will be drawn from the data in the CSV file. The data set will be saved into a Python dataframe which you will use in later calculations. 
# 
# Click the block of code below and hit the **Run** button above. 

# In[1]:


import pandas as pd
from IPython.display import display, HTML

# read data from mtcars.csv data set.
cars_df_orig = pd.read_csv("https://s3-us-west-2.amazonaws.com/data-analytics.zybooks.com/mtcars.csv")

# randomly pick 30 observations without replacement from mtcars dataset to make the data unique to you.
cars_df = cars_df_orig.sample(n=30, replace=False)

# print only the first five observations in the data set.
print("\nCars data frame (showing only the first five observations)")
display(HTML(cars_df.head().to_html()))


#  

# ### Step 2: Scatterplot of miles per gallon against weight
# The block of code below will create a scatterplot of miles per gallon (coded as mpg in the data set) and weight of the car (coded as wt). 
# 
# Click the block of code below and hit the **Run** button above.  
# NOTE: If the plot is not created, click the code section and hit the **Run** button again.

# In[3]:


import matplotlib.pyplot as plt

# create scatterplot of variables mpg against wt.
plt.plot(cars_df["wt"], cars_df["mpg"], 'o', color='red')

# set a title for the plot, x-axis, and y-axis.
plt.title('MPG against Weight')
plt.xlabel('Weight (1000s lbs)')
plt.ylabel('MPG')

# show the plot.
plt.show()


#  

# ### Step 3: Correlation coefficient for miles per gallon and weight
# Now you will calculate the correlation coefficient between the miles per gallon and weight variables. The **corr** method of a dataframe returns the correlation matrix with correlation coefficients between all variables in the dataframe. In this case, you will specify to only return the matrix for the variables "miles per gallon" and "weight".
# 
# Click the block of code below and hit the **Run** button above. 

# In[4]:


# create correlation matrix for mpg and wt. 
# the correlation coefficient between mpg and wt is contained in the cell for mpg row and wt column (or wt row and mpg column) 
mpg_wt_corr = cars_df[['mpg','wt']].corr()
print(mpg_wt_corr)


#  

# ### Step 4: Simple linear regression model to predict miles per gallon using weight
# The block of code below produces a simple linear regression model using "miles per gallon" as the response variable and "weight" (of the car) as a predictor variable. The **ols** method in statsmodels.formula.api submodule returns all statistics for this simple linear regression model. 
# 
# Click the block of code below and hit the **Run** button above. 

# In[5]:


from statsmodels.formula.api import ols

# create the simple linear regression model with mpg as the response variable and weight as the predictor variable
model = ols('mpg ~ wt', data=cars_df).fit()

#print the model summary
print(model.summary())


#  

# ## End of initial post
# Attach the HTML output to your initial post in the Module Five discussion. The HTML output can be downloaded by clicking **File**, then **Download as**, then **HTML**. Be sure to answer all questions about this activity in the Module Five discussion.

#  

# ## Follow-up posts (due Sunday)
# Return to the Module Five discussion to answer the follow-up questions in your response posts to other students. There are no Python scripts to run for your follow-up posts.
