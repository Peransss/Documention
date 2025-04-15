#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

struct Node* createNode(int data){
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode -> data = data;
    newNode -> next = NULL;
    return newNode;
}

void InsertFirst(struct Node** head, int data){
    struct Node* newNode = createNode(data);
    newNode -> next = *head;
    *head = newNode;
}

void InsertNext(struct Node** head, int data){
    struct Node* ptr = *head;
    struct Node* newNode = createNode(data);
    while (ptr -> next != NULL) {
        ptr = ptr -> next;
    }
    ptr -> next = newNode;
}

void InsertMid(struct Node** head, int data, int pos){
    struct Node* ptr = *head;
    struct Node* newNode = createNode(data);
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

void print(struct Node* head) {
    struct Node* temp = head;
    while (temp != NULL) {
        printf("%d -> ", temp->data);
        temp = temp->next;
    }
    printf("NULL\n");
}

int main(){
    struct Node* head = NULL;

    InsertFirst(&head, 10);
    InsertNext(&head, 5);
    InsertMid(&head, 8, 1);
    print(head);

    return 0;
}