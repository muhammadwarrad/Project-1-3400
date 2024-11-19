
import pandas as pd
import matplotlib.pyplot as plt 
import Filter, util,os
# If you're using matplotlib for scatter plotting

# Assuming 'Filter' and 'util' are modules or classes that you have access to
# You should import them like this (if they are custom modules or classes):
# from your_module_name import Filter, util
info = None

def load_info():
    global info
    if os.path.exists('output.csv'):
        info = pd.read_csv('output.csv')
        print("CSV loaded successfully!")
    else:
        print("Error: output.csv not found.")

def get_Temp():
    load_info()
    if info is not None:
        Filter.get_Variable(info, "temperature")
    else:
        print("Error: Info has not been loaded.")

def scatter(x, y):
    load_info()
    if info is not None:
        Filter.scatter(info, x, y)
    else:
        print("Error: Info has not been loaded.")

def purge():
    util.purge()


if __name__ == "__main__":
    pass