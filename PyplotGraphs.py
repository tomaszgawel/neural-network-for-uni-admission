import matplotlib.pyplot as plt


def create_input_graphs(input, titles, quantity):
    temp_list = []
    k = 0
    while k < quantity - 1:
        for row in input:
            temp_list.append(row[k])
        plt.clf()
        plt.hist(temp_list, 50, facecolor="#27aae1")
        plt.title(titles[k])
        plt.xlabel("Result")
        plt.ylabel("Number of people")
        plt.savefig("graphs/"+str(k)+".png")
        temp_list = []
        k += 1
