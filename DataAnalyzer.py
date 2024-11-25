# Child class 2
from DataProcessor import *
class DataAnalyzer(DataProcessor):
    def __init__(self,csv_data=None,pickle_data=None):
        super().__init__(csv_data,pickle_data)

    # 
    def calculate_joint_counts(self, col1, col2):
        "Calculate joint counts for two categorical columns."
        return pd.crosstab(self.data[col1], self.data[col2])

    def calculate_joint_probabilities(self, col1, col2):
        "Calculate joint probabilities for two categorical columns."
        joint_counts = self.calculate_joint_counts(col1, col2)
        return joint_counts / len(self.data)

    def calculate_conditional_probability(self, col1, col2, value1, value2):
        "Calculate conditional probability P(value1 | value2)."
        joint_probs = self.calculate_joint_probabilities(col1, col2)
        return joint_probs.loc[value1, value2]

    # Statistical Operations
    def calculate_statistics(self, col):
        "Calculate mean, median, and standard deviation for a column."
        return {
            'mean': self.data[col].mean(),
            'median': self.data[col].median(),
            'std': self.data[col].std()
        }

    # Vector Operations
    def get_position_vector(self, row_index):
        "Obtain position vector (latitude, longitude) for a given row."
        row = self.data.iloc[row_index]
        return np.array([row['latitude'], row['longitude']])

    def calculate_unit_vector(self, vector):
        "Calculate the unit vector of a given vector."
        return vector / np.linalg.norm(vector)

    def calculate_projection(self, vector1, vector2):
        "Calculate the projection of vector1 onto vector2."
        vector2_unit = self.calculate_unit_vector(vector2)
        return np.dot(vector1, vector2_unit) * vector2_unit

    def calculate_dot_product(self, vector1, vector2):
        "Calculate the dot product between two vectors."
        return np.dot(vector1, vector2)

    def calculate_angle_between_vectors(self, vector1, vector2):
        "Calculate the angle between two vectors in degrees."
        cos_theta = np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2))
        return np.degrees(np.arccos(np.clip(cos_theta, -1.0, 1.0)))

    def check_orthogonality(self, vector1, vector2):
        "Check if two vectors are orthogonal i.e(dot product = 0)."
        return np.isclose(self.calculate_dot_product(vector1, vector2), 0)

    # Categorical Attribute Operations
    def get_unique_values(self, col):
        "Get unique values of a categorical column."
        return self.data[col].unique()

    def generate_permutations(self, col, n):
        "Generate permutations of unique values in a column."
        unique_values = self.get_unique_values(col)
        # result of itertools.permutations is an iteratotr and is converted to a list
        return list(itertools.permutations(unique_values, n))

    def generate_combinations(self, col, n):
        "Generate combinations of unique values in a column."
        unique_values = self.get_unique_values(col)
        # result of itertools.combinations is an iteratotr and is converted to a list
        return list(itertools.combinations(unique_values, n))

    # Visualization
    def visualize_column(self, col, kind='hist'):
        "Visualize a column with a specified plot type."
        self.data[col].plot(kind=kind)
        plt.title(f"{col} - {kind}")
        plt.show()

if __name__ == '__main__':
    analyzer = DataAnalyzer('output.csv',None)

    analyzer.csv_to_pickle()
    data = analyzer.read_pickle()

    # Statistics example.
    print(data)
    print("Joint counts: ")
    # print(analyzer.calculate_joint_counts('temperature','windspeed'))

    print('Statistics for windspeed: ')
    print(analyzer.calculate_statistics('windspeed'))

    # Vector example

    vector1 = analyzer.get_position_vector(0)
    vector2 = analyzer.get_position_vector(1)
    print('Dot product of vectors: ')
    print(analyzer.calculate_dot_product(vector1,vector2))

    # Categorical Attribute Operations example
    print("Unique values for windspeed:")
    print(analyzer.get_unique_values("windspeed"))

    print("Permutations for weathercode:")
    print(analyzer.generate_permutations('weathercode',2))

    # Visualization example.
    print("Histogram for windspeed:")    
    analyzer.visualize_column('windspeed','hist')
