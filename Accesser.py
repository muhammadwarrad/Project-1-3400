import pandas as pd
import util, Filter, os

info = None

def load_info():
    global info
    if os.path.exists('output.csv'):
        info = pd.read_csv('output.csv')
        print("CSV loaded successfully!")
    else:
        print("Error: output.csv not found.")
    
    
def get_Temp():
        Filter.get_Variable(info, "temperature_2m")
    #
 
def scatter(x, y):
    Filter.scatter(info, x,y)
#

def purge():
    util.purge();
#

if __name__ == "__main__":
    load_info()
    
