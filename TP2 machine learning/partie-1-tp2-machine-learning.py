#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import csv 
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('./Property Prices in Tunisia.csv')
print(df)


# In[6]:


df.head()


# In[7]:


df.info()


# In[8]:


df.shape
df.describe()


# In[9]:


x=df['category'].unique()

y=df['category'].value_counts()

plt.bar(x,y)

plt.show()

sns.countplot(x=df['city'])


# In[17]:


fig,ax=plt.subplots()
v=df['city'][df.type=="À Vendre"]
l=df['city'][df.type=="À Louer"]
ax.hist(v)
ax.hist(l)


# In[20]:


sns.countplot(data=df,x='type')


# In[22]:


sns.countplot(y=df['city'],order=df.city.value_counts().index)


# In[27]:


df_app=df.loc[df['category']=='Appartements']
columns=['price','size']
df_app=df_app[columns]
df_app


# In[32]:


new_df=df[df.category=='Appartements'].copy()
columns=['price','size']
new_df=new_df[columns]
new_df


# In[30]:


plt.scatter(df_app['size'], df_app['price'])


# In[31]:


df_app_1=df.loc[df['category']=='Appartements']
columns=['log_price','size','type']
df_app_1=df_app_1[columns]
df_app_1


# In[34]:


plt.scatter(df_app_1['size'], df_app_1['log_price'])


# In[40]:


plt.scatter(df_app_1['size'][df_app_1.type=="À Vendre"], df_app_1['log_price'][df_app_1.type=="À Vendre"],c="cyan")
plt.scatter(df_app_1['size'][df_app_1.type=="À Louer"], df_app_1['log_price'][df_app_1.type=="À Louer"], c="green")


# In[ ]:





# In[ ]:




