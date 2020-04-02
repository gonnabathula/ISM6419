#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
from sqlalchemy import create_engine


# In[35]:


db_file = r'C:/Users/gchin/Desktop/DV/Datasets/salesdata.db'
engine = create_engine(r"sqlite:///{}".format(db_file))


# In[40]:


import sqlite3
conn = sqlite3.connect(db_file)
conn_cursor = conn.cursor()
conn.text_factory = str
sql = conn.execute("select name from sqlite_master where type = 'table';")
for name in sql:
    print (name[0])


# In[36]:


sql = 'SELECT * from scores'

sales_data_df = pd.read_sql(sql, engine)
sales_data_df

