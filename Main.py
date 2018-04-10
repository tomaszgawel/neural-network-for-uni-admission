import DataNormalization
import DataController
import NeuralNetwork
import neurolab as nl
import numpy as np

columns_names = []
data_list = []
DataController.load_data_list("data/results.csv", data_list, columns_names)
data_list = DataController.clear_outliners(data_list,columns_names)
quantity_of_columns = len(columns_names)

data = DataNormalization.Data(quantity_of_columns)
data.calc_avg(data_list)
data.calc_deviation(data_list)
data.normalize(data_list)


input_temp = []
temp = []
output_temp = []
for row in data_list:
    i = 0
    for item in row:
        if i+1 == quantity_of_columns:
            output_temp.append([int(item)])
        else:
            temp.append(item)
        i += 1
    input_temp.append(temp)
    temp = []

NN = NeuralNetwork.NeuralNet(input_temp,output_temp)
NN.create_and_train_nn(quantity_of_columns)
out = NN.test([[input(), input()]])
print(out)