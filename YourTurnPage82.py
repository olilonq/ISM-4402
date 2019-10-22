#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Can you create an age histogram categorized by gender?

import matplotlib.pyplot as plt
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
Location ="datasets/gradedata.csv"
df = pd.read_csv(Location)
df.hist(column="age", by="gender")


# In[ ]:




