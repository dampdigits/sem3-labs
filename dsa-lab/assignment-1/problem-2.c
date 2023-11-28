// Linear Search

#include<stdio.h>
  
void main()
{
    int a[20],i,x,n;
    //clrscr();
    printf("How many array elements?\n");
    scanf("%d",&n);
     
    printf("Enter array elements\n");
    for(i=0;i<n;++i)
        scanf("%d",&a[i]);
     
    printf("Enter element to search:\n");
    scanf("%d",&x);
     
    for(i=0;i<n;++i)
        if(a[i]==x)
            break;
     
    if(i<n)
        printf("Element found at index=%d\n",i);
    else
        printf("Element not found\n");
}

// Output:

// How many array elements?
// 6
// Enter array elements
// 2
// 3
// 4
// 5
// 9
// 6
// Enter element to search:
// 2
// Element found at index=0
