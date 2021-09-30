#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Task:MEAN
#Program By:Ayush Pandey
#Email Id:1805290@kiit.ac.in
#DATE:30-Sept-2021
#Python Version:3.7
#CAVEATS:None
#LICENSE:None


# In[2]:


#Write a python program to calculate the harmonic mean and geometric mean

class Ayush:
    #Harmonic mean is a kind ofaverage which is calculated by dividing the numbers of a datasetby the reciprocal of each number
    def harmonic(self,a):
        summ=0
        for i in range(len(a)):
            summ=summ+(1/a[i])
        print(len(a)/summ)
        
    #Geometric mean is the average value which signifies the central tendency of a dataset by finding the product of their values
    def geometric(self,a):
        summ=1
        for i in a:
            summ*=i
        print(summ**(1/len(a)))
a=list(map(int,input().split(" ")))
ob=Ayush()
ob.harmonic(a)
ob.geometric(a)


# In[3]:


#Write a python program to calculate the VARIANCE of a population
# 1->Find the mean First
# 2->Substract the mean from each data units
# 3->Square the values obtained from the point 2
# 4->The resultant will be the average of square difference


def ayush(a):
    summ=0
    for i in range(0,len(a),1):
        summ+=a[i]
    mean=summ/len(a)
    print("Mean is:",mean)
    for i in range(0,len(a)):
        a[i]=a[i]-mean
    print("New list after substraction from mean:")
    print(a)
    print("Squarring the values:")
    for i in range(0,len(a)):
        a[i]=a[i]**2
    print("New list:",a)
    summ=0
    for i in range(0,len(a),1):
        summ+=a[i]
    variance=summ/len(a)
    print("Variance is:",variance)
a=list(map(int,input().split(" ")))
ayush(a)


# In[ ]:





# In[ ]:





# In[ ]:




