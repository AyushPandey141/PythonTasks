#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Task:You have been given a API endpoint https://api.thedogapi.com/v1/breeds create a Pandas dataframe from the given endpont
#Program By:Ayush Pandey
#Email Id:1805290@kiit.ac.in
#DATE:1-Oct-2021
#Python Version:3.7
#CAVEATS:None
#LICENSE:None


# In[2]:


#Task
import pandas as pd
import numpy as np
import json
import requests

class ayush_json:
    def check_url(self, url):
        try:
            url = requests.get(url)
            return True
        except:
            return False

    def read_url(self, url):
        url = requests.get(url)
        return url.json()


url = "https://api.thedogapi.com/v1/breeds"
check = []
s = ayush_json()
ans={}
# Checking whether url is present or not
if(s.check_url(url)):
    see = s.read_url(url)
    flag = 0
    for i in see:
        #Storing the data which I am getting from the url in Breed1.json
        with open("Breed1.json", "w") as f:
            check.append(i)
            ans
            json.dump(check, f)
else:
    print("URL NOT PRESENT")

df=pd.json_normalize(check)
#Setting the index as id
df.set_index('id',inplace=True)
#Storing the entire data in a csv file
df.to_csv('PandasTask.csv')


# In[3]:


#Reading the csv file to check whether it worked and how my data will look
df=pd.read_csv('PandasTask.csv')
#Displaying the result
df.head()


# In[4]:


#Shape of my dataframe
df.shape


# In[ ]:




