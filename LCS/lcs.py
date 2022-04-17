# Funkcja znajdująca wszystkie najdłuższe podciągi
def LCS(first, second, first_len, second_len, table):

    # jeśli dotarlismy do samego końca (do 0 w tabelce)
    if first_len == 0 or second_len == 0:
        # tworzymy listę z pustym ciągiem
        return ['']

    # jeśli ostatni znak się ze sobą zgadza
    if first[first_len - 1] == second[second_len - 1]:

        # wywołanie rekurencyjne dla obu ciągów pomniejszonych o 1
        lcs = LCS(first, second, first_len - 1, second_len - 1, table)

        # dodajemy znak który jest zgodny z przejściem w tabelce
        for i in range(len(lcs)):
            lcs[i] = lcs[i] + (first[first_len - 1])

        return lcs


    # jeśli komórka wyzej od aktualnej ma wiekszą wartośc, przejdź do tej wyżej
    # zmniejszając długość pierwszego ciągu
    if table[first_len - 1][second_len] > table[first_len][second_len - 1]:
        return LCS(first, second, first_len - 1, second_len, table)

    # jeśli komórka po lewej od aktualnej ma wiekszą wartośc, przejdź do tej po lewej,
    # zmniejszając długość drugiego ciągu
    if table[first_len][second_len - 1] > table[first_len - 1][second_len]:
        return LCS(first, second, first_len, second_len - 1, table)
    
    # jeśli komórki po lewej i prawej są sobie równe, rozpatrz oba przypadki
    top = LCS(first, second, first_len - 1, second_len, table)
    left = LCS(first, second, first_len, second_len - 1, table)

    # połącz dwie listy i je zwróć
    return top + left


# funkcja do wypełnienia tabeli
def LCSLength(first, second, table):

    # wypełnianie tabeli iteracyjnie
    for i in range(1, len(first) + 1):
        for j in range(1, len(second) + 1):
            # jeśli znaki są równe
            if first[i - 1] == second[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1

            # jeśli nie są ze sobą równe
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])

# Funkcja do szukania NWP
def findLCS(first, second):

    # tabela wypełniona długościami podciągów
    table = [[0 for x in range(len(second) + 1)] for y in range(len(first) + 1)]

    # wypełniamy tabele
    LCSLength(first, second, table)

    # szukamy wszystkich najdłuższych wspólnych podciągów
    lcs = LCS(first, second, len(first), len(second), table)

    # nie może być duplikatów, więc tworzymy z tego zbiór
    return set(lcs)


if __name__ == '__main__':

    first = 'AABBCC'
    second = 'ABACB'

    lcs = findLCS(first, second)
    print(lcs)
