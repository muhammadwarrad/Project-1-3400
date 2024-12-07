
from Filter import *


class Access(ParentClass):
    info = None

    def __init__(self):
        
        global info
        super().__init__(self.info, CSV_CONFIG)
        self.load_Data()
        
            
    def load_Data(self):
        if os.path.exists('Data.csv'): 
            
            self.info = pd.read_csv(**self.config)
            self.data= self.info 
            logger.info("CSV loaded successfully!")
            
        else:
            logger.error("Data.csv not found.")
        
        

    def get_Temp(self):
        super().visualize_data("temperature")
    #

    def show_Data(self):
        print(self.info)
    #

    def scatter(self, x:str, y:str):
        plt.scatter( self.info[x], self.info[y])
        plt.xlabel(x)
        plt.ylabel(y)
        plt.title(f'{x} vs {y}')
        plt.show()
    #
    
    def whisker(self, x:str):
        plt.boxplot( self.info[x])
        plt.xlabel(x)
        plt.title(f'{x} ')
        plt.show()
    #
    
    def violen(self, *catigories:str):
        
        sns.violinplot(self.info[list(catigories)])
        plt.show()
    #
    
            
        
    
    

    def purge(self):
        util.purge()
        
    def eval_query_equals(self, column, value):
        #Prints false on all rows that dont equal value
        #Prints true on all rows that equal value
        return(eval("self.data[column] == value"))
        
    def bool_index_GE(self, col, num):
        return(eval("self.info[col] > float(num)"))
    
    def bool_index_LE(self, col, num):
        return(eval("self.info[col] < float(num)"))
        
        
    


if __name__ == "__main__":
    test = Access()
    print(test.bool_index_GE("temperature", 20))