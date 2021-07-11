#define a bubble sort which will sort the largest  number at end
from time import time

list = [75,86,70,88,62,87,69,77,109]

#list = [1,2,3,4]


def bubble_sort(list):
    '''bubble sorting with async list'''
    for j in range(len(list)-1):
        count = 0
        for i in range(len(list)-1-j):

            if list[i] > list[i+1]:
                list[i],list[i+1] = list[i+1],list[i]
                count += 1
        if count == 0:

            return list



    return list



print(list)

bubble_sort(list)

print(list)



