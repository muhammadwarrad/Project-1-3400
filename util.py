import os
import time

f = None

def get_path():
    f = open("output.csv", 'r')
    
    
def read_CSV():
        return(f.read())
#
def purge():
    os.remove("output.csv")
    print("ALL DATA HAS BEEN PURGED!")
#

if __name__ == "__main__":
    get_path()

