#include <iostream>
#include <string>
#include <fstream>
#include <vector>

using namespace std;

int convertToNumber(string text, int C)
{

    int length = text.size();
    int numberFromString = (int)text[0];
    for (size_t i = 1; i < length - 1; i++)
        numberFromString = (int)text[i] + C * numberFromString;

    numberFromString = C * numberFromString + (int)text[length - 1];

    return numberFromString;
}

int h(int num, int m)
{
    return num % m;
}


void printPrimes()
{

    string line;

    ifstream primeNumbers;
    primeNumbers.open("pierwsze.txt");

    vector<int> primes;
    int number;

    if (primeNumbers.is_open())
    {
        while (primeNumbers >> number && number < 3761)
        {
            primes.push_back(number);
        }
        primeNumbers.close();
    }

    for (size_t index = 0; index < primes.size(); index++)
    {
        ifstream napisy;
        napisy.open("napisy.txt");
        int m = primes[index];
        int T[m] = {0};

        if (napisy.is_open())
        {
            while (getline(napisy, line))
            {
                number = convertToNumber(line, 3);
                int key = h(number, m);
                T[key]++;
            }
            napisy.close();
        }
        unsigned int count = 0;
        int max = T[0];
        int sum = 0;

        for (size_t i = 0; i < m; i++)
        {
            // printf("%d ", T[i]);
            if (T[i] == 0)
            {
                count++;
            }
            if (T[i] > max)
            {
                max = T[i];
            }
            if (T[i] != 0)
            {
                sum += T[i];
            }
        }
        int mean = sum / (m - count);
        printf("\nPrime: %d, zero: %d,  max: %d, mean: %d\n ", primes[index], count, max, mean);
    }
}


void printPowers() {

    string line;
    int number;

    for (size_t index = 2; index < 10000; index*=2)
    {
        ifstream napisy;
        napisy.open("napisy.txt");
        int m = index;
        int T[m] = {0};

        if (napisy.is_open())
        {
            while (getline(napisy, line))
            {
                number = convertToNumber(line, 3);
                int key = h(number, m);
                T[key]++;
            }
            napisy.close();
        }
        unsigned int count = 0;
        int max = T[0];
        int sum = 0;

        for (size_t i = 0; i < m; i++)
        {
            // printf("%d ", T[i]);
            if (T[i] == 0)
            {
                count++;
            }
            if (T[i] > max)
            {
                max = T[i];
            }
            if (T[i] != 0)
            {
                sum += T[i];
            }
        }
        int mean = sum / (m - count);
        printf("\nPower of two: %d, zero: %d,  max: %d, mean: %d\n ", index, count, max, mean);
    }

}


int main()
{
    // printPrimes();
    printPowers();

}