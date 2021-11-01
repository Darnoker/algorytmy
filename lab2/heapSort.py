import math
import heapq
from os import write

def heapify(array, index, heapsize):
    largest = int()
    left_child_index = 2*index + 1
    right_child_index = 2*index + 2

    if left_child_index <= heapsize and array[left_child_index] > array[index]:
        largest = left_child_index
    else:
        largest = index

    if right_child_index <= heapsize and array[right_child_index] > array[largest]:
        largest = right_child_index

    if largest != index:
        temp = array[index]
        array[index] = array[largest]
        array[largest] = temp

        heapify(array, largest, heapsize)



# def IterativeHeapify(array, index, heapsize):
#     flag = True
#     while flag:
#         largest = int()
#         left_child_index = 2*index + 1
#         right_child_index = 2*index + 2

#         if left_child_index <= heapsize and array[left_child_index] > array[index]:
#             largest = left_child_index
#         else:
#             largest = index

#         if right_child_index <= heapsize and array[right_child_index] > array[largest]:
#             largest = right_child_index

#         if largest != index:
#             temp = array[index]
#             array[index] = array[largest]
#             array[largest] = temp
#             index = largest
#         else:
#             flag = False


def IterativeHeapify(array, index, heapsize):
    largest = heapsize + 1
    while index != largest:
        left_child_index = 2*index + 1
        right_child_index = 2*index + 2

        if left_child_index <= heapsize and array[left_child_index] > array[index]:
            largest = left_child_index
        else:
            largest = index

        if right_child_index <= heapsize and array[right_child_index] > array[largest]:
            largest = right_child_index
            
        if largest != index:
            temp = array[index]
            array[index] = array[largest]
            array[largest] = temp
            index = largest
            largest = heapsize + 1


def buildHeap(array):
    arraylength = len(array) - 1
    heapsize = arraylength

    for i in range(math.floor(arraylength/2), -1 , -1):
        IterativeHeapify(array, i, heapsize)

def heapSort(array):
    buildHeap(array)
    heapsize = len(array) - 1
    array_length = len(array) - 1
    for i in range(array_length, 0, -1):
        temp = array[0]
        array[0] = array[heapsize]
        array[heapsize] = temp
        heapsize = heapsize - 1
        IterativeHeapify(array, 0, heapsize)


read_file = open("liczby-2.txt", "r")
write_file = open("wynik-2.txt", "w")
array = []


while(r := read_file.readline()):
    array.append(int(r))
heapSort(array)
write_file.write(str(array))
write_file.write("\n")

read_file.close()
write_file.close()



# read_file = open("liczby.txt", "r")
# write_file = open("wynik.txt", "w")

# while(r := read_file.readline()):
#     split = r.split(' ')
#     array = []
#     for i in range(len(split)):
#         array.append(int(split[i]))
#     heapSort(array)
#     write_file.write(str(array))
#     write_file.write("\n")

# read_file.close()
# write_file.close()
    





