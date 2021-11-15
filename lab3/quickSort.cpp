#include <iostream>
#include <time.h>
#include <vector>
#include <chrono>
using namespace std;

void insertionSort(vector<int> &array)
{
    for (size_t i = 1; i < array.size(); i++)
    {
        int key = array[i];
        int j = i - 1;

        while (j >= 0 && key < array[j])
        {
            array[j + 1] = array[j];
            j -= 1;
        }
        array[j + 1] = key;
    }
}
void insertionSort_desc(vector<int> &array)
{
    for (size_t i = 1; i < array.size(); i++)
    {
        int key = array[i];
        int j = i - 1;

        while (j >= 0 && key > array[j])
        {
            array[j + 1] = array[j];
            j -= 1;
        }
        array[j + 1] = key;
    }
}

int partition(vector<int> &array, int p, int r)
{
    int partitonElement = array[r];
    int i = p - 1;

    for (size_t j = p; j < r + 1; j++)
    {
        if (array[j] <= partitonElement)
        {
            i += 1;
            int temp = array[i];
            array[i] = array[j];
            array[j] = temp;
        }
    }
    if (i < r)
        return i;
    else
        return i - 1;
}

void quickSort(vector<int> &array, int p, int r)
{
    if (p < r)
    {
        int q = partition(array, p, r);
        quickSort(array, p, q);
        quickSort(array, q + 1, r);
    }
}

void quickSortModified(vector<int> &array, int p, int r, int c)
{
    if (p + c < r)
    {
        int q = partition(array, p, r);
        quickSortModified(array, p, q, c);
        quickSortModified(array, q + 1, r, c);
    }
}

void compareRandom()
{
    vector<int> array;

    for (size_t n = 1000; n < 100000; n += 2000)
    {
        for (size_t i = 0; i < n; i++)
        {
            array.push_back(rand() % 1001);
        }

        auto firstArray = array;
        auto secondArray = array;

        auto startFirst = chrono::high_resolution_clock::now();
        quickSort(firstArray, 0, firstArray.size() - 1);
        auto endFirst = chrono::high_resolution_clock::now();
        chrono::duration<double> elapsedFirst = endFirst - startFirst;

        auto startSecond = chrono::high_resolution_clock::now();
        quickSortModified(secondArray, 0, secondArray.size() - 1, 100);
        insertionSort(array);
        auto endSecond = chrono::high_resolution_clock::now();
        chrono::duration<double> elapsedSecond = endSecond - startSecond;

        printf("n: %6d\t time normal: %2.10f\t time modified: %2.10f\n", n, elapsedFirst.count(), elapsedSecond.count());

        array.clear();
    }
}

void compareDesc()
{
    vector<int> array;

    for (size_t n = 1000; n < 100000; n += 2000)
    {
        for (size_t i = 0; i < n; i++)
        {
            array.push_back(rand() % 1001);
        }
        insertionSort_desc(array);

        auto firstArray = array;
        auto secondArray = array;

        auto startFirst = chrono::high_resolution_clock::now();
        quickSort(firstArray, 0, firstArray.size() - 1);
        auto endFirst = chrono::high_resolution_clock::now();
        chrono::duration<double> elapsedFirst = endFirst - startFirst;

        auto startSecond = chrono::high_resolution_clock::now();
        quickSortModified(secondArray, 0, secondArray.size() - 1, 100);
        insertionSort(array);
        auto endSecond = chrono::high_resolution_clock::now();
        chrono::duration<double> elapsedSecond = endSecond - startSecond;

        printf("n: %6d\t time normal: %2.10f\t time modified: %2.10f\n", n, elapsedFirst.count(), elapsedSecond.count());

        array.clear();
    }
}

int main()
{

    srand(time(NULL));
    // compareRandom();
    // compareDesc();

    return 0;
}

// WARTOŚCI LOSOWE

// n:   1000        time normal: 0.0009998000       time modified: 0.0029986000
// n:   3000        time normal: 0.0009991000       time modified: 0.0240040000
// n:   5000        time normal: 0.0029996000       time modified: 0.0620065000
// n:   7000        time normal: 0.0030002000       time modified: 0.1180461000
// n:   9000        time normal: 0.0039990000       time modified: 0.1960466000
// n:  11000        time normal: 0.0050467000       time modified: 0.2939509000
// n:  13000        time normal: 0.0060000000       time modified: 0.4010003000
// n:  15000        time normal: 0.0080000000       time modified: 0.5459990000
// n:  17000        time normal: 0.0109996000       time modified: 0.7070007000
// n:  19000        time normal: 0.0089991000       time modified: 0.9090484000
// n:  21000        time normal: 0.0150461000       time modified: 1.1120004000
// n:  23000        time normal: 0.0159996000       time modified: 1.3500468000
// n:  25000        time normal: 0.0160471000       time modified: 1.5980005000
// n:  27000        time normal: 0.0169999000       time modified: 1.9920044000
// n:  29000        time normal: 0.0180467000       time modified: 2.4489524000
// n:  31000        time normal: 0.0200469000       time modified: 2.7500924000
// n:  33000        time normal: 0.0229980000       time modified: 2.9600118000
// n:  35000        time normal: 0.0230132000       time modified: 3.1859858000
// n:  37000        time normal: 0.0279996000       time modified: 3.8519993000
// n:  39000        time normal: 0.0260476000       time modified: 3.9040008000
// n:  41000        time normal: 0.0250476000       time modified: 4.3609999000
// n:  43000        time normal: 0.0349976000       time modified: 4.7830978000
// n:  45000        time normal: 0.0339983000       time modified: 5.5860008000
// n:  47000        time normal: 0.0410048000       time modified: 5.7599942000
// n:  49000        time normal: 0.0380006000       time modified: 6.2870103000
// n:  51000        time normal: 0.0410003000       time modified: 6.4460459000
// n:  53000        time normal: 0.0409873000       time modified: 7.3789997000
// n:  55000        time normal: 0.0460002000       time modified: 7.6191082000

// WARTOSCI MALEJĄCE

// n:   1000        time normal: 0.0040002000       time modified: 0.0100001000
// n:   3000        time normal: 0.0359508000       time modified: 0.0790460000
// n:   5000        time normal: 0.0749982000       time modified: 0.2090470000
// n:   7000        time normal: 0.1419962000       time modified: 0.3920484000
// n:   9000        time normal: 0.2099959000       time modified: 0.6449977000
// n:  11000        time normal: 0.3190523000       time modified: 1.0149526000
// n:  13000        time normal: 0.4029519000       time modified: 1.3230005000
// n:  15000        time normal: 0.5489999000       time modified: 1.7269988000
// n:  17000        time normal: 0.6849526000       time modified: 2.0620017000
// n:  19000        time normal: 0.7940050000       time modified: 2.5289947000
// n:  21000        time normal: 1.0129950000       time modified: 3.2069530000
// n:  23000        time normal: 1.2150026000       time modified: 3.9729976000
// n:  25000        time normal: 1.6321247000       time modified: 4.9900030000
// n:  27000        time normal: 1.6700419000       time modified: 5.3429530000
// n:  29000        time normal: 1.9959985000       time modified: 6.7400007000
// n:  31000        time normal: 2.1319994000       time modified: 6.9650070000
// n:  33000        time normal: 2.3669997000       time modified: 8.0279533000
// n:  35000        time normal: 2.5568513000       time modified: 8.9444538000
// n:  37000        time normal: 3.3709956000       time modified: 10.4440003000
