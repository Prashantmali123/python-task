#!/usr/bin/env python
# coding: utf-8

# Task 1: Classification Model Implementation  
# Problem: Build a classification model (e.g., Logistic Regression or Random Forest) to predict 
# whether an email is spam or non-spam. 
# date : 06 feb 2025
# by : prashant mali

# In[ ]:


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


# In[15]:


file_path = r"C:\Users\Prashant\.cache\kagglehub\datasets\balaka18\email-spam-classification-dataset-csv\versions\1\emails.csv"
df = pd.read_csv(file_path)


# In[16]:


print(df.columns)


# In[17]:


df = df.iloc[:, 1:]


# In[18]:


X = df.drop(columns=["Prediction"])
y = df["Prediction"]


# In[19]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# In[20]:


model = LogisticRegression()
model.fit(X_train, y_train)


# In[21]:


y_pred = model.predict(X_test)


# In[22]:


accuracy = accuracy_score(y_test, y_pred) * 100
print(f'Accuracy: {accuracy:.2f}%')  # Display accuracy as a percentage
print(classification_report(y_test, y_pred))


# In[ ]:




