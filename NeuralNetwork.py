import neurolab as nl
import numpy as np


class NeuralNet(object):
    def __init__(self,input,output):
        self.input = np.array(input)
        self.output = np.array(output)
        self.net = None

    def create_and_train_nn(self, columns):
        i = 0
        pr = []
        while i < columns - 1:
            pr.append([-5, 5])
            i += 1
        self.net = nl.net.newff(pr, [columns-1, 6, 1])
        err = self.net.train(self.input, self.output, show=1)

    def test(self, test_arr):
        return self.net.sim(test_arr)
