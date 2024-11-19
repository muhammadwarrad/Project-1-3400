
import pandas as pd
import matplotlib.pyplot as plt 
import Filter, util,os

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
#

def show_Data():
    load_info()
    print(info)
#

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