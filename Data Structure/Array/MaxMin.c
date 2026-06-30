#include<stdio.h>
#include<conio.h>
int min(int *, int);
int max(int*,int);
void main(){
  int i,j;
   int minres;
   int maxres;
  char *std[]={"Shikha","Sahil","Divi","Aachal","Sheetal","Sonali"};
  char *sub[]={"Java","Math"};
  int marks[2][6]={
    {20,30,10,22,23,12},
    {40,34,23,53,45,23}
  };
  printf("Name of student ");
  for(i=0;i<6;i++) 
  printf("\t %s",std[i]);
  
  for(i=0;i<2;i++){
    printf("\t \nSubject name is  %s",sub[i]);
    for( j=0;j<6;j++){
      printf("\t %d",marks[i][j]);
      
    }
    printf("\n");
      minres=min(marks[i],6);
      maxres=max(marks[i],6);
      printf("\t min is %d",minres);
      printf("\t max is %d",maxres);
  }
  

}
int min(int *arr,int n){
  int i;
  int min=*(arr+0);
  for(i=0;i<n;i++){
    if(min>*(arr+i)){
      min=*(arr+i);
    }
  }
  return min;
}
int max(int *arr,int n){
  int i;
  int max=*(arr+0);
  for(i=0;i<n;i++){
    if(max<*(arr+i)){
      max=*(arr+i);
    }
  }
  return max;
}
