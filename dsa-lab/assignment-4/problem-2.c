// Program converts infix expressions to postfix

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#define MAX_SIZE 100
// Define a stack structure
struct Stack {
    int top;
    unsigned capacity;
    char* array;
};
// Create a new stack
struct Stack* createStack(unsigned capacity) {
    struct Stack* stack = (struct Stack*)malloc(sizeof(struct Stack));
    stack->top = -1;
    stack->capacity = capacity;
    stack->array = (char*)malloc(stack->capacity * sizeof(char));
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
void push(struct Stack* stack, char item) {
    if (isFull(stack)) {
        printf("Stack is full. Cannot push.\n");
        return;
    }
    stack->array[++stack->top] = item;
}
// Pop an element from the stack
char pop(struct Stack* stack) {
    if (isEmpty(stack)) {
        printf("Stack is empty. Cannot pop.\n");
        return '\0'; // Return null character on error
    }
    return stack->array[stack->top--];
}
// Get the top element from the stack without popping it
char peek(struct Stack* stack) {
    if (isEmpty(stack)) {
        printf("Stack is empty. Cannot peek.\n");
        return '\0'; // Return null character on error
    }
    return stack->array[stack->top];
}
// Precedence of operators
int precedence(char op) {
    if (op == '+' || op == '-')
    return 1;
    if (op == '*' || op == '/')
    return 2;
    return 0;
}
// Convert infix expression to postfix expression
void infixToPostfix(char* infix) {
    struct Stack* stack = createStack(MAX_SIZE);
    int i, j;
    char postfix[MAX_SIZE];
    for (i = 0, j = -1; infix[i]; ++i) {
        if (infix[i] >= 'a' && infix[i] <= 'z') {
            postfix[++j] = infix[i];
        } else if (infix[i] == '(') {
            push(stack, infix[i]);
        } else if (infix[i] == ')') {
            while (!isEmpty(stack) && peek(stack) != '(') {
                postfix[++j] = pop(stack);
            }
            if (!isEmpty(stack) && peek(stack) != '(') {
                printf("Invalid expression.\n");
                return;
            } else {
                pop(stack);
            }
        } else {
            while (!isEmpty(stack) && precedence(infix[i]) <= precedence(peek(stack))) {
                postfix[++j] = pop(stack);
            }
            push(stack, infix[i]);
        }
    }
    while (!isEmpty(stack)) {
        postfix[++j] = pop(stack);
    }
    postfix[++j] = '\0';
    printf("Postfix expression: %s\n", postfix);
}

int main() {
    char infix[MAX_SIZE];
    printf("Enter an infix expression: ");
    scanf("%s", infix);
    infixToPostfix(infix);
    return 0;
}