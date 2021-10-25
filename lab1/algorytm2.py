import random
import time
import math


def create_random_matrix(n: int) -> list:
    matrix = [[] for i in range(0, n)]
    for i in range(0, n):
        for j in range(0, n):
            matrix[i].append(random.randint(0, 1))
    return matrix


def create_matrix(n: int, value: int) -> list:
    matrix = [[] for i in range(0, n)]
    for i in range(0, n):
        for j in range(0, n):
            matrix[i].append(value)
    return matrix


def read_matrix(matrix):
    for row in matrix:
        print(row)


def naive_algorithm(n, matrix):
    max_ = 0
    local_max = 0
    for x1 in range(0, n):  # n
        for y1 in range(0, n): # n
            for x2 in range(n-1, x1-1, -1): # (n+1)/2
                for y2 in range(n-1, y1-1, -1):  # (n+1)/2
                    local_max = 0
                    for x in range(x1, x2+1): # (n+2) / 3
                        for y in range(y1, y2+1): # (n+2) / 3
                            local_max = local_max + matrix[x][y]
                    if local_max == (x2-x1+1)*(y2-y1+1) and local_max > max_:
                        max_ = local_max
    return max_


def recursion(matrix, x1, y1, x2, y2):
    if x2 == x1 and y2 == y1:
        return matrix[x1][y1]
    elif (x2-x1) > (y2-y1):
        return recursion(matrix, x1, y1, int((x1+x2)/2), y2) * recursion(matrix, int((x1+x2+1)/2), y1, x2, y2)
    else:
        return recursion(matrix, x1, y1, x2, int((y1+y2)/2)) * recursion(matrix, x1, int((y1+y2+1)/2), x2, y2)


def recurrent_algorithm(n, matrix):
    max_ = 0
    for x1 in range(0, n): # n
        for y1 in range(0, n): # n
            for x2 in range(x1, n): # (n+1)/2
                for y2 in range(y1, n): # (n+1)/2
                    local_max = recursion(
                        matrix, x1, y1, x2, y2) * (x2-x1+1) * (y2-y1+1)
                    if local_max > max_:
                        max_ = local_max
    return max_


def dynamic_algorithm(n, matrix):
    max_ = 0
    my_matrix = create_matrix(n, 0)
    for y in range(0, n): # n
        for x1 in range(0, n): # n
            product = 1
            for x2 in range(x1, n): # (n+1)/2
                product = product*matrix[x2][y]
                my_matrix[x1][x2] = product*(x2-x1+1+my_matrix[x1][x2])
                if my_matrix[x1][x2] > max_:
                    max_ = my_matrix[x1][x2]
    return max_


def sensible_algorithm(n, matrix):
    max_ = 0
    local_max = 0
    for x1 in range(0, n): # n
        for y1 in range(0, n): # n
            local_max = 0
            x2 = x1
            ymax = n - 1
            while x2 < n and matrix[x2][y1] == 1:
                y2 = y1
                while y2 < ymax+1 and matrix[x2][y2] == 1:
                    y2 += 1
                ymax = y2 - 1
                local_max = (x2-x1+1) * (ymax-y1+1)
                if local_max > max_:
                    max_ = local_max
                x2 += 1
    return max_


if __name__ == '__main__':
    starting_n = 20

    for n in range(starting_n, 36, 1):
        macierz = create_matrix(n,1)
        start = time.perf_counter()
        x = recurrent_algorithm(n, macierz)
        end = time.perf_counter()
        Tn = end - start
        Fn = n*n*n*n*n*math.log(n,2)/10000
        print("n: %1d \ttime: %2.10f \tfactor: %2.10f" % (n,Tn,Fn/Tn))
        

# ALGORYTM NAIWNY Fn = n*n*((n+1)/2)*((n+1)/2)*((n+2)/3)*((n+2)/3)/10000

# n: 20   time: 0.2395376000      factor: 990.0742096439
# n: 25   time: 0.7917305000      factor: 1080.6233939453
# n: 30   time: 2.0888514000      factor: 1177.7573071976
# n: 35   time: 5.2269614000      factor: 1155.0286175827
# n: 40   time: 10.7593690000     factor: 1224.8896752217
# n: 45   time: 23.2121335000     factor: 1132.7102913655
# n: 50   time: 36.8257155000     factor: 1326.2742987302


