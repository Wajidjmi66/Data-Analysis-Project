#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df=pd.read_csv('startup_funding.csv')
df


# In[3]:


df.info()


# In[4]:


df.isnull().sum()


# In[5]:


df.isnull().sum()/df.shape[0]*100


# In[6]:


df.drop(columns=['Remarks'],inplace=True)


# In[7]:


df


# In[8]:


df.set_index('Sr No',inplace=True)


# In[9]:


df


# In[10]:


# simplifying the columns names
df.columns=['date','startup','industry','subvertical','city','investors','round','amount']


# In[11]:


df


# In[12]:


df.info()


# In[13]:


df['amount'].fillna('0',inplace=True)


# In[14]:


df['amount'].isna().sum()


# In[15]:


df['amount']=df['amount'].str.lower().str.replace(',','').replace('undisclosed','0').replace('unknown','0')


# In[16]:


df.shape


# In[17]:


df=df[df['amount'].str.isdigit()]


# In[18]:


df


# In[19]:


df['amount'].nunique()


# In[20]:


df['amount'].astype('float')


# In[21]:


df['amount']=df['amount'].astype('float')


# In[22]:


df


# In[23]:


def to_inr(dollar):
    inr=dollar*84.73
    return inr/10000000


# In[24]:


df['amount']=df['amount'].apply(to_inr)


# In[25]:


df


# In[26]:


df['date']=pd.to_datetime(df['date'],errors='coerce')


# In[27]:


df.info()


# In[28]:


df.isnull().sum()/df.shape[0]*100


# In[29]:


df=df.dropna(subset=['date','startup','industry','city','investors','round','amount'])


# In[30]:


df.shape


# In[31]:


df


# In[32]:


df['startup'].unique()


# In[33]:


df.to_csv('final_startup_funding.csv',index=False)


# In[34]:


df['startup'].nunique()


# In[35]:


sorted(set(df['startup'].unique()))


# In[36]:


sorted(set(df['investors'].str.split(',').sum()))


# In[37]:


df['investors']


# In[38]:


df.sort_values(by='date',ascending=False)[df['investors'].str.contains('Softbank')].head()[['date','startup','subvertical','city','round','amount']]


# In[39]:


df[df['investors'].str.contains('Softbank')][['date','startup','subvertical','city','round','amount']].sort_values\
(by='date',ascending=False).head()


# In[40]:


df[df['investors'].str.contains('Softbank')].groupby(['startup'])['amount'].sum().sort_values(ascending=False).head()


# In[41]:


df[df['investors'].str.contains('Softbank')].groupby(['subvertical'])['amount'].sum().sort_values(ascending=False).head()


# In[42]:


df['year']=df['date'].dt.year


# In[43]:


df[df['investors'].str.contains('Softbank')].groupby(['year'])['amount'].sum().sort_values(ascending=False).head().plot()


# In[44]:


round(df['amount'].sum())


# In[45]:


round(df['amount'].max())


# In[46]:


round(df['amount'].mean())


# In[47]:


df['startup'].nunique()


# In[48]:


df['month']=df['date'].dt.month


# In[49]:


df


# In[50]:


temp=df.groupby(['year','month'])['amount'].sum().reset_index()
temp


# In[51]:


temp['x_axis']=temp['month'].astype(str)+'-'+temp['year'].astype(str)


# In[52]:


temp


# In[53]:


df.groupby(['year','month'])['startup'].count()


# In[54]:


df.groupby(['year','month'])['amount'].count()


# In[55]:


df


# In[56]:


df[df['startup']=='BYJU’S']


# In[57]:


df[df['startup']=='BYJU’S']['industry']


# In[58]:


x=df[df['startup']=='ABI Health']['industry']


# In[59]:


x


# In[ ]:





# In[60]:


df[df['startup']=='ABI Health']['industry']


# In[61]:


list(x)


# In[62]:


x


# In[63]:


w=list(x)


# In[64]:


type(w)


# In[65]:


w


# In[ ]:




