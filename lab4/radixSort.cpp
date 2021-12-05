// C++ implementation of Radix Sort
#include <iostream>
#include <string>
using namespace std;

void print(string arr[], int n)
{
	for (int i = 0; i < n; i++)
		cout << arr[i] << " ";
	cout << "\n";
}

int getMax(string arr[], int n)
{
	int max = arr[0].size();
	for (int i = 1; i < n; i++)
	{
		if (arr[i].size() > max)
			max = arr[i].size();
	}
	return max;
}

// A function to do counting sort of arr[] according to
// the digit represented by exp.
void countSort(string arr[], int n, int exp, int lengthArray[])
{
	string outputArray[n]; // output array

	int count[27] = {0};


	string addedBrackets[27];
	for (size_t i = 0; i < n; i++)
	{
		addedBrackets[i] = arr[i];
	}

	// Store count of occurrences in count[]
	for (size_t i = 0; i < n; i++)
	{
		if (lengthArray[i] < exp + 1)
		{
			for (size_t j = lengthArray[i] - 1; j < exp; j++)
			{
				addedBrackets[i].append("[");
			}
			count[(((int)addedBrackets[i][exp]) % 32) - 1]++;
		}
		else
		{
			count[(((int)addedBrackets[i][exp]) % 32) - 1]++;
		}
	}
	// Change count[i] so that count[i] now contains actual
	// position of this digit in output[]
	for (size_t i = 1; i < 27; i++)
	{
		count[i] += count[i - 1];
	}
	for (size_t i = 0; i < 27; i++)
	{
		count[i]--;
	}
	
	// Build the output array
	for (int i = n - 1; i >= 0; i--)
	{
		if (count[(((int)addedBrackets[i][exp]) % 32) - 1] >=0) {
			outputArray[count[(((int)addedBrackets[i][exp]) % 32) - 1]] = arr[i];
			count[(((int)addedBrackets[i][exp]) % 32) - 1]--;
		}	
	}

	for (size_t i = 0; i < n; i++)
	{
		lengthArray[i] = outputArray[i].size();
	}
	

	// Copy the output array to arr[], so that arr[] now
	// contains sorted numbers according to current digit
	for (size_t i = 0; i < n; i++)
	{
		arr[i] = outputArray[i];
	}

	
}

// The main function to that sorts arr[] of size n using
// Radix Sort
void radixsort(string arr[], int n)
{
	// Find the maximum number to know number of digits
	int lengthArray[n] = {0};

	for (size_t i = 0; i < n; i++)
	{
		lengthArray[i] = arr[i].length();
	}

	int m = getMax(arr, n);

	// Do counting sort for every digit. Note that instead
	// of passing digit number, exp is passed. exp is 10^i
	// where i is current digit number
	for (int exp = m - 1; exp >= 0; exp--)
		countSort(arr, n, exp, lengthArray);

}

// Driver Code
int main()
{
	string arr[] = {"Konrad", "Ala", "Mikolaj", "Milosz", "Patryk", "Grabcio", "Bogdan"};
	int n = sizeof(arr) / sizeof(arr[0]);
	// Function Call
	radixsort(arr, n);
	print(arr, n);
	return 0;
}