# ALGORYTM DYNAMICZNY Fn = n*n*((n+1)/2)/10000

# n: 50   time: 0.0161431000      factor: 394.9055633676
# n: 60   time: 0.0284137000      factor: 386.4333050606
# n: 70   time: 0.0462047000      factor: 376.4768519220
# n: 80   time: 0.0627548000      factor: 413.0361342877
# n: 90   time: 0.0854559000      factor: 431.2750787248
# n: 100  time: 0.1203502000      factor: 419.6087750581
# n: 110  time: 0.1547222000      factor: 434.0359689818


# ALGORYTM CZUŁY Fn = n*n/10000

# n: 50   time: 0.0013879000      factor: 180.1282513149
# n: 60   time: 0.0026095000      factor: 137.9574631155
# n: 70   time: 0.0037309000      factor: 131.3356026696
# n: 80   time: 0.0046337000      factor: 138.1185661566
# n: 90   time: 0.0057875000      factor: 139.9568034557
# n: 100  time: 0.0059164000      factor: 169.0217023866
# n: 110  time: 0.0081245000      factor: 148.9322419841
# n: 120  time: 0.0096282000      factor: 149.5606655450

# ALGORYTM REKURENCYJNY Fn = n*n*n*n*n*math.log(n,2)/10000

# n: 20   time: 2.7650474000      factor: 500.1784021366
# n: 21   time: 3.7281835000      factor: 481.1637618880
# n: 22   time: 4.4396816000      factor: 517.6558042275
# n: 23   time: 6.3228898000      factor: 460.4729364560
# n: 24   time: 8.8220754000      factor: 413.8292951718
# n: 25   time: 10.6738825000     factor: 424.8703140893
# n: 26   time: 12.9737616000     factor: 430.4664551302
# n: 27   time: 15.1150487000     factor: 451.3874875177
# n: 28   time: 19.7967348000     factor: 417.9292603103
# n: 29   time: 22.9576229000     factor: 434.0291347421
# n: 30   time: 30.8179716000     factor: 386.9087914705
# n: 31   time: 38.3557172000     factor: 369.7869434018
# n: 32   time: 46.2922067000     factor: 362.4198800616
# n: 33   time: 51.6657020000     factor: 382.0994173426
# n: 34   time: 60.1414538000     factor: 384.3455997009
# n: 35   time: 68.3248902000     factor: 394.2919786143

# ALGORYTM NAIWNY ( 0 )  Fn = n*n*((n+1)/2)*((n+1)/2)*((n+2)/3)*((n+2)/3)/10000  Wartość oszacowania zwiększyła się

# n: 20   time: 0.2193619000      factor: 1081.1357852024
# n: 25   time: 0.6917286000      factor: 1236.8470813553
# n: 30   time: 1.8297293000      factor: 1344.5486171096
# n: 35   time: 4.2753436000      factor: 1412.1180809889
# n: 40   time: 8.9460667000      factor: 1473.1658551126
# n: 45   time: 16.9420746000     factor: 1551.9128041143
# n: 50   time: 31.3141908000     factor: 1559.7081946630

# ALGORYTM DYNAMICZNY ( 0 ) Fn = n*n*((n+1)/2)/10000 Wartosć oszacowania zwiększyła się nie wiele.

# n: 50   time: 0.0133991000      factor: 475.7782239106
# n: 60   time: 0.0310902000      factor: 353.1659493988
# n: 70   time: 0.0401688000      factor: 433.0475393838
# n: 80   time: 0.0576669000      factor: 449.4779500892
# n: 90   time: 0.0821045000      factor: 448.8791722744
# n: 100  time: 0.1062454000      factor: 475.3146959774
# n: 110  time: 0.1387443000      factor: 484.0198840601


# ALGORYTM CZUŁY ( 0 ) Fn = n*n/10000 Wartości oszacowania zmniejszyły się

# n: 50   time: 0.0002139000      factor: 1168.7704534830
# n: 60   time: 0.0003516000      factor: 1023.8907849829
# n: 70   time: 0.0005905000      factor: 829.8052497883
# n: 80   time: 0.0006237000      factor: 1026.1343594677
# n: 90   time: 0.0007482000      factor: 1082.5982357658
# n: 100  time: 0.0010638000      factor: 940.0263207370
# n: 110  time: 0.0010851000      factor: 1115.1045986545
# n: 120  time: 0.0021460000      factor: 671.0158434296

# ALGORYTM REKURENCYJNY ( 0 ) Fn = n*n*n*n*n*math.log(n,2)/10000 Wartości zwiększone odrobine

# n: 20   time: 2.3052652000      factor: 599.9383456463
# n: 21   time: 3.0573268000      factor: 586.7435557981
# n: 22   time: 4.0567569000      factor: 566.5182819217
# n: 23   time: 5.4538547000      factor: 533.8462047941
# n: 24   time: 6.8538652000      factor: 532.6677922896
# n: 25   time: 8.6181541000      factor: 526.2166071418
# n: 26   time: 10.9936131000     factor: 508.0012471657
# n: 27   time: 13.6513624000     factor: 499.7848314686
# n: 28   time: 16.9244848000     factor: 488.8559285138
# n: 29   time: 21.4518757000     factor: 464.4944499200
# n: 30   time: 26.6647349000     factor: 447.1727992814
# n: 31   time: 31.0586548000     factor: 456.6663790401
# n: 32   time: 36.0343760000     factor: 465.5891918317
# n: 33   time: 45.2521789000     factor: 436.2537917660
# n: 34   time: 51.9226659000     factor: 445.1832880107
# n: 35   time: 59.5054041000     factor: 452.7312527832

# ALGORYTM NAIWNY ( 1 ) Fn = n*n*((n+1)/2)*((n+1)/2)*((n+2)/3)*((n+2)/3)/10000 Wartości oszacowania nie zmieniły się

# n: 20   time: 0.2513450000      factor: 943.5636276831
# n: 25   time: 0.7250713000      factor: 1179.9701629343
# n: 30   time: 1.9686832000      factor: 1249.6474801024
# n: 35   time: 4.8479509000      factor: 1245.3282066037
# n: 40   time: 10.2186794000     factor: 1289.7008981415
# n: 45   time: 18.7790935000     factor: 1400.1007290368
# n: 50   time: 34.5301577000     factor: 1414.4447420233


# ALGORYTM DYNAMICZNY ( 1 ) Fn = n*n*((n+1)/2)/10000 Wartosć oszacowania zmniejszyła się nie wiele.

# n: 50   time: 0.0176044000      factor: 362.1253777465
# n: 60   time: 0.0369708000      factor: 296.9911389529
# n: 70   time: 0.0631843000      factor: 275.3057325950
# n: 80   time: 0.0741543000      factor: 349.5414291552
# n: 90   time: 0.0968681000      factor: 380.4658086615
# n: 100  time: 0.1467586000      factor: 344.1024921197
# n: 110  time: 0.1702669000      factor: 394.4101877699


# ALGORYTM CZUŁY ( 1 ) Fn = n*n/10000 Wartość zmalała drastycznie, czas algorytmu wydłużył się.

# n: 50   time: 0.1599636000      factor: 1.5628555496
# n: 60   time: 0.3509128000      factor: 1.0258958921
# n: 70   time: 0.6478616000      factor: 0.7563343776
# n: 80   time: 1.0800879000      factor: 0.5925443661
# n: 90   time: 1.6959551000      factor: 0.4776069838
# n: 100  time: 2.5243813000      factor: 0.3961366692
# n: 110  time: 3.4876029000      factor: 0.3469431683
# n: 120  time: 5.3049694000      factor: 0.2714436015

# ALGORYTM REKURENCYJNY ( 1 ) Fn = n*n*n*n*n*math.log(n,2)/10000 Wartości nie uległy większej zmianie.

# n: 25   time: 9.3320247000      factor: 485.9626882821
# n: 26   time: 12.4269711000     factor: 449.4071098030
# n: 27   time: 15.7944543000     factor: 431.9708504523
# n: 28   time: 18.6240249000     factor: 444.2452571851
# n: 29   time: 25.6705370000     factor: 388.1600608130
# n: 30   time: 29.9698721000     factor: 397.8576921364
# n: 31   time: 32.0433873000     factor: 442.6324624354
# n: 32   time: 38.6614494000     factor: 433.9520700949
# n: 33   time: 44.5752887000     factor: 442.8784469274
# n: 34   time: 57.4505786000     factor: 402.3476123467
# n: 35   time: 64.1021758000     factor: 420.2658616396
