import csv
import math

class Data(object):
    # initialization of class
    def __init__(self,path):
        self.path = path
        self.quantity_of_lines = 0
        self.sum_of_csv = [0, 0, 0]
        self.avg = [0, 0, 0]
        self.standard_deviation = [0, 0, 0]
        self.row_name = []

    # opening .csv data and calculating a sum of the data
    # preparing to calculate average and deviation
    def open_csv_file(self):
        with open(self.path) as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            columns_names = True
            for row in csvreader:
                i = 0
                for item in row:
                    if columns_names:
                        self.row_name.append(item)
                        i += 1
                        if i == 3:
                            columns_names = False
                            break
                    else:
                        row[i] = float(row[i])
                        self.sum_of_csv[i] = self.sum_of_csv[i] + float(row[i])
                        i = i + 1
                        self.quantity_of_lines += 1
                        if i == 2:
                            break
        csvfile.close()


    # calculating average and standard deviation
    def calc_avg_and_deviation(self):
        i = 0
        while i < len(self.avg):
            self.avg[i] = self.avg[i] / float(self.quantity_of_lines)
            i += 1

        i = 0
        with open(self.path) as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            columns_names = True
            for row in csvreader:
                if columns_names:
                    columns_names = False
                    continue
                for item in row:
                    temp = math.pow((float(item) - self.avg[i]), 2)
                    self.standard_deviation[i] = self.standard_deviation[i] + temp
                    i = i + 1
                    if i == 2:
                        break
                i = 0
        csvfile.close()
        i = 0
        while i < len(self.standard_deviation)-1:
            self.standard_deviation[i] = math.sqrt(self.standard_deviation[i]/self.quantity_of_lines)
            i = i + 1


    # creating new .csv file with normalized data
    def normalize(self,n_path):
        with open(self.path) as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            with open(n_path, 'w', newline='\n') as newcsvfile:
                csvwriter = csv.writer(newcsvfile, delimiter=',', quoting=csv.QUOTE_ALL)
                csvwriter.writerow(self.row_name)
                columns_names = True
                for row in csvfile:
                    if columns_names:
                        columns_names = False
                        continue
                    row = row.split(",")
                    csvwriter.writerow([(round(float(row[0]), 4) - self.avg[0]) / self.standard_deviation[0],
                                 (float(row[1]) - self.avg[1]) / self.standard_deviation[1], int(row[2])])
            newcsvfile.close()
        csvfile.close()