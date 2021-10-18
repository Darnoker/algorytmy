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
    iterat = 0
    iterat_y = 0
    iterat_x = 0
    for x1 in range(0, n):  # n
        for y1 in range(0, n): # n
            for x2 in range(n-1, x1-1, -1): # n/2 + 1/2
                

                for y2 in range(n-1, y1-1, -1):  # n/2 + 1/2
                    iterat_y = iterat_y + 1
                    local_max = 0
                    for x in range(x1, x2+1):
                        iterat = iterat + 1
                        for y in range(y1, y2+1):
                            local_max = local_max + matrix[x][y]
                    if local_max == (x2-x1+1)*(y2-y1+1) and local_max > max_:
                        max_ = local_max
    # print("n:",n,"-", iterat_y, iterat, "w:", iterat/iterat_y)
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
    for x1 in range(0, n):
        for y1 in range(0, n):
            for x2 in range(x1, n):
                for y2 in range(y1, n):
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
            for x2 in range(x1, n): # n/2 + 1/2
                product = product*matrix[x2][y]
                my_matrix[x1][x2] = product*(x2-x1+1+my_matrix[x1][x2])
                if my_matrix[x1][x2] > max_:
                    max_ = my_matrix[x1][x2]
    return max_


def sensible_algorithm(n, matrix):
    max_ = 0
    local_max = 0
    iterator = 0
    for x1 in range(0, n): # n
        for y1 in range(0, n): # n
            local_max = 0
            x2 = x1
            ymax = n - 1
            while x2 < n and matrix[x2][y1] == 1:
                iterator = iterator + 1
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
    starting_n = 100

    for n in range(starting_n, 1100, 100):
        macierz = create_random_matrix(n)
        start = time.perf_counter()
        x = sensible_algorithm(n, macierz)
        end = time.perf_counter()
        Tn = end - start
        Fn = n*n/1000
        print("n: %1d \ttime: %2.10f \tfactor: %2.10f" % (n,Tn,Fn/Tn))
        

# ALGORYTM NAIWNY Fn = n*n*(n/2 + 0.5)*(n/2 + 0.5)*((n+2)/3) *((n+2)/3)/10000

# n: 20   time: 0.2395376000      factor: 990.0742096439
# n: 21   time: 0.3126670000      factor: 1003.1250499733
# n: 22   time: 0.4059214000      factor: 1009.2042449597
# n: 23   time: 0.5191171000      factor: 1019.0379010824
# n: 24   time: 0.6313507000      factor: 1070.7202827208
# n: 25   time: 0.7917305000      factor: 1080.6233939453
# n: 26   time: 0.9608548000      factor: 1116.9404576009
# n: 27   time: 1.1756551000      factor: 1135.6830757592
# n: 28   time: 1.5072230000      factor: 1093.6404234808
# n: 29   time: 1.7340117000      factor: 1165.2184930471
# n: 30   time: 2.0888514000      factor: 1177.7573071976
# n: 31   time: 2.6360690000      factor: 1129.2548108566
# n: 32   time: 3.4043427000      factor: 1051.8405212260
# n: 33   time: 3.5621263000      factor: 1202.5689543911
# n: 34   time: 4.3063742000      factor: 1183.8172353903
# n: 35   time: 5.2269614000      factor: 1155.0286175827
# n: 36   time: 5.8592777000      factor: 1214.5882076898
# n: 37   time: 6.6735459000      factor: 1251.5283816359
# n: 38   time: 8.1277742000      factor: 1200.9979312663
# n: 39   time: 9.6032509000      factor: 1183.3034582071
# n: 40   time: 10.7593690000     factor: 1224.8896752217
# n: 41   time: 12.4862135000     factor: 1219.7475319479
# n: 42   time: 14.9064973000     factor: 1176.6918308837
# n: 43   time: 17.6259067000     factor: 1142.3871885127
# n: 44   time: 20.3916693000     factor: 1130.0320567674
# n: 45   time: 23.2121335000     factor: 1132.7102913655
# n: 46   time: 24.6074075000     factor: 1215.6974114400
# n: 47   time: 26.3961225000     factor: 1285.9607542737
# n: 48   time: 27.6806657000     factor: 1387.8278946160
# n: 49   time: 31.1040177000     factor: 1394.2913394111
# n: 50   time: 36.8257155000     factor: 1326.2742987302



# ALGORYTM DYNAMICZNY Fn = n*n*(n/2 + 0.5)/10000

# n: 50   time: 0.0161431000      factor: 394.9055633676
# n: 51   time: 0.0181187000      factor: 373.2386981406
# n: 52   time: 0.0177864000      factor: 402.8696082400
# n: 53   time: 0.0192942000      factor: 393.0870417017
# n: 54   time: 0.0207051000      factor: 387.2958836229
# n: 55   time: 0.0236465000      factor: 358.1925443512
# n: 56   time: 0.0245241000      factor: 364.4415085569
# n: 57   time: 0.0284681000      factor: 330.9704546492
# n: 58   time: 0.0268305000      factor: 369.8701105086
# n: 59   time: 0.0266794000      factor: 391.4255942787
# n: 60   time: 0.0284137000      factor: 386.4333050606
# n: 61   time: 0.0308492000      factor: 373.9189346887
# n: 62   time: 0.0299861000      factor: 403.8070972884
# n: 63   time: 0.0326208000      factor: 389.3466745144
# n: 64   time: 0.0350079000      factor: 380.2570276995
# n: 65   time: 0.0376765000      factor: 370.0582591270
# n: 66   time: 0.0378672000      factor: 385.3625301052
# n: 67   time: 0.0376222000      factor: 405.6806885296
# n: 68   time: 0.0413528000      factor: 385.7731519994
# n: 69   time: 0.0426017000      factor: 391.1463627038
# n: 70   time: 0.0462047000      factor: 376.4768519220
# n: 71   time: 0.0462316000      factor: 392.5367064951
# n: 72   time: 0.0466687000      factor: 405.4451913167
# n: 73   time: 0.0499008000      factor: 395.1299377966
# n: 74   time: 0.0508052000      factor: 404.1909095919
# n: 75   time: 0.0534792000      factor: 399.6881030382
# n: 76   time: 0.0544923000      factor: 408.0870141286
# n: 77   time: 0.0569459000      factor: 406.0538159903
# n: 78   time: 0.0592351000      factor: 405.7020246442
# n: 79   time: 0.0614113000      factor: 406.5049917523
# n: 80   time: 0.0627548000      factor: 413.0361342877
# n: 81   time: 0.0648427000      factor: 414.8516332602
# n: 82   time: 0.0683289000      factor: 408.3864953190
# n: 83   time: 0.0684030000      factor: 422.9902197272
# n: 84   time: 0.0749435000      factor: 400.1414398847
# n: 85   time: 0.0758101000      factor: 409.8068726990
# n: 86   time: 0.0766028000      factor: 419.9924806926
# n: 87   time: 0.0789735000      factor: 421.7060153089
# n: 88   time: 0.0822608000      factor: 418.9212845000
# n: 89   time: 0.0832515000      factor: 428.1544476676
# n: 90   time: 0.0854559000      factor: 431.2750787248
# n: 91   time: 0.0902514000      factor: 422.0721229809
# n: 92   time: 0.0941959000      factor: 417.8271028782
# n: 93   time: 0.0959292000      factor: 423.7531429429
# n: 94   time: 0.0967945000      factor: 433.6093476386
# n: 95   time: 0.1004027000      factor: 431.4625005104
# n: 96   time: 0.1028913000      factor: 434.4157377737
# n: 97   time: 0.1164018000      factor: 396.0772084280
# n: 98   time: 0.1127441000      factor: 421.6610891390
# n: 99   time: 0.1121708000      factor: 436.8784032921
# n: 100  time: 0.1203502000      factor: 419.6087750581
# n: 101  time: 0.1254894000      factor: 414.5776456019
# n: 102  time: 0.1298378000      factor: 412.6733509040
# n: 103  time: 0.1298957000      factor: 424.7007406712
# n: 104  time: 0.1291705000      factor: 439.6050181737
# n: 105  time: 0.1344694000      factor: 434.5412413531
# n: 106  time: 0.1591149000      factor: 377.7936572879
# n: 107  time: 0.1433248000      factor: 431.3600995780
# n: 108  time: 0.1494180000      factor: 425.4427177449
# n: 109  time: 0.1472338000      factor: 443.8213236363
# n: 110  time: 0.1547222000      factor: 434.0359689818
