from config import Data
import Accesser


def main():
    Data(input("Enter latitude: ").split(), input("Enter Longitude: ").split())
    Accesser.show_Data()
    
    print("Would you like to Purge data? y/n")
    if( input() == 'y'):
        Accesser.purge()
    

    
    
if __name__ =="__main__":
    main()
#
