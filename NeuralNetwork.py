import neurolab as nl
import numpy as np
import pandas as pd


class NeuralNet(object):
    # creating numpy array for input and output
    def __init__(self):
        self.net = None

    # creating neural network with w 3 layers using neurolab library
    # quantity of columns - 1 neurons in input layer, 5 hidden layers and 1 in output layer
    # training neural network
    def create_and_train_nn(self, columns, input, output):
        self.input = np.array(input)
        self.output = np.array(output)
        i = 0
        pr = []
        while i < columns - 1:
            pr.append([-2, 2])
            i += 1
        self.net = nl.net.newff(pr, [columns - 1, 9, 9, 9, 9, 9, 1])
        err = self.net.train(self.input, self.output, epochs=60, show=20, goal=0.01)
        self.net.save("data/network.net")

    def load_neural_network(self, path):
        self.net = nl.load(path)

    # method that returns output of the network using user's input
    def test(self, test_arr):
        return self.net.sim(test_arr)
