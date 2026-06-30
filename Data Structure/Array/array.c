#include<stdio.h>
#include<conio.h>
float avg(int *, int);
void main(){
  int i;
  printf("Enter the name ");
  char *std[]={"Shikha","Sahil","Divi","Aachal","Sheetal","Sonali"};
  printf("Enter the marks ");
  int marks[]={20,30,10,22,23,12};
  for(i=0;i<6;i++) 
  printf("\t %s",std[i]);
  for(i=0;i<6;i++)
  printf("\t %d",marks[i]);
  float avgres=avg(marks,6);
  printf("result is %f",avgres);
}
float avg(int *arr,int n){
  int sum=0;
  int i;
  for(i=0;i<n;i++){
    sum=sum+*(arr+i);
  }
  return (float)sum/(float)n;
}
