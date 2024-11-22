
from Parent import *

info = None
Pr = None

def load_info():
    global Pr
    if os.path.exists('output.csv'):
        Pr = ParentClass(pd.read_csv('output.csv'))
        logger.info("CSV loaded successfully!")
        print("CSV loaded successfully!")
    else:
        print("Error: output.csv not found.")

def get_Temp():
    load_info()
    Pr.visualize_data("temperature")
#

def show_Data():
    load_info()
    print(info)
#

def scatter(x):
    load_info()
    Pr.visualize_data(x)
#

def purge():
    util.purge()


if __name__ == "__main__":
    load_info()