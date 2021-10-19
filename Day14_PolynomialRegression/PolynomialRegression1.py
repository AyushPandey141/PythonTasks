#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Task:1)To draw graph,calculate the r2 score and to predict the daily cases in the month of October
#Program By:Ayush Pandey
#Email Id:1805290@kiit.ac.in
#DATE:18-Oct-2021
#Python Version:3.7
#CAVEATS:None
#LICENSE:None


# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[3]:


df=pd.read_csv('case_time_series.csv')


# In[4]:


df.head()


# In[5]:


df.isna().sum()


# In[6]:


from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score


# In[7]:


#A graph between Daily Confirmed and Daily Recovered Using both Linear and Polynomail Regression
model=LinearRegression()
plt.scatter(df['Daily Confirmed'],df['Daily Recovered'],color="red")
x=np.array(list(df['Daily Confirmed']))
x=x.reshape(-1,1)
model.fit(x,df['Daily Recovered'])
plt.plot(df['Daily Confirmed'],model.predict(x),color="green")


# In[8]:


#R2 score between Daily Confirmed and Daily Recovered
r2_score(df['Daily Recovered'],model.predict(x))


# In[9]:


model1=PolynomialFeatures(degree=4)
x=np.array(list(df['Daily Confirmed']))
x=x.reshape(-1,1)
X=model1.fit_transform(x)


# In[10]:


pd.DataFrame(X)


# In[11]:


plt.scatter(df['Daily Confirmed'],df['Daily Recovered'])
model.fit(X,df['Daily Recovered'])
plt.plot(df['Daily Confirmed'],model.predict(X),color="green")


# In[12]:


#R2 score between Daily Confirmed and Daily Recovered
r2_score(df['Daily Recovered'],model.predict(X))


# In[ ]:





# In[13]:


#A graph between Daily Confirmed and Daily Deceased Using both Linear and Polynomail Regression
model=LinearRegression()
plt.scatter(df['Daily Confirmed'],df['Daily Deceased'],color="red")
x=np.array(list(df['Daily Confirmed']))
x=x.reshape(-1,1)
model.fit(x,df['Daily Deceased'])
plt.plot(df['Daily Confirmed'],model.predict(x),color="green")


# In[14]:


#R2 score between Daily Confirmed and Daily Deceased
r2_score(df['Daily Recovered'],model.predict(x))


# In[15]:


model1=PolynomialFeatures(degree=4)
x=np.array(list(df['Daily Confirmed']))
x=x.reshape(-1,1)
X=model1.fit_transform(x)

plt.scatter(df['Daily Confirmed'],df['Daily Deceased'])
model.fit(X,df['Daily Deceased'])
plt.plot(df['Daily Confirmed'],model.predict(X),color="green")


# In[16]:


#R2 score between Daily Confirmed and Daily Deceased
r2_score(df['Daily Deceased'],model.predict(X))


# In[ ]:





# In[17]:


#A graph between Total Confirmed and Total Recovered Using both Linear and Polynomail Regression
model=LinearRegression()
plt.scatter(df['Total Confirmed'],df['Total Recovered'],color="red")
x=np.array(list(df['Total Confirmed']))
x=x.reshape(-1,1)
model.fit(x,df['Total Recovered'])
plt.plot(df['Total Confirmed'],model.predict(x),color="green")


# In[18]:


#R2 score between Total Confirmed and Total Recovered
r2_score(df['Total Recovered'],model.predict(x))


# In[19]:


model1=PolynomialFeatures(degree=4)
x=np.array(list(df['Total Confirmed']))
x=x.reshape(-1,1)
X=model1.fit_transform(x)

plt.scatter(df['Total Confirmed'],df['Total Recovered'])
model.fit(X,df['Total Recovered'])
plt.plot(df['Total Confirmed'],model.predict(X),color="green")


# In[20]:


#R2 score between Total Confirmed and Total Recovered
r2_score(df['Total Recovered'],model.predict(X))


# In[ ]:





# In[21]:


#A graph between Total Recovered and Total Deceased using both linear and polynomial regression
model=LinearRegression()
x=np.array(list(df['Total Recovered']))
x=x.reshape(-1,1)
model.fit(x,df['Total Deceased'])
plt.scatter(df['Total Recovered'],df['Total Deceased'],color="red")
plt.plot(df['Total Recovered'],model.predict(x),color="green")


# In[22]:


#R2 score between Total Confirmed and Total Deceased
r2_score(df['Total Deceased'],model.predict(x))


# In[23]:


model1=PolynomialFeatures(degree=4)
x=np.array(list(df['Total Recovered']))
x=x.reshape(-1,1)
X=model1.fit_transform(x)

plt.scatter(df['Total Recovered'],df['Total Deceased'])
model.fit(X,df['Total Deceased'])
plt.plot(df['Total Recovered'],model.predict(X),color="green")


# In[24]:


#R2 score between Total Confirmed and Total Deceased
r2_score(df['Total Deceased'],model.predict(X))


# In[ ]:





# In[25]:


df.dtypes


# In[26]:


import datetime as dt
df['Date_YMD']=pd.to_datetime(df['Date_YMD'])
df['Month']=df['Date_YMD'].dt.month
df['Year']=df['Date_YMD'].dt.year


# In[27]:


df.head(2)


# In[28]:


df1=df.groupby(['Month','Year'],as_index=False).agg({'Daily Confirmed':'sum','Total Confirmed':'sum','Daily Recovered':'sum','Total Recovered':'sum','Daily Deceased':'sum','Total Deceased':'sum'})


# In[29]:


plt.scatter(df['Date_YMD'],df['Total Confirmed'])
plt.xticks(rotation=90)
plt.show()


# In[30]:


x=np.array(list(df1['Month']))
x=x.reshape(-1,1)


# In[31]:


#Total Confirmed and Month Graph
model1=PolynomialFeatures(degree=4)
X=model1.fit_transform(x)

model=LinearRegression()
#model.fit(X,df['Daily Confirmed'])

plt.scatter(df1['Month'],df1['Total Confirmed'])
model.fit(X,df1['Total Confirmed'])
plt.plot(df1['Month'],model.predict(X),color="green")


# In[32]:


r2_score(df1['Total Confirmed'],model.predict(X))


# In[33]:


#Prediction of Total Confirmed in the Month of October
ans=model.predict(model1.transform([[10]]))
ans


# In[ ]:





# In[34]:


#Regression between Month and Total Deceased
model1=PolynomialFeatures(degree=4)
X=model1.fit_transform(x)

model=LinearRegression()
plt.scatter(df1['Month'],df1['Total Deceased'])
model.fit(X,df1['Total Deceased'])
plt.plot(df1['Month'],model.predict(X),color="green")


# In[35]:


r2_score(df1['Total Deceased'],model.predict(X))


# In[36]:


#Predicting the Total Deceased in the month of October
ans=model.predict(model1.transform([[10]]))
ans


# In[37]:


#Regression between Month and Total Recovered
model1=PolynomialFeatures(degree=4)
X=model1.fit_transform(x)

model=LinearRegression()
plt.scatter(df1['Month'],df1['Total Recovered'])
model.fit(X,df1['Total Recovered'])
plt.plot(df1['Month'],model.predict(X),color="green")


# In[38]:


r2_score(df1['Total Recovered'],model.predict(X))


# In[39]:


#Predicting the Total Recovered in the month of October
ans=model.predict(model1.transform([[10]]))
ans


# In[ ]:




