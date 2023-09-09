// Program demonstrates the operations of a stack using an array.

#include <stdio.h>

#define SIZE 100
int stack[SIZE], top = -1, n = 0;

void push();
void pop();
void show();

void main ()
{
    printf("Enter the number of elements in the stack: ");
    scanf("%d",&n);
    printf("*********Stack operations using array*********");
	
	printf("\n----------------------------------------------\n");
	int choice = 0;
    while(choice != 4)
    {
        printf("Chose one from the below options...\n");  
        printf("\n1.Push\t2.Pop\t3.Show\t4.Exit");  
        printf("\nEnter your choice: ");        
        scanf("%d",&choice);  
        switch(choice)  
        {
            case 1:  
            {   
                push();  
                break;  
            }  
            case 2:  
            {  
                pop();  
                break;  
            }  
            case 3:  
            {  
                show();  
                break;  
            }  
            case 4:   
            {  
                printf("Exiting....\n");  
                break;   
            }  
            default:  
            {  
                printf("Please Enter valid choice.\n");  
            }
        }
    }
}
void push()  
{  
    int val;      
    if (top == SIZE )   
    printf("\nOverflow\n");   
    else
    {
        printf("Enter the value: ");
        scanf("%d",&val);    
        top += 1;
        stack[top] = val;
    }
}
  
void pop()
{   
    if(top == -1)   
    printf("\nUnderflow\n");  
    else
    top -= 1;   
}

void show()  
{  
    for (int i = top; i >= 0; i--)  
    {  
        printf("%d\n",stack[i]);  
    }  
    if(top == -1)   
    {  
        printf("Stack is empty\n");  
    }  
}
