#include<stdio.h>
#include<string.h>
#define SIZE 6
struct colHashing{
  char word[20];
  int value;
};
struct colHashing table[SIZE];


// Hashfunction
int hashfunction(char word[],int n){
  int sum=0;
  for(int i=0;i<n;i++){
    sum+=word[i];
  }
  return sum%SIZE;
}

// initialise
void initialise(){
  for(int i=0;i<SIZE;i++){
    table[i].value=0;
  }
}

// Insert
void insert(char word[]){
  int idx=hashfunction(word,strlen(word));
  while(table[idx].value!=0){
    if(strcmp(table[idx].word,word)==0){
      table[idx].value++;
      return;
    }
    idx=(idx+1)%SIZE;
  }
  strcpy(table[idx].word,word);
  table[idx].value++;
}

// Display
void display(){
  for(int i=0;i<SIZE;i++){
    if(table[i].value!=0){
      printf("%s %d\n",table[i].word,table[i].value);
    }
  }
}

// main function
void main(){
  initialise();
  insert("Mango");
  insert("Apple");
  insert("Banana");
  insert("Mango");
  insert("Mango");
  insert("Mango");
  display();
}