#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Task:Mutiple Regression on data for India and Pakistan
#Program By:Ayush Pandey
#Email Id:1805290@kiit.ac.in
#DATE:19-Oct-2021
#Python Version:3.7
#CAVEATS:None
#LICENSE:None


# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[3]:


#For reading the csv file
df=pd.read_csv('data_2.csv')


# In[4]:


df.head()


# In[5]:


#Comparing the Death of India and Pakistan based on Unsafe water source,Unsafe sanitation,No access to handwashing facility
df1=df.groupby(['Entity'],as_index=False).agg({'Unsafe water source':'sum','Unsafe sanitation':'sum','No access to handwashing facility':'sum'})


# In[6]:


#Storing all the data's where Entity is India and Pakistan
India=df1[df1['Entity']=='India']
Pakistan=df1[df1['Entity']=='Pakistan']


# In[7]:


x=['Unsafe water source','Unsafe sanitation','No access to handwashing facility']
y=[India['Unsafe water source'].item(),India['Unsafe sanitation'].item(),India['No access to handwashing facility'].item()]
y1=[Pakistan['Unsafe water source'].item(),Pakistan['Unsafe sanitation'].item(),Pakistan['No access to handwashing facility'].item()]
X_axis = np.arange(len(x))
plt.bar(X_axis - 0.2,y,0.4,label="India")
plt.bar(X_axis + 0.2,y1,0.4,color="red",label="Palkistan")
plt.xticks(rotation=90)
plt.xlabel(['Unsafe water source','Unsafe sanitation','No access to handwashing facility'])
plt.ylabel("No. of Death")
plt.legend()
plt.show()


# In[8]:


India=df[df['Entity']=='India']
Pakistan=df[df['Entity']=='Pakistan']


# In[9]:


from sklearn.linear_model import LinearRegression


# In[10]:


#For India Doing Mutiple regression
#Independent
x=India[['Unsafe water source','Unsafe sanitation']]
#Depenent
y=India['No access to handwashing facility']
model=LinearRegression()
model.fit(x,y)
print(model.score(x,y)*100)
print(model.coef_)

#This shows that the Unsafe water souce is the main cause for no access to handwashing facility as the coefficient value is more than 50%.


# In[11]:


#For Pakistan Doing Mutiple regression
#Independent
x=Pakistan[['Unsafe water source','Unsafe sanitation']]
#Depenent
y=Pakistan['No access to handwashing facility']
model=LinearRegression()
model.fit(x,y)
print(model.score(x,y)*100)
print(model.coef_)

#This shows that the Unsafe sanitation souce is the main cause for no access to handwashing facility as the coefficient value is around 40%.


# In[ ]:




