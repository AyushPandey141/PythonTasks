#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Task:Based on the file calculate the performance of the share on day to day basis 
#Program By:Ayush Pandey
#Email Id:1805290@kiit.ac.in
#DATE:6-Oct-2021
#Python Version:3.7
#CAVEATS:None
#LICENSE:None


# In[2]:


import pandas as pd


# In[3]:


#Reading a csv file
df=pd.read_csv('finance_data.csv')
df.head()


# In[4]:


#Finding the standard deciation of all the numerical columns
print(df.std())


# In[5]:


#Finding the mean of all the numerical columns
print(df.mean())


# In[ ]:





# In[6]:


#Finding the skewness of all the numerical columns
print(df.skew())


# In[7]:


#Coefficent of variation
print(df.std()/df.mean()*100)


# In[8]:


#For Open column calculating the Standard deviation,mean and Coefficient of Variation
a=df['Open'].std()
s=df['Open'].mean()
cv=(a/s)*100
print(a,cv)


# In[9]:


#For Close column calculating the Standard deviation,mean and Coefficient of Variation
a=df['Close'].std()
s=df['Close'].mean()
cv1=(a/s)*100
print(a,cv1)


# In[10]:


#Now calculating the difference of Close And Open column
print(((cv1-cv)/cv)*100)


# In[ ]:





# In[11]:


#TASK
#To Find The Good Performance And Bad Performance in the dataset


# In[12]:


df.head(2)


# In[13]:


df.dtypes


# In[14]:


import datetime as dt
df['Date']=pd.to_datetime(df['Date'])
df['Month']=df['Date'].dt.month


# In[15]:


df.head(2)


# In[16]:


#For Calculating the Best Performance date and worst Performance Date from the entire data
#See and see1 are two variable for storing the difference of the Close and Open Column
#If for any date the difference between the Close and the open Column is greater than see,then see will be replaced by than difference
#If for any date the difference between the Close and the open Column is lesser than see1,then see will be replaced by than difference

see=df['Close'][0]-df['Open'][0]
see1=df['Close'][0]-df['Open'][0]
for i in range(len(df)):
    q=df['Close'][i]-df['Open'][i]
    if(q>see):
        see=q
        performance=df['Date'][i]
    if(q<see1):
        see1=q
        performance1=df['Date'][i]
print("Good performance on",performance)
print("Bad performance on",performance1)


# In[17]:


#For Good Performance
check=df[df['Date']=='2021-07-06']
check


# In[18]:


#For Bad Performance
check=df[df['Date']=='2020-10-30']
check


# In[19]:


#For each month
month=[]
for i in df['Month']:
    if(i not in month):
        month.append(i)
print(month)


# In[ ]:





# In[20]:


for_month={}
a=[]
for i in range(0,len(df),1):
    a.append(df['Close'][i]-df['Open'][i])
    


# In[21]:


#Creating a new column which tells the difference between the Close and Open Column
df['Difference']=a


# In[22]:


df.head(3)


# In[23]:


#For Calculating the Best Performance date and worst Performance Date from the entire data for each month
#See and see1 are two variable for storing the difference of the Close and Open Column
#If for any date the difference between the Close and the open Column is greater than see,then see will be replaced by than difference
#If for any date the difference between the Close and the open Column is lesser than see1,then see will be replaced by than difference


see=df['Close'][0]-df['Open'][0]
see1=df['Close'][0]-df['Open'][0]
for i in range(len(df)):
    if(len(month)==0):
        break
    if(df['Month'][i]==month[0]):
        if(df['Difference'][i]>see):
            see=df['Difference'][i]
            ans=df['Date'][i]
        if(df['Difference'][i]<see1):
            see1=df['Difference'][i]
            ans1=df['Date'][i]
    j=i+1
    if(j<len(df)):
        if(df['Month'][j]!=month[0]):
            for_month[month[0]]=[ans,ans1]
            see=df['Close'][j]-df['Open'][j]
            see1=df['Close'][j]-df['Open'][j]
            month.pop(0)
print(for_month)


# In[24]:


a=pd.DataFrame(for_month.keys())
s=pd.DataFrame(for_month.values())
df1=pd.concat([a,s],axis=1)


# In[25]:


#Here Maximum indicate best performance date of every month
#Here Minimum indicate bad performance date of every month month
df1.columns=['Month','Best_Day','Worst_Day']


# In[26]:


df1.head()


# In[27]:


#Calculating mean and std of Open And CLose of each month and year
df2=df.groupby([df['Date'].dt.year,df['Month']]).agg({'Open':['mean','std'],'Close':['mean','std']})


