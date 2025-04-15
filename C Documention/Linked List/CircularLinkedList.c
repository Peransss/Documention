#include <stdio.h>
#include <stdlib.h>

struct Node{
    int data;
    struct Node* next;
};

struct Node *createNode(struct Node** head, int data){
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode -> data = data;
    newNode -> next = *head;
    return newNode;
}

void InsertFirst(struct Node** head, int data){
    struct Node* newNode = createNode(head, data);
    *head = newNode;
    newNode -> next = *head;
}

void InsertNext(struct Node** head, int data){
    struct Node* ptr = *head;
    struct Node* newNode = createNode(head, data);
    while (ptr -> next != *head){
        ptr = ptr -> next;
    }
    newNode -> next = *head;
    ptr -> next = newNode;
}

void InsertMid(struct Node** head, int data, int pos){
    struct Node* ptr = *head;
    struct Node* newNode = createNode(head, data);
    int pos_next = 0;
    while (ptr != NULL && pos_next + 1 != pos){
        ptr = ptr -> next;
        pos_next += 1;
    }
    if (ptr -> next){
        newNode -> next = ptr -> next;
        ptr -> next = newNode;
    }
}

void InsertLast(struct Node** head, int data){
    struct Node* ptr = *head;
    struct Node* newNode = createNode(head, data);
    while (ptr -> next != *head){
        ptr = ptr -> next;
    }
    newNode -> next = *head;
    ptr -> next = newNode;
}

void removeFirst(struct Node** head){
    struct Node* ptr = *head;
    struct Node* temp = NULL;
    if (ptr -> next == NULL){
        *head = NULL;
    } else {
        temp = ptr;
        *head = ptr -> next;
        temp = NULL;
    }
}

void removeMid(struct Node** head, int pos){
    struct Node* ptr = *head;
    struct Node* temp = NULL;
    int pos_next = 0;
    while (ptr != NULL && pos_next + 1 != pos){
        ptr = ptr -> next;
        pos_next += 1;
    }
    if (ptr -> next){
        temp = ptr -> next;
        ptr -> next = ptr -> next -> next;
        ptr = ptr -> next;
        temp = NULL;
    }
}

void removeLast(struct Node** head){
    struct Node* ptr = *head;
    while (ptr -> next -> next != *head){
        ptr = ptr -> next;
    }
    ptr -> next = *head;
}

void reverseLink(struct Node** head){
    struct Node* ptr = *head;
    struct Node* temp = NULL;
    struct Node* nextN = NULL;
    while (ptr){
        nextN = ptr -> next;
        ptr -> next = temp;
        temp = ptr;
        ptr = nextN;
    }
    *head = temp;
}

void print(struct Node* head) {
    struct Node* ptr = head;
    while (ptr){
        printf("%d -> ", ptr -> data);
        ptr = ptr -> next;
        if (ptr == head) {
            printf("%d", ptr -> data);
            break;
        }
    }
}

int main(){
    struct Node* head = NULL;

    InsertFirst(&head, 10);
    InsertNext(&head, 5);
    InsertNext(&head, 20);
    InsertMid(&head, 30, 1);
    InsertLast(&head, 40);
    reverseLink(&head);
    print(head);
}