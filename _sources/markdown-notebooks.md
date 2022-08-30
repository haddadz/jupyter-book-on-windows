---
jupytext:
  cell_metadata_filter: -all
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Notebooks on Windows OS

Jupyter Book also works on Windows OS with fairly minimum effort to setup. There are several methods to do so and in this guide I'll highlight one particular way.
Since it is claimed that Jupyter Notebook is not as easy to to work on Windows OS. 

Below listing all possible ways:

1. Using Python or Conda installation locally on Windows OS. 
2. Using a pre-built Docker image or creating your own.
3. Using a virtual machine.
4. Using Windows Subsystem for Linux (WSL) & Linux OS from the Microsoft Store (i.e. Ubuntu).

I ended up going with #1 and will demonstrate what's needed in this guide. 

## What's needed

Here is my current setup:

1. Windows 10 (Microsoft Windows [Version 10.0.19044.1826])
2. Python 3.10.6 app from the Microsoft Store [Available here](https://www.microsoft.com/store/productId/9PJPW5LDXLZ5)

That's all that is needed to get started! If you don't have Python installed, please use the above link to install. 

## Install Jupyter Book


```{code-cell}
# pip install jupyter-book pandas plotly sphinx-thebe
```

## Steps

Once you have installed the python libraries using pip, run the following commands in Command Prompt (cmd):

```{code-cell}
# C:\Users\{user}\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts\jupyter-book create jupiter
```
Navigate to the directory and build the book using the following link:

```{code-cell}
> C:\Users\{user}\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts\jupyter-book build ./
```
The trick here was to locate the Python folder which contains the jupyter-book or adding it to your OS env path. If you have insatlled python or conda using a different method, locat ethe jupyter-book folder accordingly. 

```{code-cell}
> dir "\jupyter-book" /s /p
```
