#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv("C:/Users/gchin/Desktop/DV/Datasets/gradedata.csv")
df.head()


# In[2]:


bins = [0, 80, 100]
group_names = ['Fail', 'Pass']


# In[3]:


df['P/F'] = pd.cut(df['grade'], bins,
labels=group_names)


# In[4]:


df.head()

