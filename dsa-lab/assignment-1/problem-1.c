// Linear Search in 1D array

#include <stdio.h>

int main(void)
{
    // Input arrat size
    int size, i;
    printf("\nEnter the size of the array: ");
    scanf("%d", &size);

    // Create array
    int arr[size];

    // Input array elements
    for (i = 0; i < size; i++)
    {
        printf("Enter element: ");
        scanf("%d", &arr[i]);
    }

    // Input the search-number
    int num;
    printf("\nEnter the number to be searched: ");
    scanf("%d", &num);

    int flag = 0;
    // Find the number in array
    for (i = 0; i < size; i++)
    {
        if (num == arr[i])
        {
            flag = 1;
            break;
        }
    }

    // Check if the number was found
    if (flag)
    {
        printf("\nFound searched number at position - %d\n.", i);
    }
    else
    {
        printf("\nSearched number not found.\n");
    }
}

// Output:

// Enter the size of the array: 6
// Enter element: 1
// Enter element: 2
// Enter element: 3
// Enter element: 4
// Enter element: 5
// Enter element: 6

// Enter the number to be searched: 5

// Found searched number at position - 4