# In[28]:


df2


# In[29]:


#Coefficient of Variance of Open
df2['Open_CV']=(df2['Open']['std']/df2['Open']['mean'])*100

#Coefficient of Variance of Close
df2['Close_CV']=(df2['Close']['std']/df2['Close']['mean'])*100

#By how much %cent change of Open_CV and Close_CV
df2['CV_Change']=((df2['Close_CV']-df2['Open_CV'])/df2['Open_CV'])*100
#df2['CV_Differ']=((df2['Close_CV']-df2['Open_CV'])/df2['Close_CV'])*100


# In[30]:


df2


# In[ ]:





# In[31]:


df.head()


# In[32]:


#Now creating two columns Positive and Negative storing the number of days where Difference was positive and negative
maxx=[]
minn=[]
count1=0
count2=0
for i in range(0,len(df)):
    j=i+1
    if(j<len(df)):
        if(df['Month'][i]==df['Month'][j]):
            if(df['Difference'][i]>0):
                count1+=1
            else:
                count2+=1
        else:
            if(df['Difference'][i]>0):
                count1+=1
            else:
                count2+=1
            maxx.append(count1)
            minn.append(count2)
            count1=0
            count2=0
    else:
        if(df['Difference'][i]>0):
            count1+=1
        else:
            count2+=1
        maxx.append(count1)
        minn.append(count2)
        count1=0
        count2=0
print(maxx)   
print(minn)


# In[33]:


df2.head()


# In[34]:


#For storing the total days of the month which had a positive difference and a negative difference
df2['Positive']=maxx
df2['Negative']=minn


# In[35]:


df2


# In[36]:


import seaborn as sns
sns.distplot(df['Open'])
print(df['Open'].skew())


# In[37]:


sns.distplot(df['Close'])
print(df['Close'].skew())


# In[38]:


#Symmetric or not skewed
sns.distplot(df['Difference'])
print(df['Difference'].skew())


# In[39]:


import matplotlib.pyplot as plt
plt.scatter(df['Month'],df['Difference'])
plt.show()


# In[40]:


df2


# In[ ]:





# In[41]:


#Just checking how spread is my standard deviation
sns.distplot(df2['Open']['mean'],color="red")
sns.distplot(df2['Open']['std'],color="green")
plt.show()


# In[42]:


#Just checking how spread is my standard deviation
sns.distplot(df2['Close']['mean'],color="red")
sns.distplot(df2['Close']['std'],color="green")
plt.show()


# In[43]:


#Comparing the graph between Open and Close column w.ith respect to date
plt.plot(df['Date'],df['Open'],color="red",label="Open")
plt.plot(df['Date'],df['Close'],color="green",label="Close")
plt.legend()


# In[44]:


plt.plot(df['Date'],df['Volume'],color="green",label="Open")


# In[45]:


#Creating a new column for storing the Percent change of Close Column with respect to the previous value
df['Per Change']=df['Close'].pct_change()*100
df.head()


# In[46]:


#To drop the first row as in Per Change it is NaN
df.dropna(inplace=True)


# In[ ]:





# In[47]:


#A plot to see the Per Chang column with respect to date
plt.plot(df['Date'],df['Per Change'],color='green')


# In[48]:


df['Per Change'].hist(bins = 50, figsize = (10,5)) 
plt.xlabel("Daily")
plt.ylabel("Frequency")
plt.show()


# In[49]:


df.shape


# In[50]:


#Seeing the trend of the stocks based on the Percent Change of the Close Column
def get(x):
      if x > -0.5 and x <= 0.5:
        return 'Slight or No change'
      elif x > 0.5 and x <= 1:
        return 'Slight Positive'
      elif x > -1 and x <= -0.5:
        return 'Slight Negative'
      elif x > 1 and x <= 3:
        return 'Positive'
      elif x > -3 and x <= -1:
        return 'Negative'
      elif x > 3 and x <= 7:
        return 'Huge Profit'
      elif x > -7 and x <= -3:
        return 'Huge Loss'
      elif x > 7:
        return 'Heavy Profit'
      elif x <= -7:
        return 'Heavy Loss'


# In[51]:


#To store the trend based on the Per Change Column
trend=[]
trend.append(df['Per Change'].apply(get))


# In[52]:


df['Trend']=trend[0]


# In[53]:


df.head()


# In[54]:


#Plotting a graph to see the count of each trend and to give a more better idea
sns.countplot(df['Trend'])
plt.xticks(rotation=90)
plt.show()


# In[55]:


#Inference form the above graph
#The result of no or slight change is the highest follwed by the postive change


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




