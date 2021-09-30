#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Program:To get a list of all factorial and kaprekar number in the range 1 to 10 
#Program By:Ayush Pandey
#Email Id:1805290@kiit.ac.in
#DATE:28-Sept-2021
#Python Version:3.7
#CAVEATS:None
#LICENSE:None


# In[ ]:





# In[2]:


#As the range from 1 to 10000 was giving too large values for the factorials so I am doing this program for range 1 to 100
import numpy as np
import math
#Created a list named as factorial and kaprekar
factorial=[]
Kaprekar=[]

#Here I am calculating the factorial of each element
for i in range(1,100):
    factorial.append(math.factorial(i))
    
#Here I am checking whether the element is kaprekar or not

#Kaprekar is a number which after squared can be splitted into two parts such that sum of parts
#is equal to the original number and none of the parts has value 0. 

for n in range(1,100):
    n2 = str(n**2)
    for i in range(len(n2)):
        a, b = int(n2[:i] or 0), int(n2[i:])
        if b and a + b == n:
            Kaprekar.append(n)
factorial=np.array(factorial)
Kaprekarr=np.array(Kaprekar)

#Creating a dictionary
json_dict={"Factorial":factorial[0::],"Kaprekar":Kaprekar[0::]}
print(json_dict)


# In[ ]:




