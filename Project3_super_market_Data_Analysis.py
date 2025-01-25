#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df=pd.read_csv('supermarket_sales - Sheet1.csv')
df.head()


# - Invoice id: Computer generated sales slip invoice identification number
# 
# - Branch: Branch of supercenter (3 branches are available identified by A, B and C).
# 
# - City: Location of supercenters
# 
# - Customer type: Type of customers, recorded by Members for customers using member card and Normal for without member card.
# 
# - Gender: Gender type of customer
# 
# - Product line: General item categorization groups - Electronic accessories, Fashion accessories, Food and beverages, Health and beauty, Home and lifestyle, Sports and travel
# 
# - Unit price: Price of each product in $
# 
# - Quantity: Number of products purchased by customer
# 
# - Tax: 5% tax fee for customer buying
# 
# - Total: Total price including tax
# 
# - Date: Date of purchase (Record available from January 2019 to March 2019)
# 
# - Time: Purchase time (10am to 9pm)
# 
# - Payment: Payment used by customer for purchase (3 methods are available – Cash, Credit card and Ewallet)
# 
# - COGS: Cost of goods sold
# 
# - Gross margin percentage: Gross margin percentage
# 
# - Gross income: gross income is all the money you earn before taxes and other deductions are subtracted.
# 
# - Rating: Customer stratification rating on their overall shopping experience (On a scale of 1 to 10)

# In[3]:


total=(df['Unit price']*df['Quantity'])+df['Tax 5%']
total


# In[4]:


522.83*7


# In[5]:


522.8299999999999+(522.8299999999999*(5/100))


# In[6]:


#  Gross Margin % = (Revenue – Cost of Goods Sold) / Revenue x 100
gross_Margin=(df['Total']- df['cogs'])/df['Total']*(100)
gross_Margin


# In[7]:


df.shape


# In[8]:


df.info()


# In[9]:


df.describe()


# In[10]:


df.isna().sum()


# In[11]:


df['City']


# In[12]:


for i in df:
    if df[i].dtype=='object':
        print(i,'.......',df[i].dtype)


# In[13]:


# find object variables in dataset

obj= [i for i in df if df[i].dtype=='object']

print('The object variables are :',obj)


# In[14]:


# find numerical variables in dataset

numerical = [col for col in df if df[col].dtype!='object']

print('The numerical variables are :', numerical)


# # Categorical Variables

# In[15]:


df.head()


# In[16]:


for i in obj:
    if i!='Invoice ID' and i!='Date' and i!='Time':
        print(i,'...',df[i].nunique(),'......',df[i].unique())
        print(df[i].value_counts(),'\n')




# ### If we don not use the above code we have to write the code for each endex indivisualy like below.

# In[17]:


print("The count of unique values in Branch variable is ",df['Branch'].nunique())
print("The unique values in Branch variable are ",df['Branch'].unique())


# In[18]:


print("The count of unique values in City variable is ",df['City'].nunique())
print("The unique values in City variable are ",df['City'].unique())


# In[19]:


print("The count of unique values in Customertype variable is ",df['Customer type'].nunique())
print("The unique values in Customertype variable are ",df['Customer type'].unique())


# In[20]:


print("The count of unique values in Gender variable is ",df['Gender'].nunique())
print("The unique values in Gender variable are ",df['Gender'].unique())


# In[21]:


print("The count of unique values in Payment variable is ",df['Payment'].nunique())
print("The unique values in Payment variable are ",df['Payment'].unique())


# In[22]:


print("The count of unique values in Productline variable is ",df['Product line'].nunique())
print("The unique values in Productline variable are ",df['Product line'].unique())


# In[23]:


df[obj].head()


# In[24]:


z=df.select_dtypes(include='object')
z.head()


# In[25]:


import warnings
warnings.filterwarnings('ignore')
sns.set_style('whitegrid')


# In[26]:


plt.figure(figsize=(22,20),dpi=600)
c=1
for i in z:
    if i!='Invoice ID' and i!='Date' and i!='Time' :
        
        plt.subplot(2,3,c)
        sns.countplot(x = z[i], data = z,palette='Set1')
        if i!='Product line':
            plt.xticks(fontsize=20)
            plt.xlabel(i,fontsize=30)
            c=c+1 # c+=1
        else:
            plt.xticks(rotation=90,fontsize=20)
            plt.xlabel(i,fontsize=30)
            c=c+1 # c+=1
        
            
plt.show()

        


# In[27]:


plt.figure(figsize=(22,6))
plt.subplot(1,5,1)
sns.countplot(x = 'Branch', data = df)
plt.subplot(1,5,2)
sns.countplot(x = 'City', data = df)
plt.subplot(1,5,3)
sns.countplot(x = 'Customer type', data = df)
plt.subplot(1,5,4)
sns.countplot(x = 'Gender', data = df)
plt.subplot(1,5,5)
sns.countplot(x = 'Payment', data = df)

plt.show()


# In[28]:


sns.countplot(x = 'Product line', data = df)
plt.xticks(rotation=90);


# ## Analyzing the data

# ##### WHICH IS THE BEST PRODUCT LINE FOR EACH BRANCH ?

# In[29]:


a=df.groupby(['Product line','Branch'])['gross income'].agg(['count','mean'])
a


# In[30]:


k=df.groupby(['Product line','Branch'])['gross income'].agg(['count','mean']).reset_index()
k


# In[31]:


plt.title('Gross Income of each branch')
sns.barplot(x='Product line',y='mean',hue='Branch',data=k)
plt.legend(loc='right',bbox_to_anchor=(1, 1))
plt.xticks(rotation=90);


