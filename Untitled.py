
# coding: utf-8

# In[1]:

import moduletest


# In[2]:

moduletest.test1("te")


# In[3]:

moduletest.test2("tes")


# In[4]:

import os


# In[6]:

os.getcwd()


# In[7]:

get_ipython().system('cd ../')


# In[8]:

os.getcwd()


# In[10]:

os.chdir("../")


# In[11]:

os.getcwd()


# In[12]:

currendir = os.getcwd()


# In[13]:

os.chdir("te")


# In[14]:

os.chdir("tes")


# In[15]:

os.getcwd()


# In[16]:

os.chdir(currendir)


# In[17]:

os.getcwd()


# In[18]:

os.chdir("te/tes")


# In[19]:

os.getcwd()


# In[20]:

os.chdir("../../")


# In[21]:

os.getcwd()


# In[22]:

with os.chdir("te"):
    os.mkdir("test")


# In[ ]:



