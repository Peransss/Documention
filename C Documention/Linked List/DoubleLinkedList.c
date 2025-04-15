#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
    struct Node* prev;
};

struct Node* createNode(char data){
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode -> data = data;
    newNode -> next = newNode;
    newNode -> prev = newNode;
    return newNode;
}

void InsertFirst(struct Node** head, char data){
    struct Node* newNode = createNode(data);
    newNode -> next = *head;
    newNode -> prev = NULL;
    *head = newNode;
}

void InsertNext(struct Node** head, char data){
    struct Node* ptr = *head;
    struct Node* newNode = createNode(data);
    while (ptr -> next){
        ptr = ptr -> next;
    }
    ptr -> next = newNode;
    newNode -> prev = ptr;
}

void InsertMid(struct Node** head, char data, int pos){
    struct Node* ptr = *head;
    struct Node* newNode = createNode(data);
    int pos_next = 0;
    while (ptr != NULL && pos_next + 1 != pos){
        ptr = ptr -> next;
        pos_next += 1;
    }
    if (pos_next <= 1){
        newNode -> next = ptr -> next;
        ptr -> next = newNode;
        newNode -> prev = ptr;
        } else {
            ptr -> next = newNode -> next;
            newNode -> prev = ptr;
            newNode -> next = newNode;
        }
}

void print(struct Node* head) {
    struct Node* temp = head;
    while (temp != NULL) {
        printf("%d <-> ", temp->data);
        temp = temp->next;
    }
    printf("NULL\n");
}

int main(){
    struct Node* head = NULL;

    InsertFirst(&head, 10);
    InsertNext(&head, 5);
    InsertMid(&head, 20, 1);
    print(head);
}