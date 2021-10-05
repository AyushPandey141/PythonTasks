#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Task:Task to compare the rate of people vaccinated in United States and India 
#Program By:Ayush Pandey
#Email Id:1805290@kiit.ac.in
#DATE:4-Oct-2021
#Python Version:3.7
#CAVEATS:None
#LICENSE:None


# In[2]:


import pandas as pd 
import numpy as np 
from statistics import mode 

# data extraction 
df = pd.read_csv('country_vaccinations.csv')
df.head()
# vaccine combinations being used 


# In[3]:


from collections import Counter 

country_list = df['country'].unique()

vaccine_ava = df['vaccines'].unique()
print(country_list)
print("")
print(vaccine_ava)


# In[4]:


vaccine_used = []
for i in country_list:
    vaccine_used.append(df[df['country']==i]['vaccines'].mode(0))
vaccine_used = pd.Series(vaccine_used)
print(vaccine_used)


# In[5]:


vaccine_mode = []
for i in range(0, 102):
    vaccine_mode.append(vaccine_used[i][0])
    
#1st method
"""words_to_count = (word for word in vaccine_mode if word[:1].isupper())
c = Counter(words_to_count)
print(c)"""
#Till here

c={}
#print(vaccine_mode)

#2nd method
for i in vaccine_mode:
    if(i not in c):
        c[i]=1
    else:
        c[i]+=1
print(c)
c=Counter(c)
print(len(c))
#Till here

count = []

names_vaccine = [] 
for i in range(0,19):
    count.append(c.most_common()[i][1])
    names_vaccine.append(c.most_common()[i][0])
#print("Most widely used vaccine: ", names_vaccine[0])
print("Most widely used vaccine: ", mode(vaccine_mode))

print("vaccines used in India:  ", df[df['country']=='India']['vaccines'].mode(0)[0])


# In[6]:


#For each country checking the vaccine used frequently
def get(x):
    ans=df[df['country']==x]['vaccines'].mode(0)[0]
    if(x not in see):
        see[x]=ans


# In[7]:


ans=0
see={}
q=df['country'].apply(get)


# In[8]:


print(see)
print(len(see))


# In[9]:


#A logic to het sum of any column with respect to the country
a=df[df['country']=='Albania']['people_vaccinated'].sum()
print(a)


# In[10]:


#By above logic checking for countries which are unvaccinated
# unvaccinated countries 

#Sir Logic
people_vaccinated = []

for i in country_list:
    people_vaccinated.append(df[df['country']==i]['people_vaccinated'].sum(0))

index_country = []

countries_unvaccinated = [] 

for i in range(1,102):
    if(people_vaccinated[i]==0):
        index_country.append(i)

for i in index_country:
    countries_unvaccinated.append(country_list[i])

print("countries unvaccinated # ", countries_unvaccinated)



#My attempt
see=[]
for i in country_list:
    see.append(df[df['country']==i]['people_vaccinated'].sum())
#print(see)
ans=[]
for i in range(len(see)):
    if(see[i]==0):
        ans.append(country_list[i])
print(ans)
        


# In[ ]:





# In[ ]:





# In[11]:


a=df[df['country']=='United States']['vaccines'].count()
a


# In[12]:


df.dtypes


# In[13]:


#Now converting type of date from object to datetime
import datetime
df['date']=pd.to_datetime(df['date'])


# In[14]:


df.dtypes


# In[15]:


df.head()


# In[16]:


#Task

#For storing all data Where Country is 'India'
first_vaccines=df[df['country']=='India']
#For storing all data Where Country is 'United States'
second_vaccines=df[df['country']=='United States']
total_India=sum(first_vaccines['people_vaccinated'])
total_US=sum(second_vaccines['people_vaccinated'])
print("In India People Vaccinated are:",total_India)
print("In United States People Vaccinated are:",total_US)
print("Rate of United States with Respect to India is:")
ans=((total_US-total_India)/total_US)*100
print(ans)


# In[17]:


#After seeing the csv file I found that the date of India And US are different
#So to get proper Rate of vaccination of US and INDIA it is importtant to see for the dates which are similar
#I found that the date from "2021-01-15" to "2021-02-22" are present in both
#So I will be using the people vaccinated between these dates to get the more exact result 


# In[18]:


second_vaccines.head()


# In[19]:


start="2021-01-15"
end="2021-02-22"
UnitedStates=second_vaccines[(second_vaccines['date']>=start) & (second_vaccines['date']<=end)]


# In[20]:


UnitedStates.head()


# In[21]:


total_vaccines_US=UnitedStates['people_vaccinated'].sum()
print(total_vaccines_US)


# In[22]:


first_vaccines.head()


# In[23]:


total_vaccines_India=first_vaccines['people_vaccinated'].sum()
total_vaccines_India


# In[24]:


print("Rate of United States with Respect to India is:")
ans=((total_vaccines_US-total_vaccines_India)/total_vaccines_US)*100
print(ans)


# In[25]:


#We can also calculate the Rate of vaccinations for Month of January and February
df['Month']=df['date'].dt.month


# In[26]:


df1=df.groupby(['country','Month']).people_vaccinated.sum()


# In[27]:


people_vaccinated_India=df1['India']
people_vaccinated_US=df1['United States']
print("For India:")
print(people_vaccinated_India)
print("For United States:")
print(people_vaccinated_US)


# In[28]:


#For the Month Of January Rate of Vaccines In US with respect to India Was
ans=((people_vaccinated_US[1]-people_vaccinated_India[1])/people_vaccinated_US[1])*100
print(ans)


# In[29]:


#For the Month Of February Rate of Vaccines In US with respect to India Was
ans=((people_vaccinated_US[2]-people_vaccinated_India[2])/people_vaccinated_US[2])*100
print(ans)


# In[ ]:




