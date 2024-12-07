import os

f = None

def get_path():
    if os.path.exists('Data.csv'):
        f = open("Data.csv", 'r')
    
    
def read_CSV():
        return(f.read())
#
def purge():
    os.remove("Data.csv")
    os.remove("Data.pk1")
    print("Saved data has been deleted")
#

if __name__ == "__main__":
    get_path()


