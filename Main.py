import DataNormalization
import DataController
import NeuralNetwork

# loading data
columns_names = []
data_list = []
DataController.load_data_list("data/results.csv", data_list, columns_names)
data_list = DataController.clear_outliners(data_list,columns_names)
quantity_of_columns = len(columns_names)

# copying data for input
data_input = []
for row in data_list:
    data_input.append(list(row))

# normalization of data
data = DataNormalization.Data(quantity_of_columns)
data.calc_avg(data_list)
data.calc_deviation(data_list)
data.normalize(data_list)

# splitting data into input and output list
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

# creating neural network
NN = NeuralNetwork.NeuralNet(input_temp,output_temp)
NN.create_and_train_nn(quantity_of_columns)

# input for the user
print("Enter data [%]:")
test_input = []
i = 0
for item in columns_names:
    if i+1 == len(columns_names):
        test_input.append(int(1))
        break
    print(item+": ")
    x = input()
    test_input.append(float(x))
    i += 1

# adding user input into a list with data
data_input.append(test_input)

# normalization of data with user input
data2 = DataNormalization.Data(quantity_of_columns)
data2.calc_avg(data_input)
data2.calc_deviation(data_input)
data2.normalize(data_input)

# testing user input
out = NN.test([data_input[len(data_input)-1][:-1]])
print("Chances of getting into university:")
print(str(int(round(out[0][0],2)*100))+"%")
