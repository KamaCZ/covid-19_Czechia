#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[3]:


obce = pd.read_csv("obce.csv")
obce


# In[4]:


obce.shape


# In[5]:


obce.describe()


# In[6]:


obce.values


# In[7]:


obce["obec_nazev"]


# In[20]:


konice = obce[obce["obec_nazev"] == "Konice"]

#df[df['W']>0]

konice
konice.to_excel("Konice_covdi19_pripaddy.xlsx",sheet_name="Sheet1")

budyne = obce[obce["obec_nazev"] == "Budyně nad Ohří"]
budyne.to_excel("Budyne_covid19_pripady.xlsx",sheet_name="Sheet1")
budyne


            




# In[9]:


# df['zip'].value_counts().head(5)
obce["obec_nazev"].value_counts().head(100)


# In[10]:


by_obec_nazev = obce.groupby("obec_nazev")


# In[11]:


by_obec_nazev.sum()


# In[12]:


by_obec_nazev.describe()


# In[13]:


obce.head


# In[14]:


testy = pd.read_csv("testy.csv")


# In[15]:


testy.describe()


# In[16]:


testy.head()


# In[ ]:




