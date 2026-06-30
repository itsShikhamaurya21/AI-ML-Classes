// #include<stdio.h>
// int main(){
//   int arr[] = {1, 2, 3, 4, 5};
// printf("%zu", sizeof(&arr));
// return 0;
// }
// #include <stdio.h>
// void modify(int arr[]) {
// arr[0] = 99;
// }
// int main() {
// int a[3] = {1, 2, 3};
// modify(a);
// printf("%d", a[0]);
// return 0;
// }
// #include <stdio.h>
// int main() {
// int arr[0];
// printf("%zu", sizeof(arr));
// return 0;
// }
// #include <stdio.h>
// int main() {
// int arr[5] = {1, 2, 3, 4, 5};
// int *p = arr;
// printf("%d", *(p + 4) - *(p + 1));
// return 0;
// }
// #include <stdio.h>
// int main() {
// int arr[4] = {10, 20, 30, 40};
// void *ptr = arr;
// printf("%d", *(int *)(ptr + 1));
// return 0;
// }

// #include <stdio.h>
// int main() {
// int arr[5] = {1, 2, 3, 4, 5};
// int *p = arr + 1;
// int *q = arr + 4;
// printf("%td", q - p);
// return 0;
// }
// int arr[1][1]={{2,2},{2,3}};
// for(int i=0;i<2;i++){
//   for(int j=0;j<2;j++){
//     printf("%d",*(arr+i)+j);
//   }
// }
// }
// #include <stdio.h>
// int main() {
//     int arr[2][3] = {1, 2, 3, 4, 5, 6};
//     printf("%d", arr[0][4]);
//     return 0;
// }

#include <stdio.h>
int main() {
    int a[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9});
    int (*p)[3] = a;
    printf("%d %d", ***&p, *(*(p + 2) + 1));
    return 0;
}
