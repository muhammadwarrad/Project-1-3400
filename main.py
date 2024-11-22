from config import Data
import Accesser


def main():
    Data(input("Enter latitude: ").split(), input("Enter Longitude: ").split())
    
    
    Accesser.scatter("temperature")
    
    

    
    
if __name__ =="__main__":
    main()
#
