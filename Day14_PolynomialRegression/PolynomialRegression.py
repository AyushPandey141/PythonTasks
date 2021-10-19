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


#Reading the csv file
df=pd.read_csv('case_time_series.csv')


# In[4]:


df.head()


# In[ ]:





# In[5]:


#Checking whether NaN values are present or not
df.isna().sum()


# In[6]:


#Daily Confirmed and Daily Recovered Graph
def graph(x,y):
    plt.scatter(x,y,color='red')
    poly=np.poly1d(np.polyfit(x,y,4))
    line=np.linspace(1,10,100)
    plt.plot(line,poly(line),color='green')
    plt.show()
a=df['Daily Confirmed']
s=df['Daily Recovered']
graph(a,s)


# In[7]:


#Checking for a linear regression between the Daily Confirmed and Daily Recovered
def linear(x,y):
    x_mean=np.mean(x)
    y_mean=np.mean(y)
    x_std=np.std(x)
    x_squared=[]
    x_diff=[]
    y_diff=[]
    for i in range(len(x)):
        x_diff.append(x[i]-x_mean)
        x_squared.append(x_diff[i]**2)
    for i in range(len(x)):
        y_diff.append(y[i]-y_mean)
    see=[]
    for i in range(len(x)):
        see.append(x_diff[i]*y_diff[i])
    m=sum(see)/sum(x_squared)
    c=y_mean-m*x_mean
    return(m,c)
def show(x,y,m,c):
    print(m,c)
    plt.scatter(x,y,color="red")
    predicted=[]
    for i in range(0,len(x)):
        predicted.append(m*x[i]+c)
    plt.plot(x,predicted,color="green")
    plt.xlabel("Daily Confirmed")
    plt.ylabel("Daily Recovered")
    y_predicted=np.array(predicted)
    plt.show()
x=np.array(list(df['Daily Confirmed']))
y=np.array(list(df['Daily Recovered']))
m,c=linear(x,y)
predicted=show(x,y,m,c)


# In[8]:


from sklearn.metrics import r2_score


# In[9]:


#R2 score between Daily Confirmed and Daily Recovered
def r_square(a,s):
    poly=np.poly1d(np.polyfit(a,s,4))
    return(r2_score(s,poly(a)))
print(r_square(a,s))


# In[10]:


#Daily Confirmed and Daily Deceased Graph
def graph(x,y):
    plt.scatter(x,y)
    poly=np.poly1d(np.polyfit(x,y,4))
    line=np.linspace(1,10,100)
    plt.plot(line,poly(line))
    plt.show()
a=df['Daily Confirmed']
s=df['Daily Deceased']
graph(a,s)


# In[11]:


#R2 score between Daily Confirmed and Daily Deceased
def r_square(a,s):
    poly=np.poly1d(np.polyfit(a,s,4))
    return(r2_score(s,poly(a)))
print(r_square(a,s))


# In[12]:


#Total Confirmed and Total Recovered Graph
def graph(x,y):
    plt.scatter(x,y)
    poly=np.poly1d(np.polyfit(x,y,4))
    line=np.linspace(1,10,100)
    plt.plot(line,poly(line))
    plt.show()
a=df['Total Confirmed']
s=df['Total Recovered']
graph(a,s)


# In[13]:


#R2 score between Total Confirmed and Total Recovered
def r_square(a,s):
    poly=np.poly1d(np.polyfit(a,s,4))
    return(r2_score(s,poly(a)))
print(r_square(a,s))


# In[14]:


#Drawing a linear regression between Total Confirmed and Total Recovered
def linear(x,y):
    x_mean=np.mean(x)
    y_mean=np.mean(y)
    x_std=np.std(x)
    x_squared=[]
    x_diff=[]
    y_diff=[]
    for i in range(len(x)):
        x_diff.append(x[i]-x_mean)
        x_squared.append(x_diff[i]**2)
    for i in range(len(x)):
        y_diff.append(y[i]-y_mean)
    see=[]
    for i in range(len(x)):
        see.append(x_diff[i]*y_diff[i])
    m=sum(see)/sum(x_squared)
    c=y_mean-m*x_mean
    return(m,c)
def show(x,y,m,c):
    print(m,c)
    plt.scatter(x,y,color="red")
    predicted=[]
    for i in range(0,len(x)):
        predicted.append(m*x[i]+c)
    plt.plot(x,predicted,color="green")
    plt.xlabel("Total Confirmed")
    plt.ylabel("Total Recovered")
    y_predicted=np.array(predicted)
    plt.show()
x=np.array(list(df['Total Confirmed']))
y=np.array(list(df['Total Recovered']))
m,c=linear(x,y)
predicted=show(x,y,m,c)


# In[15]:


