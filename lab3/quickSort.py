import random
import time
import sys
sys.setrecursionlimit(50000)

def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1

        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j + 1] = key

def insertionSort__desc(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1

        while j >= 0 and key > array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j + 1] = key




def partition(array, p, r):
    partition_element = array[r]
    i = p - 1

    for j in range(p,r+1):
        if array[j] <= partition_element:
            i = i + 1
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
    if i<r:
        return i
    else:
        return i - 1

def quickSortModified(array, p, r, c):
    if p + c<r:
        q = partition(array, p , r)
        quickSortModified(array, p, q, c)
        quickSortModified(array, q+1, r, c)

def quickSort(array, p, r):
    if p<r:
        q = partition(array, p , r)
        quickSort(array, p, q)
        quickSort(array, q+1, r)



# for n in range(1000, 97000, 2000):
#     array = []
#     flag = True
    
#     for i in range(n):
#         array.append(random.randint(0,1001))

#     start = time.perf_counter()
#     quickSort(array, 0 , len(array) - 1)
#     end = time.perf_counter()
#     timeElapsed = end - start
#     print("n: %1d \ttime: %2.10f" % (n, timeElapsed))


for n in range(1000, 97000, 2000):
    array = []
    flag = True
    
    for i in range(n):
        array.append(random.randint(0,1001))
    insertionSort__desc(array)
    start = time.perf_counter()
    quickSort(array, 0 , len(array) - 1)
    end = time.perf_counter()
    timeElapsed = end - start
    print("n: %1d \ttime: %2.10f" % (n, timeElapsed))


    # for i in range(0, len(array)-1):
    #     if array[i] > array[i+1]:
    #         print("ZLE!!!")
    #         flag = False
    #         break
    # if flag:
    #     print("POSORTOWANE!!!")


# WARTOSCI LOSOWE --- QUICKSORT NORMALNY

# n: 1000         time: 0.0047372000      
# n: 3000         time: 0.0207210000
# n: 5000         time: 0.0348198000
# n: 7000         time: 0.0572750000
# n: 9000         time: 0.0712465000
# n: 11000        time: 0.0770084000
# n: 13000        time: 0.1184848000
# n: 15000        time: 0.1472085000
# n: 17000        time: 0.1828012000
# n: 19000        time: 0.1928578000
# n: 21000        time: 0.2118892000
# n: 23000        time: 0.2443748000
# n: 25000        time: 0.2178280000
# n: 27000        time: 0.2939816000
# n: 29000        time: 0.2963727000
# n: 31000        time: 0.3056223000
# n: 33000        time: 0.3117778000
# n: 35000        time: 0.3462323000
# n: 37000        time: 0.3600484000
# n: 39000        time: 0.4273720000
# n: 41000        time: 0.5082267000
# n: 43000        time: 0.4587217000
# n: 45000        time: 0.5392993000
# n: 47000        time: 0.5398878000
# n: 49000        time: 0.6084368000
# n: 51000        time: 0.7566847000
# n: 53000        time: 0.8090041000
# n: 55000        time: 0.8418515000
# n: 57000        time: 0.8421982000
# n: 59000        time: 0.7584930000
# n: 61000        time: 0.8355577000
# n: 63000        time: 0.8661151000
# n: 65000        time: 0.8550830000
# n: 67000        time: 0.9603031000
# n: 69000        time: 0.9710779000
# n: 71000        time: 1.1051902000
# n: 73000        time: 1.0617699000
# n: 75000        time: 1.1579514000
# n: 77000        time: 1.1596250000
# n: 79000        time: 1.1914103000
# n: 81000        time: 1.2137445000
# n: 83000        time: 1.2967023000
# n: 85000        time: 1.6305914000
# n: 87000        time: 1.4671541000
# n: 89000        time: 1.6355332000
# n: 91000        time: 1.8983558000
# n: 93000        time: 1.7135441000
# n: 95000        time: 1.8507459000

# WARTOŚCI LOSOWE --- QUICKSORT ZMODYFIKOWANY
# n: 1000         time: 0.0061274000
# n: 3000         time: 0.0169511000
# n: 5000         time: 0.0291312000
# n: 7000         time: 0.0410995000
# n: 9000         time: 0.0542136000
# n: 11000        time: 0.0661670000
# n: 13000        time: 0.0783200000
# n: 15000        time: 0.0884439000
# n: 17000        time: 0.1068893000
# n: 19000        time: 0.1237544000
# n: 21000        time: 0.1190097000
# n: 23000        time: 0.1320051000
# n: 25000        time: 0.1339326000
# n: 27000        time: 0.1571298000
# n: 29000        time: 0.1606354000
# n: 31000        time: 0.1884420000
# n: 33000        time: 0.1658900000
# n: 35000        time: 0.1859972000
# n: 37000        time: 0.2127205000
# n: 39000        time: 0.2123857000
# n: 41000        time: 0.2222726000
# n: 43000        time: 0.2493411000
# n: 45000        time: 0.2555687000
# n: 47000        time: 0.2338322000
# n: 49000        time: 0.2518408000
# n: 51000        time: 0.2439962000
# n: 53000        time: 0.2407833000
# n: 55000        time: 0.2404226000
# n: 57000        time: 0.2599131000
# n: 59000        time: 0.2515338000
# n: 61000        time: 0.3052480000
# n: 63000        time: 0.2793207000
# n: 65000        time: 0.2880571000
# n: 67000        time: 0.3081252000
# n: 69000        time: 0.3026281000
# n: 71000        time: 0.3221743000
# n: 73000        time: 0.3139365000
# n: 75000        time: 0.3457785000
# n: 77000        time: 0.3663756000
# n: 79000        time: 0.3438824000
# n: 81000        time: 0.3481167000
# n: 83000        time: 0.3510895000
# n: 85000        time: 0.3753278000
# n: 87000        time: 0.4296606000
# n: 89000        time: 0.4137193000
# n: 91000        time: 0.4225715000
# n: 93000        time: 0.4122823000
# n: 95000        time: 0.5149074000