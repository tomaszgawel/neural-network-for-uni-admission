import DataNormalization
import DataController
import NeuralNetwork
import PyplotGraphs

class Control(object):
    def __init__(self):
        self.data = []
        self.data_temp = []
        self.input = []
        self.output = []
        self.columns_names = []
        self.quantity_of_columns = None
        self.NN = None

    def load_data(self):
        self.data.clear()
        self.columns_names.clear()
        DataController.load_data_list("data/data.csv", self.data, self.columns_names)
        self.data = DataController.clear_outliners(self.data,self.columns_names)
        self.quantity_of_columns = len(self.columns_names)
        if len(self.data_temp) == 0:
            for row in self.data:
                self.data_temp.append(list(row))
        PyplotGraphs.create_input_graphs(self.data, self.columns_names, self.quantity_of_columns)

    def copy_data(self):
        self.data.clear()
        for row in self.data_temp:
            self.data.append(list(row))

    def normalize_data(self):
        data = DataNormalization.Data(self.quantity_of_columns)
        data.calc_avg(self.data)
        data.calc_deviation(self.data)
        data.normalize(self.data)
        DataController.saveNormalizedData(self.data, self.columns_names)

    def split_data(self):
        self.input.clear()
        temp = []
        self.output.clear()
        for row in self.data:
            i = 0
            for item in row:
                if i + 1 == self.quantity_of_columns:
                    self.output.append([int(item)])
                else:
                    temp.append(item)
                i += 1
            self.input.append(temp)
            temp = []

    def create_and_learn_naural_net(self):
        self.NN = NeuralNetwork.NeuralNet(self.input, self.output)
        print("Learning has started:")
        self.NN.create_and_train_nn(self.quantity_of_columns, self.columns_names)

    def add_user_input_into_data(self, gpe, gre, prestige):
        self.data.append([float(gpe), float(gre), float(prestige), 0.0])

    def test_user_input(self):
        return self.NN.test([self.data[len(self.data)-1][:-1]])