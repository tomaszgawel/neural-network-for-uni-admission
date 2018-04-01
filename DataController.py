import csv
from random import shuffle


# loading data to a list
# it will help us to sort, shuffle and control data
# skipping not full data
def load_data_list(path, list, columns_n):
    temp = []
    with open(path) as csvfile:
        columns_names = True
        for row in csvfile:
            full_row = True
            size = len(row)
            if columns_names:
                row = row.split(",")
                for item in row:
                    columns_n.append(item)
                columns_names = False
                continue
            row = row.split(",")
            i = 0
            for items in row:
                if str(row[i]) == "":
                    full_row = False
                    break
                if i != size-1:
                    temp.append(float(row[i]))
                else:
                    temp.append(int(row[2]))
                i += 1
            if full_row:
                list.append(temp)
            temp = []
    csvfile.close()


# sorting specific column of the list of data
def sort(list, pos):
    return sorted(list, key=lambda x: x[pos])


# removing items in data that stand out too much using Tuckey's range test
# shuffling data for neural network
def clear_outliners(list, column_names):
    k = 0
    while k < len(column_names)-1:
        list = sort(list,k)
        q1 = list[int(1 * len(list) / 4)]
        q3 = list[int(3 * len(list) / 4)]
        irq = q3[k] - q1[k]
        sup = q3[k] + 1.5*irq
        inf = q1[k] - 1.5*irq
        for row in list:
            if row[k] > sup or row[k] < inf:
                list.remove(row)
        k = k+1
        shuffle(list)
    return list
