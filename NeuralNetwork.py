import neurolab as nl
import numpy as np


class NeuralNet(object):
    # creating numpy array for input and output
    def __init__(self, input, output):
        self.input = np.array(input)
        self.output = np.array(output)
        self.net = None

    # creating neural network with w 3 layers using neurolab library
    # quantity of columns - 1 neurons in input layer, 6 in hidden layer and 1 in output layer
    # training neural network
    def create_and_train_nn(self, columns):
        i = 0
        pr = []
        while i < columns - 1:
            pr.append([-2, 2])
            i += 1
        self.net = nl.net.newff(pr, [columns-1, 6, 1])
        err = self.net.train(self.input, self.output, epochs=300, show=20, goal=0.01)

    # method that returns output of the network using user's input
    def test(self, test_arr):
        return self.net.sim(test_arr)
