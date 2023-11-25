// Program evaluates a POSTFIX expression

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <limits.h>
#define MAX_SIZE 100
// Define a stack structure
struct Stack {
    int top;
    unsigned capacity;
    int* array;
};
// Create a new stack
struct Stack* createStack(unsigned capacity) {
    struct Stack* stack = (struct Stack*)malloc(sizeof(struct Stack));
    stack->top = -1;
    stack->capacity = capacity;
    stack->array = (int*)malloc(stack->capacity * sizeof(int));
    return stack;
}
// Check if the stack is full
bool isFull(struct Stack* stack) {
    return stack->top == stack->capacity - 1;
}
// Check if the stack is empty
bool isEmpty(struct Stack* stack) {
    return stack->top == -1;
}
// Push an element onto the stack
void push(struct Stack* stack, int item) {
    if (isFull(stack)) {
        printf("Stack is full. Cannot push.\n");
        return;
    }
    stack->array[++stack->top] = item;
}
// Pop an element from the stack
int pop(struct Stack* stack) {
    if (isEmpty(stack)) {
        printf("Stack is empty. Cannot pop.\n");
        return INT_MIN; // Return a minimum integer value on error
    }
    return stack->array[stack->top--];
}
// Function to evaluate a postfix expression
int evaluatePostfix(char* postfix) {
    struct Stack* stack = createStack(MAX_SIZE);
    int i;
    for (i = 0; postfix[i]; ++i) {
        if (postfix[i] >= '0' && postfix[i] <= '9') {
            push(stack, postfix[i] - '0'); // Convert char digit to integer
        } else {
            int operand2 = pop(stack);
            int operand1 = pop(stack);
            switch (postfix[i]) {
            case '+':
                push(stack, operand1 + operand2);
                break;
            case '-':
                push(stack, operand1 - operand2);
                break;
            case '*':
                push(stack, operand1 * operand2);
                break;
            case '/':
                push(stack, operand1 / operand2);
                break;
            }
        }
    }
    if (!isEmpty(stack)) {
        return pop(stack);
    } else {
        printf("Invalid postfix expression.\n");
        return INT_MIN; // Return a minimum integer value on error
    }
}
int main() {
    char postfix[MAX_SIZE];
    printf("Enter a postfix expression: ");
    scanf("%s", postfix);
    int result = evaluatePostfix(postfix);
    if (result != INT_MIN) {
        printf("Result of the postfix expression: %d\n", result);
    }
    return 0;
}

// Output:

// Enter a postfix expression: 589+-
// Result of the postfix expression: -12
