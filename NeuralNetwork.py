import neurolab as nl
import numpy as np
import pandas as pd


class NeuralNet(object):
    # creating numpy array for input and output
    def __init__(self, input, output):
        self.input = np.array(input)
        self.output = np.array(output)
        self.net = None

    # creating neural network with w 3 layers using neurolab library
    # quantity of columns - 1 neurons in input layer, 6 in hidden layer and 1 in output layer
    # training neural network
    def create_and_train_nn(self, columns, col_names):
        i = 0
        pr = []
        while i < columns - 1:
            pr.append([-2, 2])
            i += 1
        self.net = nl.net.newff(pr, [columns - 1, 6, 1])
        err = self.net.train(self.input, self.output, epochs=30, show=20, goal=0.01)
        self.net.save("data/network.net")


    # method that returns output of the network using user's input
    def test(self, test_arr):
        return self.net.predict(test_arr)


class LoadedNeuralNet(object):
    def __init__(self):
        self.net = None

    def load_neural_network(self, path):
        self.net = nl.load(path)

    def test(self, test_arr):
        return self.net.predict(test_arr)
