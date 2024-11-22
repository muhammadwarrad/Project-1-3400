import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import util, os
from log_config import logger


class ParentClass:
    def __init__(self, data, config=None):
        """
        Initialize the ParentClass with data and configuration.
        
        :param data: The dataset (e.g., a pandas DataFrame).
        :param config: Dictionary containing configuration constants.
        """
        self.data = data
        self.config = config


    def visualize_data(self, column, plot_type='histogram'):
        """
        Visualize data in a specific column using the specified plot type.
        
        :param column: The column of the DataFrame to visualize.
        :param plot_type: The type of plot ('histogram' or 'line').
        """
        if plot_type == 'histogram':
            self._plot_histogram(column)
        elif plot_type == 'line':
            self._plot_line(column)
        else:
            print(f"Unsupported plot type: {plot_type}")
    
    def _plot_histogram(self, column):
        """
        Generate a histogram for the specified column.
        """
        plt.figure(figsize=(8, 6))
        sns.histplot(self.data[column], kde=True, bins=30)
        plt.title(f"Histogram of {column}")
        plt.xlabel(column)
        plt.ylabel("Frequency")
        plt.show()

    def _plot_line(self, column):
        """
        Generate a line plot for the specified column.
        """
        plt.figure(figsize=(8, 6))
        plt.plot(self.data[column], color='blue')
        plt.title(f"Line Plot of {column}")
        plt.xlabel("Index")
        plt.ylabel(column)
        plt.show()

    def query_data(self, column, value):
        """
        Query the dataset for rows where the value in the specified column meets the condition.
        
        :param column: The column to check.
        :param value: The value to query for.
        :return: A DataFrame containing the rows where the condition is met.
        """
        return self.data[self.data[column] == value]