#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Program:API TASK 
#Program By:Ayush Pandey
#Email Id:1805290@kiit.ac.in
#DATE:20-Sept-2021
#Python Version:3.7
#CAVEATS:None
#LICENSE:None


# In[2]:


import requests
import json 


# In[3]:


#To get all details where 'name'="Afghan Hound"

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
s=ayush_json()
#Checking whether url is present or not
if(s.check_url(url)):
    see=s.read_url(url)
    flag=0
    for i in see:
        #Checking whether value in 'name' is Afghan Hound
        if(i['name']=="Afghan Hound"):
            flag=1
            print(i)
    if(flag==0):
        print("Name not present")
else:
    print("URL NOT PRESENT")


# In[4]:


#To display breed_group along with image

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
s=ayush_json()
#Checking whether url is present or not
if(s.check_url(url)):
    see=s.read_url(url)
    for i in see:
        #As there were few document where breed_name was not there and there was one document with empty breed_group
        if('breed_group' in i and i['breed_group']!=""):
            print("Breed Group:",i['breed_group'])
            print("Image",i['image'])
        else:
            print("Breed Group:Not Present")
            print("Image",i['image'])
else:
    print("URL NOT PRESENT")


# In[ ]:




