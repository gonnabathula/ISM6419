#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import glob
all_data = pd.DataFrame()
for f in glob.glob("C:/Users/gchin/Desktop/DV/Datasets/weekly_call_data/weekdata*.xlsx"):
    df = pd.read_excel(f)
all_data = all_data.append(df,ignore_index=True)
all_data.describe()


# In[5]:


writer = pd.ExcelWriter('mycollected_data.xlsx', engine='xlsxwriter')
all_data.to_excel(writer, sheet_name='Sheet1')
writer.save()

