#include <iostream>
#include <string>
#include <fstream>
#include <vector>

using namespace std;

int convertToNumber(string text, int constant)
{

    int length = text.size();
    unsigned long long numberFromString = (int)text[0];
    for (size_t i = 1; i < length - 1; i++)
        numberFromString = (unsigned int)text[i] + constant * numberFromString;

    numberFromString = constant * numberFromString + (int)text[length - 1];

    if (numberFromString < 0)
    {
        numberFromString *= -1;
    }

    return numberFromString % 4294967296;
}

int h(unsigned long long num, int m)
{
    return num % m;
}

void printPrimes()
{

    string line;

    ifstream primeNumbers;
    primeNumbers.open("./pierwsze.txt");

    vector<int> primes;
    unsigned long long number;

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
        if (m - count == 0)
        {
            mean = 0;
        }
        else
        {
            mean = sum / (m - count);
        }
        printf("Prime: %d, zero: %d,  max: %d, mean: %d\n ", primes[index], count, max, mean);
    }
}

void printPowers()
{

    int constant = 3;

    for (size_t arraySize = 2; arraySize < 100000; arraySize *= 2)
    {
        string line;
        unsigned long long number;
        ifstream napisy;
        napisy.open("napisy.txt");
        int T[arraySize] = {0};

        if (napisy.is_open())
        {

            while (getline(napisy, line))
            {
                number = convertToNumber(line, constant);
                int key = h(number, arraySize);
                T[key]++;
            }
            napisy.close();
        }
        unsigned int count = 0;
        int max = T[0];
        int sum = 0;

        for (size_t i = 0; i < arraySize; i++)
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
        int mean;
        if (arraySize - count == 0)
        {
            mean = 0;
        }
        else
        {
            mean = sum / (arraySize - count);
        }
        printf("Power of two: %d, zero: %d,  max: %d, mean: %d\n ", arraySize, count, max, mean);
    }
}

int main()
{
   printPrimes();
    //printPowers();

    //    string s = "intercallability";
    //    unsigned  long number = convertToNumber(s, 3);
    //    if (number < 0) {
    //        number*=-1;
    //    }
    //    printf("%lu", number);
}
