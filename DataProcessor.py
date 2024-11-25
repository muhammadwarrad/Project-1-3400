# Parent class 2.
import pandas as pd
import numpy as np
import pickle
import itertools
import matplotlib.pyplot as plt
from log_config import logger

class DataProcessor:
    def __init__(self,csv_file=None,pickle_file=None):
        self.csv_file = csv_file
        self.pickle_file = pickle_file
        self.data = None

    def csv_to_pickle(self):
        
        try:
            # Check if csv path is valid
            if not self.csv_file:
                raise(Exception('Not a valid path'))
            df = pd.read_csv(self.csv_file)
            self.pickle_file = self.csv_file.replace('csv','pk1')

            with open(self.pickle_file,'wb') as f:
                # Serialize csv file
                pickle.dump(df,f)
            
            logger.info('csv file serialized successfully.')    
            print('csv file serialized successfully.')
        
        except Exception as e:
            print(f'An unexpected error occored: {e}')
            logger.error('csv path not found.')

    def read_pickle(self):
        try:
            if not self.pickle_file:
                raise(Exception('Pickle path not found'))
            
            with open (self.pickle_file,'rb') as f:
                # returns deserialized pickle file.
                self.data = pickle.load(f)
                print("Pickle file loaded successfully")
                logger.info("Pickle file loaded successfully")
            
            return self.data
        except Exception as e:
            print(f'An unexpected error occored: {e}')
            logger.error('csv path not found.')


# Sample code run
# if __name__ == "__main__":
    # dp = DataProcessor("output.abc",None)
    # dp.csv_to_pickle()
    # print(dp.read_pickle())