import DataNormalization
import DataController

data_list = []

DataController.load_data_list("data/results.csv", data_list)

data = DataNormalization.Data()
data.calc_avg(data_list)
data.calc_deviation(data_list)
data.normalize(data_list)




