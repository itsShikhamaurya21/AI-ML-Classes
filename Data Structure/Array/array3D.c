#include <stdio.h>
#include <conio.h>
float avg(int *, int);
void main()
{
  int i, j, s;
  float avgres;
  char *std[] = {"Shikha", "Sahil", "Divi", "Aachal", "Sheetal", "Sonali"};
  char *sub[] = {"Java", "Math"};
  char *sec[] = {"Section A", "Section B"};
  int marks[2][2][6] = {
    {
      {20, 30, 10, 22, 23, 12},
      {40, 34, 23, 53, 45, 23}
    },
    {
      {1,2,3,4,5,6},
      {7,8,9,10,11,12}
    }

  };
  printf("Name of student ");
  for (i = 0; i < 6; i++)
    printf("\t %s", std[i]);
  for (s = 0; s < 2; s++)
  {
    printf("\n");
    printf("\t Section %s",sec[s]);
    for (i = 0; i < 2; i++)
    {
      printf("\t \nSubject name is  %s", sub[i]);
      for (j = 0; j < 6; j++)
      {
        printf("\t%d",marks[s][i][j]);
      }
      printf("\n");
      avgres = avg(marks[s][i], 6);
      printf("\t result is %f", avgres);
    }
  }
}
float avg(int *arr, int n)
{
  int sum = 0;
  int i;
  for (i = 0; i < n; i++)
  {
    sum = sum + *(arr + i);
  }
  return (float)sum / (float)n;
}
