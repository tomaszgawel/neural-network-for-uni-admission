import math


class Data(object):
    # initialization of class
    def __init__(self):
        self.quantity_of_lines = 0
        self.avg = [0, 0, 0]
        self.standard_deviation = [0, 0, 0]

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


    # calculating standard deviation
    def calc_deviation(self, list):
        for row in list:
            i = 0
            for item in row:
                temp = math.pow((float(item) - self.avg[i]), 2)
                self.standard_deviation[i] = self.standard_deviation[i] + temp
                i += 1
                if i == 2:
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
                if i == 2:
                    break
