#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")


# In[2]:


df=pd.read_excel("Data_Train.xlsx")


# In[3]:


df.head()


# In[4]:


df.shape


# In[5]:


df.info()


# In[6]:


df.isnull().sum()


# In[7]:


df.isnull().sum().sum()


# In[8]:


df.describe()


# In[9]:


df.describe(include=object)


# In[10]:


df['Route'].mode()


# In[11]:


df['Route']=df['Route'].fillna(df['Route'].mode()[0])


# In[12]:


df['Total_Stops'].mode()


# In[13]:


df['Total_Stops']=df['Total_Stops'].fillna(df['Total_Stops'].mode()[0])


# In[14]:


df.isnull().sum()


# In[15]:


df.isnull().sum().sum()


# In[16]:


df['Date_of_Journey']=pd.to_datetime(df['Date_of_Journey'])


# In[17]:


df.head(20)


# In[18]:


df.info()


# In[19]:


df['Total_Stops'].unique()


# In[20]:


df.replace({"non-stop":0, "1 stop":1, "2 stops":2,"3 stops":3,"4 stops":4},inplace=True)


# In[21]:


df.head()


# In[22]:


df.head(20)


# In[23]:


df.info()


# # 1st Insight: How many Flight with respect to their stopages?

# In[24]:


df.groupby(['Total_Stops'])['Airline'].count()


# In[25]:


df['Total_Stops'].value_counts()


# In[26]:


df[df['Total_Stops']==4]


# In[27]:


plt.title('No. of flight stopage')
plt.hist(df['Total_Stops'],color='purple')
plt.xlabel('stopage')
plt.ylabel('No. of flight')
plt.xticks(df['Total_Stops'].unique())
plt.show()


# In[28]:


df.groupby(['Airline','Total_Stops'])['Total_Stops'].count()


# In[29]:


df.groupby(['Airline'])['Total_Stops'].count()


# In[30]:


plt.figure(figsize=(10,7))
plt.bar(df['Airline'],df['Total_Stops'])
plt.xlabel('Airline')
plt.ylabel('Total_Stops')
plt.xticks(rotation=90)
plt.show()


# In[31]:


x=df.copy()
x


# In[32]:


y=df.groupby(['Airline','Total_Stops'])['Total_Stops'].count().to_frame().rename(columns={'Total_Stops':'count'})
y


# In[33]:


z=pd.merge(x,y,on=['Airline','Total_Stops'],how='inner')
z


# In[34]:


sns.catplot(
    x='Airline', 
    y='count', 
    hue='Total_Stops', 
    kind='bar', 
    data=z, 
    height=6, 
    aspect=2
)
plt.xticks(rotation=45)  # Rotate x-axis labels for clarity
plt.title("Bar Plot of Count by Airline and Total Stops")
plt.show()


# # 2nd Insights: what flight is Expensive and cheaper ?
# 

# In[35]:


p=df.groupby(['Airline'])['Price'].agg(['min','max']).reset_index().sort_values(by='max',ascending=False)


# In[36]:


p


# In[37]:


plt.figure(figsize=(12,6))
plt.subplot(1,2,1)
plt.bar(p['Airline'],p['min'],label='min')
plt.xticks(rotation=90)
plt.legend()

plt.subplot(1,2,2)
plt.bar(p['Airline'],p['max'],label='max')
plt.xticks(rotation=90)
plt.legend()

plt.show()


# # 3rd insights: Variations of flight Price from source

# In[38]:


df.head()


# In[39]:


df['Source'].unique()


# In[40]:


df['Destination'].unique()


# In[41]:


df.replace({'New Delhi':'Delhi'},inplace=True)


# In[42]:


sd=df.groupby(['Source','Destination'])['Price'].sum().reset_index()


# In[43]:


sd


# In[44]:


sd1=df.groupby(['Source','Destination','Airline'])['Price'].agg(['sum','max','min','mean','count']).reset_index()
sd1


# In[45]:


plt.figure(figsize=(12,6))
sns.barplot(x='Source',y='Price',hue='Destination',data=df)
plt.xticks(rotation=90,size=15)
plt.title('variation of price by source')
plt.show()


# In[46]:


df.info()


# In[47]:


df['Date_of_Journey'].unique()


# In[48]:


df['Day_of_Journey']=df['Date_of_Journey'].dt.day
df['Month_of_Journey']=df['Date_of_Journey'].dt.month


# In[49]:


df['Day_of_Journey'].unique()


# In[50]:


df['Month_of_Journey'].unique()


# In[51]:


df.head(2)


# In[52]:


df.info()


# In[53]:


df['year_of_Journey']=df['Date_of_Journey'].dt.year


# In[54]:


df.head()


# In[55]:


df['year_of_Journey'].unique()


# In[56]:


df['year_of_Journey'].nunique()


# In[57]:


df.drop(columns=['year_of_Journey'],inplace=True)


# In[58]:


df.head()


# # 5th Insight: On What monthmaximum flight take off?

# In[59]:


plt.figure(figsize=(8,8))
Month=list(df['Month_of_Journey'])
Airline=list(df['Airline'])
plt.scatter(Airline,Month,marker='P',color='red')
plt.xticks(rotation=90)
plt.yticks(df['Month_of_Journey'].unique())
plt.title('Month having the maximum flight Take off')
plt.xlabel('Airline')
plt.ylabel('Month')
plt.show()


# # 6th Insights: What Month has The Maximum Earning

# In[60]:


p=df.groupby(['Month_of_Journey'])['Price'].agg(['sum']).reset_index().sort_values(by='sum',ascending=False)
p


# In[61]:


plt.bar(p['Month_of_Journey'],p['sum'])
plt.xticks(p['Month_of_Journey']);


# In[62]:


# Prices
z=df.groupby(['Month_of_Journey'])['Price'].agg(['sum']).iloc[:,0]
z=list(z)
z


# In[63]:


# Month
a=df.groupby(['Month_of_Journey'])['Price'].agg(['sum']).index
a=list(a)
a


# In[64]:


plt.bar(a,z)
plt.title('Prices')
plt.show()


# In[65]:


df['Airline'].unique()


# In[66]:


df['Airline'].nunique()


# # 7th Insights: Checking the Availablity of Flight with respect to Source and Destination

# In[67]:


df1=df.groupby(['Destination','Source'])['Airline'].value_counts()


# In[68]:


df1


# In[69]:


df


# In[ ]:




