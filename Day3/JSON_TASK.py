#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Program:JSON TASK 
#Program By:Ayush Pandey
#Email Id:1805290@kiit.ac.in
#DATE:21-Sept-2021
#Python Version:3.7
#CAVEATS:None
#LICENSE:None


# In[2]:


import pymongo


# In[3]:


#You have a JSON file.Write a Python progrom to insert the data present in  the JSON file into your MongoDB collection in form of documents

import json
class Ayush_Mongo:
    connection = pymongo.MongoClient("mongodb://localhost:27017")

    def mongo_connection(self):
        #Checking whether connection is successful or not
        if self.connection:
            return True 
        else:
            return False 
    
    def db_exists(self, db_name):
        if db_name in self.mongodb_list():
            return True
        else:
            return False 
    
    def create_new_collection(self, db_name, new_collection):
        if self.connection:
            self.connection[db_name][new_collection].insert_many(data)
            return True
        else:
            return("error")
    def display_all(self,db_name,collection_name):
        result=[]
        #If connection is successful
        if(self.connection):
            q=self.connection[db_name][collection_name].find({})
            #Printing all the documents present in the collection
            for data in q:
                print(data)
        else:
            print("Error")
#I have used this API->https://api.thedogapi.com/v1/breeds
#I have saved this API as Breed.json in my machine
with open('Breed.json') as f:
    data = json.load(f)
ob=Ayush_Mongo()
#Will return True is connection is successful 
print(ob.mongo_connection())
#Used for inserting the data in the collection named as Values
print(ob.create_new_collection("DETAIL","Values"))
#For printing all the documents present in the collection
print(ob.display_all("DETAIL","Values"))

