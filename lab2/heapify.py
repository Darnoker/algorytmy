import math
import heapq

def heapify(list_, index, heapsize):
    largest = int()
    left_child_index = 2*index
    right_child_index = 2*index + 1

    if left_child_index <= heapsize and list_[left_child_index] > list_[index]:
        largest = left_child_index
    else:
        largest = index

    if right_child_index <= heapsize and list_[right_child_index] > list_[index]:
        largest = right_child_index

    if largest != index:
        temp = list_[index]
        list_[index] = list_[largest]
        list_[largest] = temp

        heapify(list_, largest, heapsize)

def buildHeap(list_):
    list_length = len(list_) - 1
    heapsize = list_length

    for i in range(math.floor(list_length/2), -1 , -1):
        heapify(list_, i, heapsize)




array = [1,2,3,4,5,6]
array2 = array
print(len(array))

buildHeap(array)

print(array)

heapq.heapify(array2)
print(array2)


