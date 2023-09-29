#include <stdio.h>
#include <stdbool.h>

#define MAX_SIZE 10

int queue[MAX_SIZE];
int front = -1;
int rear = -1;

bool isFull() {
    return  (front == 0 && rear == MAX_SIZE - 1) || (front == rear + 1);
}

bool isEmpty() {
	return front == -1;
}

void enqueue(int item) {
    if (isFull()) {
        printf("Queue is full. Cannot enqueue.\n");
    }
    if (front == -1) {
        front = rear = 0;
    }
    else if (rear == MAX_SIZE - 1) {
        rear = 0;
    }
    else {
        rear ++;
    }

    queue[rear] = item;
    printf("Enqueued: %d\n", item);
}

int dequeue() {
    if (isEmpty()) {
        printf("Queue is empty. Cannot dequeue.\n");
        return -1;
    }

    int  item = queue[front];
    if (front == rear) {
        front = rear = -1;
    }
    else if (front  == MAX_SIZE - 1) {
        front = 0;
    }
    else {
        front++;
    }
    return item;
}

void display() {
    if  (isEmpty()) {
        printf("Queue is empty.\n");
        return;
    }
    printf("Queue elements: ");
    int i = front;
    if (front <= rear) {
        while  (i <= rear) {
            printf("%d", queue[i]);
            i++;
        }
    }
    else {
        while (i <  MAX_SIZE) {
            printf("%d",  queue[i]);
            i++;
        }
        i = 0;
        while (i <= rear) {
            printf("%d", queue[i]);
            i++;
        }
    }
    printf("\n");
}

int main(void) {
    enqueue(1);
    enqueue(2);
    enqueue(3);
    enqueue(4);
    display();
    int deq = dequeue();
    if (deq != -1) {
        printf("Dequeued: %d\n", deq);
    }
    display();
    enqueue(5);
    enqueue(6);
    display();
    return 0;
}