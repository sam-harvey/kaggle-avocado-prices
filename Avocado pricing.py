
# coding: utf-8

# Setup

# In[6]:


#Download kernel data
get_ipython().system('mkdir data')
get_ipython().system('kaggle datasets download neuromusic/avocado-prices -p ./data')


# In[1]:


#Libraries
import pandas as pd
import numpy as np
import re as re


# In[18]:


df_avocado = pd.read_csv('data/avocado.csv')


# In[ ]:


df_avocado.drop(list(df_avocado)[0], axis=1, inplace = True)

#convert to snake case
df_avocado.columns = [i.replace(" ", "_") for i in df_avocado.columns]
df_avocado.columns = [re.sub("(?<=[a-z])(?=[A-Z])", "_", i) for i in df_avocado.columns]
df_avocado.columns = [i.lower() for i in df_avocado.columns]


# EDA

# In[11]:


df_avocado.head(5)


# In[15]:


df_avocado.dtypes


# In[19]:


df_avocado['avo_type_sum'] = df_avocado['4046'] + df_avocado['4225'] + df_avocado['4770']


# In[ ]:


#Sometimes the total volume differs


# In[20]:


total_test = df_avocado['avo_type_sum'] + df_avocado['Total Bags'] == df_avocado['Total Volume']


# In[26]:


len(total_test)


# In[27]:


sum(total_test)


# Modelling
