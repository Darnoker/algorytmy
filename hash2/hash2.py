from re import split


class hashStructure:
    def __init__(self, count, surname):
        self.count = count
        self.surname = surname


def h(key, modulo):
    return key % modulo


def H(key, i, modulo):
    return (h(key, modulo) + i) % modulo


def convertToNumber(text, constant) -> int:
    length = len(text)
    numberFromString = ord(text[0])
    for i in range(1, length - 1):
        numberFromString = ord(text[i]) + constant * numberFromString

    numberFromString = constant * numberFromString + ord(text[length - 1])
    return numberFromString


def insertHash(value, m, hashList, hashStruct):
    for i in range(m):
        val = H(value, i, m)
        if hashList[val] is None:
            hashList[val] = hashStruct
            return True
        else:
            hashList[val].count += 1

    return False


def findHash(key, m, hashList, c):
    count = 0
    for i in range(m):
        val = convertToNumber(key, c)
        val = H(val, i, m)
        count += 1
        if hashList[val] is not None:
            dupa = hashList[val].surname
            if hashList[val].surname == key:
                print("Liczba prób dla klucza:", key, ":", count)
                return True

    print("Liczba prób dla klucza:", key, ":", count)
    return False


# main

m = 2001
c = 3
size = 0
eigthSize = int(m * 0.8)
hashList = [None] * m
surnameList = []
with open("nazwiska.txt") as f:
    for row in f:
        if size >= eigthSize:
            break
        surname = row.split(" ")
        surname = surname[-1]
        surname = surname[:-1]

        surnameList.append(surname)

        hashStruct = hashStructure(0, surname)
        value = convertToNumber(surname, c)

        if insertHash(value, m, hashList, hashStruct):
            size += 1



for surname in surnameList:
    findHash(surname, m, hashList, c)