#Total Confirmed and Total Deceased Graph
def graph(x,y):
    plt.scatter(x,y)
    poly=np.poly1d(np.polyfit(x,y,4))
    line=np.linspace(1,10,100)
    plt.plot(line,poly(line))
    plt.show()
a=df['Total Confirmed']
s=df['Total Deceased']
graph(a,s)


# In[16]:


#R2 score between Total Confirmed and Total Deceased
def r_square(a,s):
    poly=np.poly1d(np.polyfit(a,s,4))
    return(r2_score(s,poly(a)))
print(r_square(a,s))


# In[17]:


#Drawing a linear regression between Total Confirmed and Total Deceased
def linear(x,y):
    x_mean=np.mean(x)
    y_mean=np.mean(y)
    x_std=np.std(x)
    x_squared=[]
    x_diff=[]
    y_diff=[]
    for i in range(len(x)):
        x_diff.append(x[i]-x_mean)
        x_squared.append(x_diff[i]**2)
    for i in range(len(x)):
        y_diff.append(y[i]-y_mean)
    see=[]
    for i in range(len(x)):
        see.append(x_diff[i]*y_diff[i])
    m=sum(see)/sum(x_squared)
    c=y_mean-m*x_mean
    return(m,c)
def show(x,y,m,c):
    print(m,c)
    plt.scatter(x,y,color="red")
    predicted=[]
    for i in range(0,len(x)):
        predicted.append(m*x[i]+c)
    plt.plot(x,predicted,color="green")
    plt.xlabel("Total Confirmed")
    plt.ylabel("Total Deceased")
    y_predicted=np.array(predicted)
    plt.show()
x=np.array(list(df['Total Confirmed']))
y=np.array(list(df['Total Deceased']))
m,c=linear(x,y)
predicted=show(x,y,m,c)


# In[18]:


df.tail()


# In[ ]:





# In[19]:


df.dtypes


# In[20]:


#Extracting the month and year from the Date Column


# In[21]:


import datetime as dt
df['Date_YMD']=pd.to_datetime(df['Date_YMD'])
df['Month']=df['Date_YMD'].dt.month
df['Year']=df['Date_YMD'].dt.year


# In[22]:


df.dtypes


# In[23]:


#Grouping based on the Month and Year
df1=df.groupby(['Month','Year'],as_index=False).agg({'Daily Confirmed':'sum','Total Confirmed':'sum','Daily Recovered':'sum','Total Recovered':'sum','Daily Deceased':'sum','Total Deceased':'sum'})


# In[24]:


df1.head()


# In[25]:


plt.scatter(df['Date_YMD'],df['Total Confirmed'])
plt.xticks(rotation=90)
plt.show()


# In[26]:


#Total Confirmed and Month Graph
def graph(x,y):
    plt.scatter(x,y,color='red')
    poly=np.poly1d(np.polyfit(x,y,4))
    line=np.linspace(1,10,100)
    plt.plot(line,poly(line),color='green')
    plt.show()
a=df1['Month']
s=df1['Total Confirmed']
graph(a,s)


# In[27]:


#Prediction of Total Confirmed in the Month of October
def predict(a,s,value):
    poly=np.poly1d(np.polyfit(a,s,4))
    return(poly(value))
print(predict(a,s,10))


# In[ ]:





# In[28]:


#Total Deceased and Month Graph
def graph(x,y):
    plt.scatter(x,y,color='red')
    poly=np.poly1d(np.polyfit(x,y,4))
    line=np.linspace(1,10,100)
    plt.plot(line,poly(line),color='green')
    plt.show()
a=df1['Month']
s=df1['Total Deceased']
graph(a,s)


# In[29]:


def r_square(a,s):
    poly=np.poly1d(np.polyfit(a,s,4))
    return(r2_score(s,poly(a)))
print(r_square(a,s))


# In[30]:


#Prediction of Total Deceased in the Month of October
def predict(a,s,value):
    poly=np.poly1d(np.polyfit(a,s,4))
    return(poly(value))
print(predict(a,s,10))


# In[ ]:





# In[31]:


#Total Recovered and Month Graph
def graph(x,y):
    plt.scatter(x,y,color='red')
    poly=np.poly1d(np.polyfit(x,y,4))
    line=np.linspace(1,10,100)
    plt.plot(line,poly(line),color='green')
    plt.show()
a=df1['Month']
s=df1['Total Recovered']
graph(a,s)


# In[32]:


def r_square(a,s):
    poly=np.poly1d(np.polyfit(a,s,4))
    return(r2_score(s,poly(a)))
print(r_square(a,s))


# In[33]:


#Prediction of Total Recovered in the Month of October
def predict(a,s,value):
    poly=np.poly1d(np.polyfit(a,s,4))
    return(poly(value))
print(predict(a,s,10))


# In[ ]:





# In[ ]:




