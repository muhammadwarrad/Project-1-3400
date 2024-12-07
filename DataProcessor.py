import pandas as pd
import numpy as np
import pickle
import itertools
import matplotlib.pyplot as plt
import logging
import logging.config
from config import LOGGING_CONFIG

# Configure logging using the LOGGING_CONFIG dictionary
logging.config.dictConfig(LOGGING_CONFIG)

# Create a logger instance for this module
logger = logging.getLogger(__name__)

class DataProcessor:
    def __init__(self, csv_file=None, pickle_file=None):
        self.csv_file = csv_file
        self.pickle_file = pickle_file
        self.data = None

    def csv_to_pickle(self):
        try:
            # Check if csv path is valid
            if not self.csv_file:
                raise(Exception('Not a valid path'))
            
            df = pd.read_csv(self.csv_file)
            self.pickle_file = self.csv_file.replace('csv', 'pk1')

            with open(self.pickle_file, 'wb') as f:
                # Serialize CSV file
                pickle.dump(df, f)

            logger.info('CSV file serialized successfully.')
            print('CSV file serialized successfully.')

        except Exception as e:
            print(f'An unexpected error occurred: {e}')
            logger.error(f'Error in csv_to_pickle: {e}')

    def read_pickle(self):
        try:
            if not self.pickle_file:
                raise(Exception('Pickle path not found'))

            with open(self.pickle_file, 'rb') as f:
                # Returns deserialized pickle file.
                self.data = pickle.load(f)

            logger.info("Pickle file loaded successfully")
            print("Pickle file loaded successfully")
            return self.data

        except Exception as e:
            print(f'An unexpected error occurred: {e}')
            logger.error(f'Error in read_pickle: {e}')
