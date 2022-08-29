#!/usr/bin/env python
# coding: utf-8

# # Notebooks on Windows OS
# 
# Jupyter Book also works on Windows OS and for easy to setup. There are several methods to do and in this guide I'll show how to setup using one of the many methods.
# Since it was difficult to get Jupyter Notebook to work on Windows. 
# 
# Below listing all possible ways:
# 
# 1. Using Python or Conda installation locally on a Windows OS machine. 
# 2. Using a pre-built Docker image or creating your own.
# 3. Using a Virtual Machine.
# 4. Using Windows Subsystem for Linux (WSL) & Linux OS from Microsoft Store (i.e. Ubuntu).
# 
# I ended up going with #1 and will demonstrate what's needed in this guide. 
# 
# ## What's needed
# 
# Here is my current setup:
# 
# 1. Windows 10 (Microsoft Windows [Version 10.0.19044.1826])
# 2. Python 3.10.6 app from the Microsoft Store [Available here] (https://www.microsoft.com/store/productId/9PJPW5LDXLZ5)
# 
# That's all that is needed to get started! If you don't have Python installed, please use the above link to install. 
# 
# ## Install Jupyter Book

# In[1]:


> pip install jupyter-book pandas plotly sphinx-thebe


# ## Steps
# 
# With MyST Markdown, you can define code cells with a directive like so:

# In[ ]:


> C:\Users\{user}\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts\jupyter-book create jupiter


# Navigate to the directory and build the book

# In[ ]:


> C:\Users\{user}\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts\jupyter-book build ./

