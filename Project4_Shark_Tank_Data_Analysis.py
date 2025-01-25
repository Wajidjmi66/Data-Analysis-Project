#!/usr/bin/env python
# coding: utf-8

# # Shark Tank India
# ---

# ### About
# Shark Tank India is an Indian Hindi-language business reality television series that airs on Sony Entertainment Television. The show is the Indian franchise of the American show Shark Tank. It shows entrepreneurs making business presentations to a panel of investors or sharks, who decide whether to invest in their company. This data is about the  first season of Shark Tank India premiered on 20 December 2021, and concluded on 4 February 2022

# ## Importing Required Modules 
# 1. importing numpy for mathematical operation on arrays and dataframe.
# 2. importing pandas for reading data and data manipualtion.
# 3. importing matplotlib and seaborn to show the insights and  visualization from the dataset.
# 3. importing warnings for Warning messages that are typically issued in dataframe where it is useful to alert the user of some condition in a program, where that condition (normally) doesn t warrant raising an exception and terminating the program.

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")


# In[2]:


sns.set(style = 'darkgrid')


# In[3]:


pd.set_option('display.max_columns',None)


# ## Reading Dataset and Checking the NaN Values , Data Types , and Statistical Analysis
# 
# 1. Since data is in form of excel file we have to use pandas read_excel to load the data
# 2. After loading it is important to check the complete information of data as it can indication many of the hidden infomation such as null values in a column or a row
# 3. Check whether any null values are there or not. if it is present then following can be done,
#     1. Filling NaN values with mean, median and mode using fillna() method
# 4. Describe data --> which can give statistical analysis

# In[4]:


df=pd.read_csv("Shark Tank India Dataset.csv")


# In[5]:


df.head(3)


# In[6]:


# No. of succesfull deals & unsuccefull
# Most Deal in a epsiode
# Most Expensive dealing epsiode


# In[7]:


(75/16)*100


# In[8]:


df.shape


# In[9]:


df.info()


# In[10]:


df.isnull().sum()


# In[11]:


df.shape


# In[12]:


df.describe()


# # Exploratory Data Analysis (EDA)

# ## How many deals done in the whole season

# In[13]:


done=df[df['deal']==1].count()[0]
print('Succesfull deals....',done)
not_done=df[df['deal']==0].count()[0]
print('Rejected deals....',not_done)


# In[14]:


deal=df['deal'].value_counts().values[0]
no_deal=df['deal'].value_counts().values[1]


# In[15]:


df['deal'].value_counts().index


# In[16]:


df['deal'].value_counts(normalize=True)


# In[17]:


df['deal'].value_counts()


# In[18]:


v=df['deal'].value_counts().values
i=df['deal'].value_counts().index


# In[19]:


plt.pie(v,labels=i,autopct='%.2f%%');


# In[20]:


df['deal'].value_counts().plot(autopct='%.2f%%',kind='pie');


# ### Deals percentages

# ##  Most Dealing Episode

# In[21]:


best_episodes=df.groupby(['episode_number'])['deal'].sum().sort_values(ascending=False).reset_index()
best_episodes


# In[22]:


sns.set(style='darkgrid')


# In[23]:


df['episode_number'].value_counts()


# In[24]:


sns.catplot(x = 'deal', y = 'episode_number',kind='swarm',hue='deal', data = df)


# ## Most Expensive dealing Episodes

# In[25]:


A=df.groupby(df['episode_number'])['deal_amount'].sum().sort_values(ascending=False).reset_index()#.head(10)
A


# In[26]:


plt.figure(figsize=(10,6),dpi=200)
plt.bar(A['episode_number'],A['deal_amount'])
plt.xticks(A['episode_number'],fontsize=8)
plt.show()


# ##  All Sharks in

# In[27]:


df[df['total_sharks_invested']==5]


# In[28]:


df['total_sharks_invested'].value_counts()


# In[29]:


plt.figure(figsize=(10,6))
plt.title('Maximum Sharks in')
plt.bar(df['episode_number'],df['total_sharks_invested'])
plt.xticks(df['episode_number'].unique(),rotation=30);


# In[30]:


df[df['total_sharks_invested']==5]


# In[31]:


df.columns


# ## No Bargain Deal

# In[32]:


df[(df['pitcher_ask_amount']==df['deal_amount']) & (df['ask_equity']==df['deal_equity'])]


# ## No of Sharks invested with respect to Business

# In[33]:


df['total_sharks_invested'].value_counts()


# In[34]:


plt.figure(figsize =(20, 6))
sns.countplot(x=df['total_sharks_invested'])
plt.title('Number of Sharks invested', fontsize = 15)
plt.show()


# In[35]:


df.head(1)


# ### Created a function that show the Equity and Amount per shark

# In[36]:


def sharks(data):
    list= ['anupam_deal','aman_deal','namita_deal','vineeta_deal','peyush_deal','ghazal_deal','ashneer_deal']
    for i in list:
        deal = data[['amount_per_shark','equity_per_shark']][data[i]==1]
#         print("{} deals with {}".format(len(deal),i[:-5]))
        print('\n',len(deal),'deals with',i[:-5])
        print(deal)
    


# In[37]:


a=df[(df['ashneer_deal']==1) & (df['anupam_deal']==1)]
len(a[['amount_per_shark','equity_per_shark']])


# In[38]:


a[['amount_per_shark','equity_per_shark']]


# In[39]:


df[(df['ashneer_deal']==1) & (df['anupam_deal']==1)][['amount_per_shark','equity_per_shark']]


# In[40]:


len(df[(df['ashneer_deal']==1) & (df['aman_deal']==1)][['amount_per_shark','equity_per_shark']])


# In[41]:


ash_grover = df[df['ashneer_deal']==1]
ash_grover


# In[42]:


ash_grover.shape


# In[43]:


ash_grover[['amount_per_shark','equity_per_shark']][ash_grover['anupam_deal']==1]


# In[44]:


ash_grover[['amount_per_shark','equity_per_shark']][ash_grover['aman_deal']==1]


# # Ashneer Deals

# In[45]:


sharks(ash_grover)


# In[46]:


df


# In[47]:


amt=ash_grover['amount_per_shark'].sum()
print("Total amount invested on shark tank by Ashneer",amt,"lakhs")


# In[48]:


eqt=ash_grover['equity_per_shark'].sum()
print("Total equity buy on shark tank by Ashneer",eqt,'%')


# In[49]:


ash_grover[ash_grover['equity_per_shark']==ash_grover['equity_per_shark'].max()]


# In[50]:


eqt = df.groupby('ashneer_deal')['equity_per_shark'].sum()[1]
amt = df.groupby('ashneer_deal')['amount_per_shark'].sum()[1]
print("Total equity buy on shark tank by Ashneer",eqt,'%')
print("Total amount invested on shark tank by Ashneer",amt,"lakhs")


# In[51]:


ash_grover['amount_per_shark'].sum()


# In[52]:


ash_grover['amount_per_shark'].max()


# In[53]:


ash_grover[ash_grover['amount_per_shark']==70.0]


# In[54]:


ash_grover.sort_values(by='amount_per_shark',ascending=False).head(1)


# In[55]:


ash_grover['amount_per_shark'].max()


# In[56]:


ash_grover[ash_grover['amount_per_shark']==ash_grover['amount_per_shark'].max()]


# In[57]:


ash_grover[ash_grover['equity_per_shark']==ash_grover['equity_per_shark'].max()]


# # Anupam Deals

# In[58]:


anupam = df[df['anupam_deal']==1]
anupam


# In[59]:


sharks(anupam)


# In[60]:


eqt = df.groupby('anupam_deal')['equity_per_shark'].sum()[1]
amt = df.groupby('anupam_deal')['amount_per_shark'].sum()[1]
print("Total equity buy on shark tank by Anupam",eqt,'%')
print("Total amount invested on shark tank by Anupam",amt,"lakhs")


# In[61]:


anupam['amount_per_shark'].sum()


# In[62]:


anupam['equity_per_shark'].sum()


# In[63]:


anupam[anupam['amount_per_shark']==anupam['amount_per_shark'].max()]


# In[64]:


anupam[anupam['equity_per_shark']==anupam['equity_per_shark'].max()]


# # Aman Deals

# In[65]:


aman = df[df['aman_deal']==1]
aman


# In[66]:


sharks(aman)


# In[67]:


eqt = df.groupby('aman_deal')['equity_per_shark'].sum()[1]
amt = df.groupby('aman_deal')['amount_per_shark'].sum()[1]
print("Total equity buy on shark tank by Aman",eqt,'%')
print("Total amount invested on shark tank by Aman",amt,"lakhs")


# In[68]:


aman['amount_per_shark'].sum()


# In[69]:


aman['equity_per_shark'].sum()


# In[70]:


aman[aman['amount_per_shark']==aman['amount_per_shark'].max()]


# In[71]:


aman[aman['deal_equity']==aman['deal_equity'].max()]


# # Namita Deals

# In[72]:


namita = df[df['namita_deal']==1]
namita


# In[73]:


sharks(namita)


# In[74]:


eqt = df.groupby('namita_deal')['equity_per_shark'].sum()[1]
amt = df.groupby('namita_deal')['amount_per_shark'].sum()[1]
print("Total equity buy on shark tank by namita",eqt,'%')
print("Total amount invested on shark tank by namita",amt,"lakhs")


# In[75]:


namita[namita['amount_per_shark']==namita['amount_per_shark'].max()]


# In[76]:


namita[namita['equity_per_shark']==namita['equity_per_shark'].max()]


# # Vineeta Deals

# In[77]:


vineeta = df[df['vineeta_deal']==1]
vineeta


# In[78]:


vineeta['amount_per_shark'].sum()


# In[79]:


vineeta['equity_per_shark'].sum()


# In[80]:


sharks(vineeta)


# In[81]:


eqt = df.groupby('vineeta_deal')['equity_per_shark'].sum()[1]
amt = df.groupby('vineeta_deal')['amount_per_shark'].sum()[1]
print("Total equity buy on shark tank by vineeta",eqt,'%')
print("Total amount invested on shark tank by vineeta",amt,"lakhs")


# In[82]:


vineeta[vineeta['amount_per_shark']==vineeta['amount_per_shark'].max()]


# In[83]:


vineeta[vineeta['deal_equity']==vineeta['deal_equity'].max()]


# # Peyush Deals

# In[84]:


peyush= df[df['peyush_deal']==1]
peyush


# In[85]:


peyush['amount_per_shark'].sum()


# In[86]:


peyush['equity_per_shark'].sum()


# In[87]:


sharks(peyush)


# In[88]:


eqt = df.groupby('peyush_deal')['equity_per_shark'].sum()[1]
amt = df.groupby('peyush_deal')['amount_per_shark'].sum()[1]
print("Total equity buy on shark tank by peyush",eqt,'%')
print("Total amount invested on shark tank by peyush",amt,"lakhs")


# In[89]:


peyush[peyush['amount_per_shark']==peyush['amount_per_shark'].max()]


# In[90]:


peyush[peyush['deal_equity']==peyush['deal_equity'].max()]


# In[91]:


peyush.sort_values(by='equity_per_shark',ascending=False)


# # Ghazal Deals

# In[92]:


ghazal=df[df['ghazal_deal']==1]
ghazal


# In[93]:


ghazal['amount_per_shark'].sum()


# In[94]:


ghazal['equity_per_shark'].sum()


# In[95]:


sharks(ghazal)


# In[96]:


eqt = df.groupby('ghazal_deal')['equity_per_shark'].sum()[1]
amt = df.groupby('ghazal_deal')['amount_per_shark'].sum()[1]
print("Total equity buy on shark tank by ghazal",eqt,'%')
print("Total amount invested on shark tank by ghazal",amt,"lakhs")


# In[97]:


ghazal[ghazal['amount_per_shark']==ghazal['amount_per_shark'].max()]


# In[98]:


ghazal[ghazal['deal_equity']==ghazal['deal_equity'].max()]


# In[99]:


df.head(5)


# ## Number of Sharks Teamedup

# In[100]:


w=df[df['total_sharks_invested']==1]
w


# In[101]:


len(w)


# In[102]:


# Part-1
q=df[df['total_sharks_invested']>1]

q['total_sharks_invested'].value_counts()


# In[103]:


# Part-2
teamup=df[df['total_sharks_invested']>1]

plt.figure(figsize=(7,7))
plt.hist(teamup.total_sharks_invested)
plt.yticks(q['total_sharks_invested'].value_counts().values)
plt.xticks(q['total_sharks_invested'].value_counts().index)
plt.title('visualization of number of Sharks teamedup')
plt.xlabel('Number of Sharks')
plt.ylabel('Number of Investments');


# In[104]:


# part-4
plt.figure(dpi=200)
plt.scatter(teamup['brand_name'],teamup['total_sharks_invested'],s=9);
plt.yticks(q['total_sharks_invested'])
plt.xticks(rotation=90,fontsize=6)

plt.show()


# In[105]:


df.groupby(['ashneer_deal'])['amount_per_shark'].sum()


# In[106]:


df.episode_number


# ##  Total Amount invested by Sharks in Different Companies

# In[107]:


t=ash_grover['amount_per_shark'].sum()
t2=aman['amount_per_shark'].sum()
print(t)
print(t2)


# In[108]:


a=df[df['ashneer_deal']==1]
aa=list(a['amount_per_shark'])
aa
t=0

for i in aa:
    t+=i
    

b=df[df['anupam_deal']==1]
ba=list(b.amount_per_shark)
u=0
for i in ba:
    u+=i

c=df[df['aman_deal']==1]
ca=list(c.amount_per_shark)
v=0
for i in ca:
    v+=i

d=df[df['namita_deal']==1]
da=list(d.amount_per_shark)
w=0
for i in da:
    w+=i
    
e=df[df['vineeta_deal']==1]
ea=list(e.amount_per_shark)
x=0
for i in ea:
    x+=i
    
