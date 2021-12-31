# Deploying Piu Mosso Client Guide
## 1. Download and install Python
Download and install Python from https://www.python.org/downloads/. Make sure you select the option to add the python and pip executables to the PATH environment variable during the setup.

## 2. (Optional) Create a virtual environment
If python is already installed on your machine along with a lot of pip packages it may be a good idea to run the application in a virtual environment to isolate the dependencies. To do this open a command prompt in the client program’s directory and run the following:

```python -m venv env```

```.\env\Scripts\activate```

This will create a virtual environment in a subdirectory named ‘env’ and enter a subshell inside that virtual environment. Use this subshell to install the dependencies and run the program as described by the next two steps.

## 3. Install the dependencies
To install the project’s dependencies (the requests library and the Python bindings for Qt6), run the following in a command prompt open in the project’s directory:

```pip install -r requirements.txt```

## 4. Run the program
To run the program, invoke the python interpreter on the ‘main.py’ file like this:

```python main.py```
