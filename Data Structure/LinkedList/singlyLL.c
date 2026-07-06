#include <stdio.h>
#include<stdlib.h>
struct Node{
  int data;
  struct Node *next;
};
struct Node *head=NULL;

void insertAtBegin();
void insertAtEnd();
void insertAtPosition();
void deleteAtbegin();
void deleteAtEnd();
void deleteAtPosition();
void display();
int main(){
  int choice;
   printf("\n1. Insertion at begin");
    printf("\n2. Insertion at end");
    printf("\n3. Insertion at position");
    printf("\n4. Deletion at begin");
    printf("\n5. Deletion at end");
    printf("\n6. Deletion at position");
    printf("\n7. Display");
  while(1){
    printf("\nEnter the choice ");
    scanf("%d",&choice);
    switch(choice){
      case 1:
        printf("\n=======Insertion at begin ==============\n");
        insertAtBegin();
        printf("\n=======Insertion SuccessFull==============\n");
        break;
      case 2:
      printf("\n========Insertion at end =================\n");
        insertAtEnd();
      printf("\n=======Insertion SuccessFull================\n");
        break;
      case 3:
      printf("\n========Insertion at position =================\n");
        insertAtPosition(); 
      printf("\n=======Insertion SuccessFull================\n");
        break;  
      case 4:
      printf("\n========Deletion at begin =================\n");
        deleteAtbegin();
      printf("\n=======Deletion SuccessFull================\n");
        break;
      case 5:
      printf("\n========Deletion at end =================\n");
        deleteAtEnd();
      printf("\n=======Deletion SuccessFull================\n");
        break;
      case 6:
      printf("\n========Deletion at position =================\n");
        deleteAtPosition();
      printf("\n=======Deletion SuccessFull================\n");  
      break;
      case 7:
      printf("\n========Display =================\n");  
        display();
      printf("\n=======Display SuccessFull================\n");
      break;
      case 8:
      exit(0);
      default:
      printf("Invalid choice ");
    }
  }

  return 0;
}
void insertAtBegin(){
  struct Node *newnode;
  newnode=(struct Node*)malloc(sizeof(struct Node));
  if(newnode==NULL){
    printf("Memory allocation failed ");
    return ;  
  }
  printf("Enter data : ");
  scanf("%d",&newnode->data);

  newnode->next=head;
  head=newnode;
  printf("Inserted Successfully ");
}

void insertAtEnd(){
  struct Node *newnode;
  newnode=(struct Node*)malloc(sizeof(struct Node));
  if(newnode==NULL){
    printf("Memory allocation is failed ");
    return;
  }
  printf("Enter data ");
  scanf("%d",&newnode->data);
  struct Node *temp;
  temp=head;
  if(head==NULL){
    head=newnode;
  }
  newnode->next=NULL;
  while(temp->next!=NULL){
    temp=temp->next;

  }
  temp->next=newnode;
  printf("Insertion at end successfull ");
}
void InsertAtPosition(){
  struct Node *newnode;
  newnode=(struct Node*)malloc(sizeof(struct Node));
  int pos;
  struct Node *temp=head;
  printf("Enter position :");
  scanf("%d",&pos);
  if(pos==1){
    insertAtBegin();
  }
   for(int i=1;i<pos && temp->next!=NULL;i++){

    temp=temp->next;
   }
   while(temp->next!=NULL){
    temp->next=newnode->next;
    
  }
  temp->next=newnode;
}