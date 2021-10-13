#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Task:To plot graphs Using Matplotlib
#Program By:Ayush Pandey
#Email Id:1805290@kiit.ac.in
#DATE:12-Oct-2021
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


# In[4]:


vaccine_used = []
for i in country_list:
    vaccine_used.append(df[df['country']==i]['vaccines'].mode(0))
vaccine_used = pd.Series(vaccine_used)


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


# In[ ]:





# In[8]:


#A logic to get sum of any column with respect to the country
a=df[df['country']=='Albania']['people_vaccinated'].sum()
print(a)


# In[9]:


#By above logic checking for countries which are unvaccinated
# unvaccinated countries 

#1st Method
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



#2nd Method
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





# In[10]:


a=df[df['country']=='United States']['vaccines'].count()
a


# In[11]:


df.dtypes


# In[12]:


#Now converting type of date from object to datetime
import datetime
df['date']=pd.to_datetime(df['date'])


# In[13]:


df.head(2)


# In[14]:


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


# In[15]:


#After seeing the csv file I found that the date of India And US are different
#So to get proper Rate of vaccination of US and INDIA it is importtant to see for the dates which are similar
#I found that the date from "2021-01-15" to "2021-02-22" are present in both
#So I will be using the people vaccinated between these dates to get the more exact result 


# In[16]:


second_vaccines.head(2)


# In[17]:


start="2021-01-15"
end="2021-02-22"
UnitedStates=second_vaccines[(second_vaccines['date']>=start) & (second_vaccines['date']<=end)]


# In[18]:


UnitedStates.head(2)


# In[19]:


total_vaccines_US=UnitedStates['people_vaccinated'].sum()
print(total_vaccines_US)


# In[20]:


first_vaccines.head(2)


# In[21]:


total_vaccines_India=first_vaccines['people_vaccinated'].sum()
total_vaccines_India


# In[22]:


print("Rate of United States with Respect to India is:")
ans=((total_vaccines_US-total_vaccines_India)/total_vaccines_US)*100
print(ans)


# In[23]:


#We can also calculate the Rate of vaccinations for Month of January and February
df['Month']=df['date'].dt.month


# In[24]:


df1=df.groupby(['country','Month']).people_vaccinated.sum()


# In[25]:


people_vaccinated_India=df1['India']
people_vaccinated_US=df1['United States']
print("For India:")
print(people_vaccinated_India)
print("For United States:")
print(people_vaccinated_US)


# In[26]:


#For the Month Of January Rate of Vaccines In US with respect to India Was
ans=((people_vaccinated_US[1]-people_vaccinated_India[1])/people_vaccinated_US[1])*100
print(ans)


# In[27]:


#For the Month Of February Rate of Vaccines In US with respect to India Was
ans=((people_vaccinated_US[2]-people_vaccinated_India[2])/people_vaccinated_US[2])*100
print(ans)


# In[28]:


df.head(2)


# In[ ]:





# # TASK 
# 1)To plot a graph of Standard Deviation in the month of January And February
# 
# 2)To plot a graph for Fully vaccinated people of India And US
# 
# 3)To plot a graph for Partially vaccinated people of India And US

# In[ ]:





# In[29]:


import matplotlib.pyplot as plt


# In[30]:


x_axis=[]
y_axis=[]
for i in range(0,len(df)):
    if(df['country'][i]=='India'):
        x_axis.append(df['date'][i])
        y_axis.append(df['daily_vaccinations'][i])


# In[31]:


plt.title("Daily Vaccinations Vs Date")
plt.plot(x_axis,y_axis,color="green")
plt.xlabel("Date")
plt.ylabel("Daily Vaccinations")
plt.xticks(rotation=90)
plt.savefig('Daily Vaccinations VS Date.png',format='png',bbox_inches='tight')
plt.show()


# In[32]:


df.head()


# In[33]:


India=df[df['country']=='India']
US=df[df['country']=='United States']


# In[34]:


India.head(2)


# In[35]:


US.head(2)


# In[36]:


#To plot a graph for fully vaccinated people of India And US
plt.title("People Fully Vaccinated In India And Us VS Date")
plt.plot(India['date'],India['people_fully_vaccinated'],color="red",label='India')
plt.plot(US['date'],US['people_fully_vaccinated'],color="green",label='US')
plt.xticks(rotation=90)
plt.legend()
plt.xlabel("Date")
plt.ylabel("People_Count")
plt.savefig('People Fully Vaccinated.png',format='png',bbox_inches='tight')
plt.show()


# In[37]:


#Checking the sum of people vaccinated in India and US
print(sum(US['people_fully_vaccinated']))
print(sum(India['people_fully_vaccinated']))


# In[38]:


#To plot a graph for Partially vaccinated people of India And US
plt.title("       People Partially Vaccinated In India And Us VS Date")
plt.plot(India['date'],India['people_vaccinated'],color="red",label='India')
plt.plot(US['date'],US['people_vaccinated'],color="green",label='US')
plt.xticks(rotation=90)
plt.legend()
plt.xlabel("Date")
plt.ylabel("People_Count")
plt.savefig('People Partially Vaccinated.png',format='png',bbox_inches='tight')
plt.show()


# In[39]:


#Standard Deviation for the month of January And February on the basis of Total vaccinations
df5=df.groupby('Month').agg({'total_vaccinations':'std'})


# In[40]:


y_axis=[]
x_axis=['January','February']
y_axis.append(df5['total_vaccinations'][1])
y_axis.append(df5['total_vaccinations'][2])


# In[41]:


#For All Countries the standard deviation bar plot for the month of January and February
plt.title("Standard Deviation For Jan And Feb")
plt.bar(x_axis,y_axis)
plt.xlabel("Month")
plt.ylabel("Standard Deviation")
plt.savefig('Standard Deviation For All.png',format='png',bbox_inches='tight')
plt.show()


# In[42]:


#For India
df6=India.groupby('Month').agg({'total_vaccinations':'std'})


# In[43]:


y_axis=[]
x_axis=['January','February']
y_axis.append(df6['total_vaccinations'][1])
y_axis.append(df6['total_vaccinations'][2])


# In[44]:


#For India the standard deviation bar plot for the month of January and February
plt.title("Standard Deviation For Jan And Feb(India)")
plt.bar(x_axis,y_axis)
plt.xlabel("Month")
plt.ylabel("Standard Deviation")
plt.savefig('Standard Deviation Of India.png',format='png',bbox_inches='tight')
plt.show()


# In[45]:


#For US
df7=US.groupby('Month').agg({'total_vaccinations':'std'})


# In[46]:


y_axis=[]
x_axis=['January','February']
y_axis.append(df7['total_vaccinations'][1])
y_axis.append(df7['total_vaccinations'][2])


# In[47]:


#For US the standard deviation bar plot for the month of January and February
plt.title("Standard Deviation For Jan And Feb(US)")
plt.bar(x_axis,y_axis)
plt.xlabel("Month")
plt.ylabel("Standard Deviation")
plt.savefig('Standard Deviation of US.png',format='png',bbox_inches='tight')
plt.show()


# In[ ]:




