
# coding: utf-8

# Setup

# In[6]:


#Download kernel data
get_ipython().system('mkdir data')
get_ipython().system('kaggle datasets download neuromusic/avocado-prices -p ./data')


# In[7]:


#Libraries
import pandas as pd
import numpy as np


# In[9]:


df_avocado = pd.read_csv('data/avocado.csv')


# EDA

# In[11]:


df_avocado.head(5)


# In[15]:


df_avocado.dtypes

