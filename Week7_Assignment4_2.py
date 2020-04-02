#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv("C:/Users/gchin/Desktop/DV/Datasets/gradedata.csv")
df.head()


# In[5]:


import numpy as np
df['isBusy'] = np.where((df['exercise']>3)
& (df['hours']> 17),'YES', 'NO')
df.head(10)

