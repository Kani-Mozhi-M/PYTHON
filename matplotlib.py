#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt


# In[28]:


x=[1,2,3,4,5]
y=[1,2,3,4,5]

plt.scatter(x,y)
plt.plot(x,y)
plt.show()



# In[9]:


x1=[1,2,3,4,5]
y1=[5,4,3,2,1]

plt.scatter(x,y)
plt.plot(x,y)
plt.scatter(x1,y1)
plt.plot(x1,y1)
plt.show()


# In[20]:


plt.plot(x,y,'r*--')
plt.show()


# In[22]:


plt.plot(x,y,'rp--') #p pentagon
plt.show()


# In[24]:


plt.plot(x,y,'rD') #s square D diamond
plt.show()


# In[32]:


import numpy as np
x=np.array([1,2,3,4,5])
y=x**2+10
plt.scatter(x,y) #dot
plt.plot(x,y)
plt.show()


# In[34]:


x=np.arange(0,10,0.1)
y=2*(x**4)+100
# plt.scatter(x,y) #dot
plt.plot(x,y)
plt.show()


# In[54]:


x=np.arange(0,10,0.25)
y=x**4
y1=x**2

plt.plot(x,y,label="x^4")
plt.plot(x,y1,color="r",marker="+",label="x^2")
plt.legend() #label
plt.title("example plot")
plt.text(10,6000,"sample",fontsize=16)
plt.axis([0,20,0,10000]) #x,x,y,y
plt.xlabel("X",fontsize=15)
plt.ylabel("Y")
plt.grid()
plt.show()


# In[62]:


profit=[10,20,30,40]
label=["amazon","flipkart","meesho","snapdeal"]
explode=[0.5,0.1,0,0]
plt.pie(profit,labels=label,autopct="%.2f%%",explode=explode,startangle=90)
plt.show()


# In[67]:


profit=[10,20,30,40]
label=["amazon","flipkart","meesho","snapdeal"]
explode=[0.5,0,0,0]
plt.pie(profit,labels=label,autopct="%.2f%%",explode=explode,startangle=90,counterclock=False)
plt.show()

