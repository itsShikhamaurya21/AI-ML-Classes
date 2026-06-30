#include<stdio.h>
#include<string.h>
#define SIZE 6
struct Student{
  int rollNo;
  char name[20];
};

struct Student table[SIZE];

void initialize(){
  for(int i=0;i<SIZE;i++){
    table[i].rollNo=-1;
  }
}
//Hash function
int hashFunction(int rollNo){
  return rollNo%SIZE;
}
//insert 
void insert(int rollNo,char name[]){
  int index=hashFunction(rollNo);
  table[index].rollNo=rollNo;
  strcpy(table[index].name,name);
  printf("%s is inserted at index %d\n",name,index);
}
//search

void Search(int rollNo){
  int index=hashFunction(rollNo);
  if(table[index].rollNo==rollNo){
    printf("\nStudent found ");
    printf("rollno  is %d and name is %s",table[index].rollNo,table[index].name);
  }else{
    printf("Student  not found");
  }
}

void display(){
    printf("\nDISPLAY:\n");

    for(int i=0; i<SIZE; i++){
        if(table[i].rollNo != -1){
            printf("Index %d : %d\t%s\n",i,table[i].rollNo,table[i].name);
        }
        else{
            printf("Index %d : Empty\n", i);
        }
    }
}
int main(){
  initialize();
  insert(123,"Shikha");
  insert(124,"Sahil");
  insert(132,"Shivam");
  insert(116,"Arun");
  insert(100,"tushar");
  Search(100);
  display();
}