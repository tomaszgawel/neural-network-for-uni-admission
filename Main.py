import DataNormalization
import DataController

columns_names = []
data_list = []
DataController.load_data_list("data/results.csv", data_list, columns_names)
data_list = DataController.clear_outliners(data_list,columns_names)
quantity_of_columns = len(columns_names)

data = DataNormalization.Data(quantity_of_columns)
data.calc_avg(data_list)
data.calc_deviation(data_list)
data.normalize(data_list)

