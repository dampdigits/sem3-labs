#include<stdio.h>
#include<conio.h>
  
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
        printf("Element found at index=%d",i);
    else
        printf("Element not found");
  
    getch();
}
