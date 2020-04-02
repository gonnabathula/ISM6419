#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
df = pd.read_csv("C:/Users/gchin/Desktop/DV/Datasets/gradedata.csv")
df.head()


# In[17]:


df.loc[(df['grade'] <=0,'grade')] = 0
df.head()

