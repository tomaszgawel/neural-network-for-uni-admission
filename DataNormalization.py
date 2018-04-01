import math


class Data(object):
    # initialization of class
    def __init__(self,q):
        self.quantity_of_lines = 0
        self.columns_quantity = q
        self.avg = []
        self.standard_deviation = []
        i = 0
        while i < q:
            self.avg.append(0)
            self.standard_deviation.append(0)
            i += 1

    # calculating average of each column
    def calc_avg(self, list):
        for row in list:
            i = 0
            for item in row:
                self.avg[i] += item
                i += 1
            self.quantity_of_lines += 1
        i = 0
        while i < len(self.avg):
            self.avg[i] = self.avg[i] / float(self.quantity_of_lines)
            i += 1


    # calculating standard deviation of each column
    def calc_deviation(self, list):
        for row in list:
            i = 0
            for item in row:
                temp = math.pow((float(item) - self.avg[i]), 2)
                self.standard_deviation[i] = self.standard_deviation[i] + temp
                i += 1
                if i == self.columns_quantity - 1:
                    break
        i = 0
        while i < len(self.standard_deviation) - 1:
            self.standard_deviation[i] = math.sqrt(self.standard_deviation[i] / self.quantity_of_lines)
            i = i + 1


    # updating list of data with normalized one
    def normalize(self, list):
        for row in list:
            i = 0
            for item in row:
                row[i] = (float(row[i]) - self.avg[i]) / self.standard_deviation[i]
                i += 1
                if i == self.columns_quantity - 1:
                    break
