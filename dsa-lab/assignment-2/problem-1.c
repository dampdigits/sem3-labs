// Binary Search in 1D array - assuming the elements are entered in increasing order

#include <stdio.h>

int main(void)
{
    int size;
    printf("\nEnter the array size: ");
    scanf("%d", &size);

    int arr[size];
    for (int i = 0; i < size; i++)
    {
        printf("Enter element:");
        scanf("%d", &arr[i]);
    }

    int num;
    printf("\nEnter the number to be searched: ");
    scanf("%d", &num);
    
    int beg = 0, end = size - 1, mid = 0;
    int found = 0;

    do    
    {
        mid = (beg + end) / 2;
        if (num == arr[mid])
        {
            found = 1;
            break;
        }
        else if (num < arr[mid])
        {
            end = mid - 1;
        }
        else
        {
            beg = mid + 1;
        }
    } while (beg <= end);

    if (found)
    {
        printf("\nFound searched number at position - %d\n.", mid + 1);
    }
    else
    {
        printf("\nSearched number not found.\n");

    }

    return 0;
}

// Output:

// Enter the array size: 3
// Enter element:1
// Enter element:2
// Enter element:3

// Enter the number to be searched: 1

// Found searched number at position - 1
