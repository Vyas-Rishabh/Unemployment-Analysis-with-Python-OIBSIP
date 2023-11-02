#!/usr/bin/env python
# coding: utf-8

# # Unemployment Analysis

# In[1]:


#importing Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')


# In[2]:


#loading our dataset
unemp = pd.read_csv("Unemployment in India.csv")
unemp.head()


# In[3]:


# dataset information
unemp.info()


# In[4]:


# print random 5 rows
unemp.sample(5)


# In[5]:


# find null values
unemp.isna().sum()


# In[6]:


unemp.describe()


# In[7]:


unemp['Area'].value_counts()


# In[8]:


unemp['Region'].value_counts()


# In[10]:


unemp[' Date'].value_counts()


# In[11]:


# there's a typo in frequency values
unemp[' Frequency'].value_counts()


# In[13]:


# checking the correlation between Estimated Employed and Estimated Unemployment Rate (%)
unemp[' Estimated Employed'].corr(unemp[' Estimated Unemployment Rate (%)'])


# ### Data Cleaning

# In[14]:


# Dropping null values and frequency column
df2 = unemp.dropna().drop(columns=[' Frequency'])
df2


# In[22]:


# renaming columns name
df3 = df2.rename(columns={'Region':'region', ' Date':'date', ' Estimated Unemployment Rate (%)':'est_unemp_perc', \
                         ' Estimated Employed':'est_mil_emp', ' Estimated Labour Participation Rate (%)':'est_labour_perc', \
                         'Area':'area'}).reset_index(drop = True)


# In[23]:


df3


# In[24]:


# checking the duplicates
df3.duplicated().sum()


# In[26]:


# checking the outliers
sns.boxplot(data=df3, x='region', y='est_unemp_perc')
plt.title('Detecting Outliers in Unemployment rates per region')
plt.ylabel('Unemployment percentage')
plt.xticks(rotation = 90)
plt.show()


# ### Data Visualization

# In[31]:


# particiation rate per month
sns.lineplot(data=df3, x='date', y='est_labour_perc', hue='area', errorbar=None)
plt.title('Percetntage of participation rate per month')
plt.xlabel('Date')
plt.ylabel('Labour participation rate')
plt.xticks(rotation=70)

plt.show()


# In[37]:


df5 = df3.groupby('region')[['est_unemp_perc']].mean().sort_values(by='est_unemp_perc', ascending= False)
df5.plot(kind='bar')
plt.title('Estimated unemployment percentage per region')
plt.ylabel('Unemployment percentage')
plt.xticks(rotation=90)
plt.figtext(x= 0.18, y=0.75, s='Tripura has the highest\n unemplyment percentage\n of all regions')
plt.show()


# In[38]:


# area wise unemplyment rate
sns.barplot(data=df3, x='area', y='est_unemp_perc')
plt.title('Average unemployment percentage per area')
plt.ylabel('Unemployment percentage')
plt.show()


# Rural area has a lower unemployment percentage than urban areas. <br>
# <br>

# In[48]:


ax1 = df3.groupby('region')['est_unemp_perc'].agg(lambda x: max(x) - min(x)).sort_values(ascending= False).plot(kind='bar')
plt.suptitle('The difference in unemployment rate per rigion')
plt.title('Maximum Rate - Minimum Rate')
plt.figtext(x= 0.15, y= 0.75, s='Puducherry is the most affected'
                                '\nby the crisis with more then'
                                '\n70% difference in unemployment rate')
plt.show()


# <h3>Conclusion</h3>
# 
# 1. During the peak of the crisis in April 2020, the labor force participation rate reached its lowest point, indicating a significant decrease in economic activity.
# 
# 2. Visualizations show that urban areas generally experienced higher unemployment rates compared to rural areas.
# 
# 3. Some states, such as Meghalaya, had the fewest employees but also the lowest unemployment rates. In contrast, states like Puducherry were severely impacted by the crisis.

# You can find this project on <a href='https://github.com/Vyas-Rishabh/Unemployment-Analysis-with-Python-OIBSIP'><b>GitHub.</b></a>
