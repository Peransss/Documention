#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node *next;
    struct Node *prev;
};

struct Node *createNode(int data) {
    struct Node *newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode -> data = data;
    newNode -> next = newNode;
    newNode -> prev = newNode;
    return newNode;
}

void InsertFirst(struct Node **head, int data) {
    struct Node *newNode = createNode(data);
    *head = newNode;
    newNode -> next = *head;
    newNode -> prev = newNode;
}

void InsertNext(struct Node **head, int data) {
    struct Node *ptr = *head;
    struct Node *newNode = createNode(data);
    struct Node *head1 = *head;
    if (*head != NULL) {
        printf("Linked list is empty!");
    } else {
        while (ptr -> next != *head) {
            ptr = ptr -> next;
        }
        ptr -> next = newNode;
        newNode -> prev = ptr;
        newNode -> next = *head;
        head1 -> prev = newNode;
    }
}

void print(struct Node* head) {
    struct Node* ptr = head;
    while (ptr){
        printf("%d <-> ", ptr -> data);
        ptr = ptr -> next;
        if (ptr == head) {
            printf("%d", ptr -> data);
            break;
        }
    }
}


int main() {
    struct Node *head = NULL;

    InsertFirst(&head, 10);
    InsertNext(&head, 5);
    print(head);
}