f=df[df['peyush_deal']==1]
fa=list(f.amount_per_shark)
y=0
for i in fa:
    y+=i
    
g=df[df['ghazal_deal']==1]
ga=list(g.amount_per_shark)
z=0
for i in ga:
    z+=i


# In[109]:


t=ash_grover['amount_per_shark'].sum()


# In[110]:


t


# In[111]:


peyush


# In[112]:


l1=['Asheer','anupam','aman','namita','vineeta','peyush','ghazal']
l2=[t,u,v,w,x,y,z]
plt.bar(l1,l2);


# In[113]:


# L=[1,2,3,4,5,67,7,8,89,9]
# fo


# In[114]:


print('total amount invested by ashneer',t)


# In[115]:


# ash=df[df['ashneer_deal']==1]
# ash['amount_per_shark'].sum()


# In[ ]:





# In[116]:


# print(t,u,v,w,x,y,z)
# L=[494.33333333, 533.83360253, 887.5000166929999, 648.333602533, 328.3333333300001, 719.666919163, 130.0002525]
# print(sum(L))


# In[117]:


# (494.33333333/3742.0010600789997)*100


# In[ ]:





# ## Total equity owned by sharks in diffrent Companies

# In[118]:


h=df[df['ashneer_deal']==1]
he=list(h.equity_per_shark)
a=0
for i in he:
    a+=i

i=df[df['anupam_deal']==1]
ie=list(i.equity_per_shark)
b=0
for y in ie:
    b+=y
    
j=df[df['aman_deal']==1]
je=list(j.equity_per_shark)
c=0
for i in je:
    c+=i
    
k=df[df['namita_deal']==1]
ke=list(k.equity_per_shark)
d=0
for i in ke:
    d+=i
    
l=df[df['vineeta_deal']==1]
le=list(l.equity_per_shark)
e=0
for i in le:
    e+=i
    
m=df[df['peyush_deal']==1]
me=list(m.equity_per_shark)
f=0
for i in me:
    f+=i
    
n=df[df['ghazal_deal']==1]
ne=list(n.equity_per_shark)
g=0
for i in ne:
    g+=i


# In[119]:


o=df[df['peyush_deal']==1]
o['equity_per_shark'].sum()


# In[120]:


o=df[df['peyush_deal']==1]
o['equity_per_shark'].sum()


# In[121]:


df.head(10)


# In[122]:


peyush.sort_values(by='equity_per_shark',ascending=False)


# In[123]:


l1=['Asheer','anupam','aman','namita','vineeta','peyush','ghazal']
l2=[a,b,c,d,e,f,g]
plt.bar(l1,l2);


# In[124]:


xyz=df[df['ashneer_deal']==1]
xyz['equity_per_shark'].sum()


# In[125]:


df['anupam_deal'].sum()


# In[126]:


df.head(2)


# ##  which Shark invested in most companies

# In[127]:


df['anupam_deal'].sum()


# In[128]:


D=[]
list = ['anupam_deal','aman_deal','namita_deal','vineeta_deal','peyush_deal','ghazal_deal','ashneer_deal']
for i in list:
    deal = df[i].sum()
    D.append(deal)
    print(i,"deals with",deal,"companies" )


# In[129]:


plt.bar(list,D)
plt.xticks(rotation=90);


# In[130]:


len(df[df['anupam_deal']==1])


# ## Insights 8: Which Shark present at the time of Company

# In[131]:


df.head(1)


# In[132]:


p=[]
list = ['anupam_present','aman_present','namita_present','vineeta_present','peyush_present','ghazal_present','ashneer_present']
for i in list:
    pres = df[i].sum()
    p.append(pres)
    print(i,"present in front of",pres,"companies" )


# In[133]:


plt.bar(list,p)
plt.xticks(rotation=90);


# In[134]:


ashneer=(df['ashneer_present'])
anupam=(df['anupam_present'])
aman=(df['aman_present'])
namita=(df['namita_present'])
vineeta=(df['vineeta_present'])
peyush=(df['peyush_present'])
ghazal=(df['ghazal_present'])


xx=pd.DataFrame({'Sharks':['ASHNEER','ANUPAM','AMAN','NAMITA','VINEETA','PEYUSH','GHAZAL'],
              'Number_of_appearance':[sum(ashneer),sum(anupam),sum(aman),sum(namita),sum(vineeta),sum(peyush),sum(ghazal)]})


# In[135]:


sum(ashneer)


# In[136]:


xx


# In[137]:


plt.figure(figsize=(7,7))

sns.barplot(x='Sharks',y='Number_of_appearance',data=xx);


# In[138]:


df


# In[ ]:





# In[ ]:





# In[ ]:




