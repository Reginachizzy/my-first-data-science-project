
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np


# In[2]:

get_ipython().system('conda install -c anaconda xlrd --yes')


# In[3]:

df_can = pd.read_excel('https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DV0101EN/labs/Data_Files/Canada.xlsx',
                       sheet_name='Canada by Citizenship',
                       skiprows=range(20),
                       skipfooter=2)

print ('Data read into a pandas dataframe!')


# In[4]:

df_can.head(20)


# In[6]:

df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace = True)
df_can.head(10)


# In[7]:

df_can.shape


# In[8]:

df_can[columns]


# In[9]:

df_can.columns


# In[10]:

df_can.index


# In[11]:

df_can['Total'] = df_can.sum(axis=1)


# In[12]:

df_can.head(10)


# In[13]:

df_can.isnull().sum()


# In[14]:

df_can.set_index('Country', inplace = True)


# In[15]:

df_can.set_index('Continent', inplace = True)


# In[16]:

df_can.head(5)


# In[17]:

get_ipython().magic('matplotlib inline')

import matplotlib  as mpl
import matplotlib.pyplot as plt


# In[18]:

df_can.loc['Middle Africa']


# In[19]:

df_can.loc['Asia']


# In[20]:

df_can.loc['Asia', [1980, 1981, 1982]]


# In[21]:

years =df_can.loc['Asia', [1980, 1981, 1982, 2012]]
years.plot(kind = 'hist')


# In[22]:

numbers = list(map(str, range(1980, 2014)))


# In[25]:

graph = df_can.loc['Asia', (1980, 1981, 1982, 1983, 1984, 1985, 1986, 2010, 2011, 2012,2013)]
graph.plot(kind = 'bar')
plt.title('Asians that moved to canada')
plt.xlabel('years of migration')
plt.ylabel('population that migration')
plt.show()


# In[26]:

graph = df_can.loc['Asia', (1980, 1981, 1982, 1983, 1984, 1985, 1986, 2010, 2011, 2012,2013)]
graph.plot(kind = 'line')
plt.title('Asians that moved to canada')
plt.xlabel('years of migration')
plt.ylabel('population that migration')
plt.show()


# In[27]:




# In[ ]:

graph = df_can.loc['Asia', (1980, 1981, 1982, 1983, 1984, 1985, 1986, 2010, 2011, 2012,2013)]
graph.plot(kind = 'line')
plt.title('Asians that moved to canada')
plt.xlabel('years of migration')
plt.ylabel('population that migration')
plt.show()