# In[32]:


df.head()


# ### Insigth 1 :WHICH IS THE BEST SELLING BRANCH ?

# In[33]:


l=df.groupby(['Branch'])['gross income'].sum().reset_index()
l


# In[34]:


plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.pie('gross income',labels='Branch',data=l,autopct='%0.2f%%')
plt.subplot(1,2,2)
sns.barplot(x='Branch',y='gross income',data=l);


# ### Insight 2:WHICH BRANCH HAS HIGH RATING?

# In[35]:


u=df.groupby(['Branch'])['Rating'].mean().reset_index()
u


# In[36]:


plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.pie('Rating',labels='Branch',data=u,autopct='%0.2f%%')
plt.subplot(1,2,2)
sns.barplot(x='Branch',y='Rating',ci=None,data=u);


# so the branch c is the most branch have a high gross income and high rating so we select this branch to analysis it and create dataframe

# In[37]:


c=df[df['Branch']=='C']
c


# ### insights 3: classify gross income based on customer type in branch C?

# In[38]:


c.groupby(['Customer type'])['gross income'].sum().reset_index()


# In[39]:


c['Customer type'].value_counts()


# In[40]:


sns.countplot(x='Customer type',data=c);


# In[41]:


df.head(2)


# ### Insight 4: Which day has most gross income ?

# In[42]:


df['Date']=pd.to_datetime(df['Date'])


# In[43]:


df['Days']=df['Date'].dt.day_name()


# In[44]:


df['month']=df['Date'].dt.month_name()


# In[45]:


df


# In[46]:


df['Days'].unique()


# In[47]:


# df['Weeks']=df['Days'].apply(lambda a :'Weekday' if a=='Monday' or a=='Tuesday' or a=='Wednesday'or a=='Thursday' or a=='Friday' else 'Weekend')


# In[48]:


df['Weeks']=df['Days'].apply(lambda a :'Weekend' if a=='Saturday' or a=='Sunday' else 'Weekday')


# In[49]:


df.head(2)


# In[50]:


df.groupby(['Weeks'])['gross income'].sum()


# In[51]:


i=df.groupby(['month','Days'])['gross income'].sum().reset_index().sort_values(by='gross income',ascending=False)
i


# In[52]:


df.groupby('month')['gross income'].sum().reset_index().sort_values(by='gross income',ascending=False)


# In[53]:


sns.barplot(x='Days',y='gross income',hue='month',data=i)
plt.xticks(rotation=45);


# ### Insight 5 :what mode of payment is high ?

# In[54]:


sns.countplot(x='Payment',data=c);


# In[55]:


c['Payment'].value_counts()


# In[56]:


df.groupby(['Gender','Customer type'])['gross income'].sum()


# In[57]:


df.groupby(['Gender','Customer type','Payment'])['gross income'].agg(['sum','count'])


# In[58]:


sns.catplot(x='Payment',hue='Gender',kind='count',col='Customer type',data=c);
 


# ### Insights 6:calculate the gross income with respect to product line

# In[59]:


Products=c.groupby(['Product line'])['gross income'].sum().reset_index()
Products


# In[60]:


sns.barplot(x='Product line',y='gross income',data=Products);
plt.xticks(rotation=90);


# ### Insights 7: Availability of product

# In[61]:


c['Product line'].value_counts(normalize=True)*100


# In[62]:


c_index=c['Product line'].value_counts().index
c_index


# In[63]:


c_values=c['Product line'].value_counts().values
c_values


# In[64]:


plt.pie(c_values,labels=c_index,autopct='%.2f%%')
plt.show()


# In[ ]:





# In[65]:


df.head(1)


# In[66]:


x=df['Product line'].value_counts().reset_index()
x


# In[67]:


p=x['Product line']
p


# In[68]:


q=x['index']
q


# In[69]:


plt.pie(x['Product line'],labels=x['index'],autopct='%.2f%%')
plt.show()


# In[ ]:





# In[70]:


df.head(1)


# In[71]:


df['Time']=pd.to_datetime(df['Time'])
df['Hour']=df['Time'].dt.hour


# In[72]:


df.info()


# In[73]:


df.head(1)


# In[74]:


plt.figure(figsize=(12,8))
sns.lineplot(x='Hour',y='Quantity',data=df,ci=None)
plt.title('Product sales per hour', fontsize=20)
plt.xlabel('Time of the day', fontsize=15)
plt.xticks(df['Hour'].unique())
# plt.yticks(df['Quantity'].unique())
plt.ylabel('Quantity', fontsize=15)


# INSIGHTS: We can see that the sales is highest at 2pm. Good volume of sales is recorded around 5pm and 7pm. The sales is recorded to be the lowest around 10pm, 3pm and 4pm.

# In[75]:


plt.figure(figsize=(12,8))
sns.lineplot(x='Hour',y='Quantity',data=df, hue='Product line',ci=None)
plt.title('Product sales per hour', fontsize=20)
plt.xlabel('Time of the day', fontsize=15)
plt.ylabel('Quantity', fontsize=15)


# Health and Beauty products has no specific time of purchase Electronic sales are seen around 7 pm which is the end of daily work, when family can enjoy such shopping. Home and lifestyle is recorded around 5 pm and 7 pm which can be an ideal time for homemakers to make such purchases. Food and beverages are seen to be purchased more at 11 am which is an ideal time to purchase daily or weekly food items. Fashion accessories are seen to be purchased at 4 pm which can be an ideal time not only for adults but also for teenagers.

# In[76]:


df


# In[ ]:




