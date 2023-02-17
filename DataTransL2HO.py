#!/usr/bin/env python
# coding: utf-8

# #Python Data Transformation

# In[1]:


import pandas as pd
import numpy as np


# # Dataset 1

# In[19]:


airbnb_test_users = pd.read_csv('C:/Users/Nessa/Desktop/Data Wrangling/airbnb_test_users.csv')


# In[20]:


airbnb_test_users.head()


# # What is the average age of those who use each web browser type?

# In[ ]:


# groupby()
# states.groupby('State')['Cases'].sum()


# In[39]:


airbnb_test_users.columns


# In[40]:


airbnb_test_users.groupby('first_browser')['age'].mean()


# # What is the total signup_flow for each device?

# In[ ]:


# groupby()
# states.groupby('State')['Cases'].sum()


# In[41]:


airbnb_test_users.groupby('first_device_type')['signup_flow'].sum()


# # Dataset 2

# In[31]:


airbnb_sample_submission = pd.read_csv(r"C:\Users\Nessa\Desktop\Data Wrangling\airbnb_sample_submission.csv")


# In[32]:


airbnb_sample_submission.head()


# # They need the country information from this dataset included in the airbnb_test_users file.

# In[ ]:


# merge()
# planes = pd.merge(features, candidates, on='adshex')


# In[43]:


airbnb2 = pd.merge(airbnb_test_users,airbnb_sample_submission, on = "id")


# In[44]:


airbnb2.head()


# # Dataset 3

# In[29]:


airbnb_users = pd.read_excel('C:/Users/Nessa/Desktop/Data Wrangling/airbnb_users.xlsx')


# In[34]:


airbnb_users.head()


# # Add additional users to the test file from this dataset.

# In[ ]:


# concat()
# Muscles3 = pd.concat([Muscles1, Muscles2])


# In[45]:


airbnb3 = pd.concat([airbnb2, airbnb_users])


# In[46]:


airbnb3.head()


# In[ ]:




