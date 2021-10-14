import random
import time


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
    for x1 in range(0, n):
        for y1 in range(0, n):
            for x2 in reversed(range(n-1, x1)):
                for y2 in reversed(range(n-1, y1)):
                    local_max = 0
                    for x in range(x1, x2+1):
                        for y in range(y1, y2+1):
                            local_max += matrix[x][y]
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
    for x1 in range(0, n):
        for y1 in range(0, n):
            for x2 in range(x1, n):
                for y2 in range(y1, n):
                    local_max = recursion(matrix, x1, y1, x2, y2) * (x2-x1+1) * (y2-y1+1)
                    if local_max > max_:
                        max_ = local_max
    return max_


def dynamic_algorithm(n, matrix):
    max_ = 0
    my_matrix=create_matrix(n,0)
    for y in range(0, n):
        for x1 in range(0, n):
            product = 1
            for x2 in range(x1, n):
                product = product*matrix[x2][y]
                my_matrix[x1][x2] = product*(x2-x1+1+my_matrix[x1][x2])
                if my_matrix[x1][x2] > max_:
                    max_ = my_matrix[x1][x2]
    return max_


def sensible_algorithm(n, matrix):
    max_ = 0
    local_max = 0
    for x1 in range(0, n):
        for y1 in range(0, n):
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
    n = 20
    macierz = create_random_matrix(n)
    # read_matrix(macierz)

    for i in range(n, 100, 1):
        start = time.perf_counter()
        x = naive_algorithm(i, macierz)
        end = time.perf_counter()
        Tn = end - start
        Fn = i*i*i*i*i*i
        print("n: %1d \ttime: %2.10f \tfactor: %2.10f" % (i,Tn,Fn/Tn))
