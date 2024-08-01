#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# pip install papermill


# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt


# In[ ]:


f = '../../data/Temixco_2018_10Min.parquet'
tmx = pd.read_parquet(f)


# In[ ]:


tmx_latex = tmx.mean().to_latex()
tmx_latex


# In[ ]:


with open('../../latex/tabla_promedios.tex', 'w') as file:
    file.write(tmx_latex)


# # 1 Save and export notebook as executable script

# In[ ]:




