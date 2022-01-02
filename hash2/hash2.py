from re import split

class hashStructure:
    def __init__(self, count, surname):
        self.count = count
        self.surname = surname


def h(key, modulo):
    return key % modulo


def H(key, i, modulo):
    return (h(key,modulo) + i) % modulo


def convertToNumber(text, constant) -> int:
    length = len(text)
    numberFromString = ord(text[0])
    for i in range(1, length - 1):
        numberFromString = ord(text[i]) + constant * numberFromString

    numberFromString = constant * numberFromString + ord(text[length - 1])
    return numberFromString



# main

m = 4
hashList = [None]*m
with open("nazwiska.txt") as f:
    for row in f:
        surname = row.split(" ")
        surname = surname[-1]
        surname = surname[:-1]

        hashStruct = hashStructure(0, surname)
        value = convertToNumber(surname, 3)

        for i in range(m):
            val = H(value, i, m)
            if hashList[val] is None:
                hashList[val] = hashStruct
                break
            else:
                hashList[val].count += 1

for i in range(len(hashList)):
    if hashList[val] is not None:
        print(hashList[val].count)





