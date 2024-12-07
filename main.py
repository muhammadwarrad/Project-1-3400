from Api import Data
from Accesser import Access, util
from DataAnalyzer import DataAnalyzer


# Constants for menu options
SHOW_DATA = '1'
VISUALIZE_DATA = '2'
QUERY_DATA = '3'
GRAPH_DATA = '4'
GET_STATS = '5'
SEE_UNIQUE_VALUES = '6'
GET_JOINT_COUNTS = '7'
GET_PERMUTATIONS = '8'
GET_DOT_PRODUCT = '9'
BOOL_INDEX = '10'
ADD_LOCATIONS = '11'  # New option to add locations
QUIT = 'q'


def get_input_with_prompt(prompt):
    """Utility function to get input with a custom prompt"""
    return input(prompt)


def handle_graph_type():
    """Handle graph type selection"""
    graph_type = get_input_with_prompt("What type of graph: scatter, whisker, violin? ")
    if graph_type == "scatter":
        return "scatter"
    elif graph_type == "whisker":
        return "whisker"
    elif graph_type == "violin":
        return "violin"
    else:
        print("Not supported type")
        return None


def handle_user_choice(res, test: Access, analizer: DataAnalyzer):
    """Handle user choice for actions like show data, visualize, etc."""
    try:
        if res == SHOW_DATA:
            test.show_Data()
        elif res == VISUALIZE_DATA:
            graph_type = get_input_with_prompt("line or histogram? ")
            col = get_input_with_prompt("Enter Data column name: ")
            test.visualize_data(col, graph_type)
        elif res == QUERY_DATA:
            column = get_input_with_prompt("Please select the column you would like to query (e.g., temperature): ")
            value = get_input_with_prompt("What value are you searching for? ")
            test.query_data(column, value)
        elif res == GRAPH_DATA:
            graph_type = handle_graph_type()
            if graph_type == "scatter":
                x_value = get_input_with_prompt("Enter x Value: ")
                y_value = get_input_with_prompt("Enter y Value: ")
                test.scatter(x_value, y_value)
            elif graph_type == "whisker":
                data = get_input_with_prompt("Enter data to graph (e.g., temperature): ")
                test.whisker(data)
            elif graph_type == "violin":
                data = get_input_with_prompt("Enter data to graph. Multiple categories are accepted: ")
                data = data.split()
                test.violen(*data)
        elif res == GET_STATS:
            data = get_input_with_prompt("Enter Data column name: ")
            print(analizer.calculate_statistics(data))
        elif res == SEE_UNIQUE_VALUES:
            column_name = get_input_with_prompt("Enter data column name: ")
            print(analizer.get_unique_values(column_name))
        elif res == GET_JOINT_COUNTS:
            data1 = get_input_with_prompt("Enter name of Data 1: ")
            data2 = get_input_with_prompt("Enter name of Data 2: ")
            print(analizer.calculate_joint_counts(data1, data2))
        elif res == GET_PERMUTATIONS:
            column_name = get_input_with_prompt("Enter Data column name: ")
            print(analizer.generate_permutations(column_name,))
        elif res == GET_DOT_PRODUCT:
            index1 = int(get_input_with_prompt("Enter index 1: "))
            index2 = int(get_input_with_prompt("Enter index 2: "))
            vector1 = analizer.get_position_vector(index1)
            vector2 = analizer.get_position_vector(index2)
            print(analizer.calculate_dot_product(vector1, vector2))
        elif res == BOOL_INDEX:
            type = get_input_with_prompt("Please enter \"greater\" or \"less\"")
            data:str = get_input_with_prompt("Enter Data name: ")
            val:int = get_input_with_prompt("Enter your value: ")
            if(type == "greater"):
                print(f"{sum(test.bool_index_GE(data,val))} values in {data} are Greater than {val}")
            elif(type == "less"):
                print(f"{sum(test.bool_index_LE(data,val))} values in {data} are less than {val}")
            else:
                print("Sorry please try again")
                
        elif res == ADD_LOCATIONS:
            latitudes = get_input_with_prompt("Enter Latitudes: ").split()
            longitudes = get_input_with_prompt("Enter Longitudes: ").split()
            Data(latitudes, longitudes)
            test.load_Data()
            analizer.csv_to_pickle()
            analizer.read_pickle()
        else:
            print("Invalid option. Please try again.")
    except ValueError as e:
        print(f"Value error occurred: {e}. Please ensure your inputs are valid.")
    except IndexError as e:
        print(f"Index error occurred: {e}. Please check your indices.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Continuing program execution...\n")  # Ensures the program continues running


def main():
    # Initialize objects
    test = Access()
    analizer = DataAnalyzer("Data.csv", None)
    analizer.read_pickle()
    
    print("Welcome!\n")
    
    while True:
        try:
            # Display menu
            print("\nWhat would you like to do?")
            print(f"{SHOW_DATA}. Show Data")
            print(f"{VISUALIZE_DATA}. Visualize Data")
            print(f"{QUERY_DATA}. Query Data")
            print(f"{GRAPH_DATA}. Graph Data")
            print(f"{GET_STATS}. Get Stats")
            print(f"{SEE_UNIQUE_VALUES}. See Unique Values")
            print(f"{GET_JOINT_COUNTS}. Get Joint Counts")
            print(f"{GET_PERMUTATIONS}. Get Permutations")
            print(f"{GET_DOT_PRODUCT}. Get Dot Product")
            print(f"{BOOL_INDEX}. Find greater or less than")
            print(f"{ADD_LOCATIONS}. Add Locations") 
            print(f"{QUIT}. Quit")
            
            res = get_input_with_prompt("Select an option: ")
            
            if res == QUIT:
                util.purge()
                print("Exiting the program...")
                break
            
            # Pass the objects to handle_user_choice
            handle_user_choice(res, test, analizer)

        except Exception as e:
            print(f"An unexpected error occurred in the main loop: {e}")
            print("The program will continue...\n")


if __name__ == "__main__":
    main()
