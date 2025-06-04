#include <stdio.h>
#include <stdbool.h>

#define MAX_SIZE 25

typedef struct {
    int arr[MAX_SIZE];
    int top;
} Stack;

void Initialize(Stack * stack){
    stack -> top = -1;
}

bool isEmpty(Stack * stack){
    return stack -> top == -1;
}

bool isFull(Stack *stack){
    return stack -> top == MAX_SIZE - 1;
}

void Push(Stack *stack, int data){
    if (isFull(stack)){
        printf("Stack is Full!");
    } else {
        stack -> arr[++stack -> top] = data;
        printf("Pushed %d", data);
    }
}

int Pop(Stack *stack){
    if (isEmpty(stack)){
        printf("Stack is Empty!");
    } else {
        int pop = stack -> arr[stack -> top];
        stack -> top--;
        printf("Pop %d", pop);
        return pop;
    }
}

int main(){
    Stack stack;

    Initialize(&stack);

    Push(&stack, 3);
}
