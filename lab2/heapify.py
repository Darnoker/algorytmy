import math
import heapq

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



def IterativeHeapify(array, index, heapsize):
    flag = True
    while flag:
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
            index = largest
        else:
            flag = False


def buildHeap(array):
    arraylength = len(array) - 1
    heapsize = arraylength

    for i in range(math.floor(arraylength/2), -1 , -1):
        IterativeHeapify(array, i, heapsize)

def heapSort(array):
    buildHeap(array)
    heapsize = len(array) - 1
    array_length = len(array) - 1
    for i in range(array_length, 1, -1):
        temp = array[0]
        array[0] = array[heapsize]
        array[heapsize] = temp
        heapsize = heapsize - 1
        IterativeHeapify(array, 0, heapsize)

array = [2,6,3,3,4,5,7,8,6,9]
heapSort(array)
print(array)




