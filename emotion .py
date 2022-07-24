#!/usr/bin/env python
# coding: utf-8

# In[11]:


import cv2
from deepface import DeepFace
import matplotlib.pyplot as plt


# In[3]:


img = cv2.imread('/Users/user/Downloads/womensad.jfif')
print('read image correct')


# In[5]:


plt.imshow(cv2.cvtColor(img , cv2.COLOR_BGR2RGB))


# In[6]:


predictionImg = DeepFace.analyze(img)


# In[7]:


predictionImg


# In[10]:


predictionImg['dominant_emotion']
   


# In[ ]:




