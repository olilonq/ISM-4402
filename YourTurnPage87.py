#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Create a scatter plot of the hours and grade data in datasets/gradedata.csv.
#Do you see a pattern in the data?

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
Location ="datasets/gradedata.csv"
df = pd.read_csv(Location)
plt.scatter(df['hours'], df['grade'])

#Answer, yes there is a pattern in the data - More hours studying
#Correlate with a higher grade


# In[ ]:




