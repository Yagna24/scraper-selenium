#!/usr/bin/env python
# coding: utf-8

# In[1]:


import selenium 
from selenium import webdriver 

# In[2]:


path = r'C:\Program Files (x86)\chromedriver.exe'


# In[3]:


driver = webdriver.Chrome(path)


# In[4]:



driver.get("https://www.walmart.com/reviews/product/14898365?sort=submission-asc")


# In[6]:


print(driver.title)


# In[12]:


mains = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div[6]/div[1]/div[1]/div/div[1]')
date = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div[6]/div[1]/div[1]/div/div[1]/div/div[2]/span')
name = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div[6]/div[1]/div[1]/div/div[1]/div/div[4]/div/div/span[2]')
title = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div[6]/div[1]/div[1]/div/div[1]/div/div[1]/div[1]/h3')
rating = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div[6]/div[1]/div[1]/div/div[1]/div/div[1]/div[1]/div/div')
#print(rating.text)
desc = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div[6]/div[1]/div[1]/div/div[1]/div/div[3]/div/div')


# In[23]:


datelist =[]
link = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div[6]/div[2]/div/div/button')
one = '/html/body/div[1]/div/div/div/div[1]/div/div[6]/div[1]/div['
two = ']/div/div[1]/div/div[2]'
for i in range(0,5):
    link.click()
    for x in range(1,20,1) :
        path = one+str(x)+two
        date = driver.find_element_by_xpath(path)
        datelist.append(date.text)
    


# In[26]:


namelist =[]
link = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div[6]/div[2]/div/div/button')
one = '/html/body/div[1]/div/div/div/div[1]/div/div[6]/div[1]/div['
two = ']/div/div[1]/div/div[4]/div/div/span[2]'
for i in range(0,5):
    link.click()
    for x in range(1,20,1) :
        path = one+str(x)+two
        name = driver.find_element_by_xpath(path)
        
        namelist.append(name.text)
    


# In[28]:


starlist =[]

link = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div[6]/div[2]/div/div/button')
one = '/html/body/div[1]/div/div/div/div[1]/div/div[6]/div[1]/div['
two = ']/div/div[1]/div/div[1]/div[1]/div/div'
for i in range(0,5):
    link.click()
    for x in range(1,20,1) :
        path = one+str(x)+two
        rating = driver.find_element_by_xpath(path)
        
        starlist.append(rating.text)
    


# In[30]:


titlelist =[]
link = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div[6]/div[2]/div/div/button')
one = '/html/body/div[1]/div/div/div/div[1]/div/div[6]/div[1]/div['
two = ']/div/div[1]/div/div[1]/div[1]/h3'
for i in range(0,5):
    link.click()
    for x in range(1,20,1) :
        path = one+str(x)+two
        title = driver.find_element_by_xpath(path)
        titlelist.append(title.text)


# In[32]:


desclist =[]
link = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div[6]/div[2]/div/div/button')
one = '/html/body/div[1]/div/div/div/div[1]/div/div[6]/div[1]/div['
two = ']/div/div[1]/div/div[3]/div/div'
for i in range(0,5):
    link.click()
    for x in range(1,20,1) :
        path = one+str(x)+two
        desc = driver.find_element_by_xpath(path)
        desclist.append(desc.text)


# In[33]:


all_items = {
    'title' : titlelist,
    'description' : desclist,
    'Date' : datelist,
    'Rating' : starlist,
    'Names' : namelist
}


# In[34]:


import pandas as pd
df = pd.DataFrame(all_items)


# In[35]:


df.to_csv(r'C:\Users\HP\Desktop\web.csv')

