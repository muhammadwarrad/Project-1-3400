from config import Data
import Accesser


def main():
    Data(input("Enter latitude: ").split(), input("Enter Longitude: ").split())
    Accesser.get_Temp()
    

    
    # Current display is working but we need the param conditions to be dynamic as well.

# test

if __name__ =="__main__":
    main()
#