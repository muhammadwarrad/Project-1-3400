from config import Data
import Accesser


def main():
    chart = Data(input("Enter latitude: "), input("Enter Longitude: "))

    chart.display_Weather()
    
    Accesser.load_info()
    Accesser.get_Temp()
    
    Accesser.scatter(input("input x:"), input("input y: "))
    
    purge = input("would you like to purge data y/n: ")
    if purge == 'y':
        Accesser.purge()
    
    # Current display is working but we need the param conditions to be dynamic as well.

# test

if __name__ =="__main__":
    main()
#