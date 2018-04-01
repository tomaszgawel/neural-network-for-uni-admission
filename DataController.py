import csv
from random import shuffle


def load_data_list(path, list):
    with open(path) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        columns_names = True
        for row in csvfile:
            if columns_names:
                columns_names = False
                continue
            row = row.split(",")
            list.append([float(row[0]), float(row[1]), int(row[2])])
    csvfile.close()


def shuffle_list(list):
    shuffle(list)


def sort(list, pos):
    return sorted(list, key=lambda x: x[pos])


