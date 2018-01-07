# Created by M Tafaquh Fiddin Al Islami
# 2110151035 | 3 D4 IT B 2017
# Politeknik Elektronika Negeri Surabaya

# Neural Network Single-Layer Perceptron

from operator import attrgetter
import random
import math
import csv
import struct
import matplotlib
import matplotlib.pyplot as plt
import copy

list_data = []

def main():
    #loadData()

    list_data.append([9, 8, 0])
    list_data.append([8, 7, 0])
    list_data.append([7, 7, 0])
    list_data.append([7, 4, 0])
    list_data.append([3, 4, 1])
    list_data.append([1, 4, 1])
    list_data.append([2, 3, 1])


    weight = []
    for i in range(0, len(list_data[0])):
        weight.append(round(random.uniform(-1, 1), 2))
    print(weight)

    errorFlag = True
    bayes = 1
    errorVal = 1

    lr = round(random.uniform(0, 1), 2)
    epoch = 0
    while (errorVal != 0):


        print("epoch ke-", epoch)
        for i in range(0, len(list_data)):
            sumPropWeight = 0
            for j in range(0, len(weight)-2):
                sumPropWeight += (list_data[i][j] * weight[j])

            sumPropWeight += (bayes * weight[len(weight)-1] )

            if(sumPropWeight > 0): output = 1
            else: output = 0

            errorVal = list_data[i][len(list_data[i])-1] - output

            print(errorVal)

            if(errorVal != 0):
                for k in range(0, len(weight)-2):
                    weight[k] = weight[k] + (lr * list_data[i][k] * errorVal)
                weight[len(weight)-1] = weight[len(weight)-1] + (lr * bayes * errorVal)
                break
        epoch += 1

    print(weight)

    #Testing Goes Here
    testing = [[1, 2], [5, 5], [7, 6], [7, 7]]

    print("Data Testing       label      sumPropWeight")
    for i in range(0, len(testing)):
        sumPropWeight = 0
        for j in range(0, len(weight) - 2):
            sumPropWeight += (testing[i][j] * weight[j])

        sumPropWeight += (bayes * weight[len(weight) - 1])

        if (sumPropWeight > 0):
            output = 1
        else:
            output = 0
        print(testing[i], output, sumPropWeight)

if __name__ == '__main__':
    main()
