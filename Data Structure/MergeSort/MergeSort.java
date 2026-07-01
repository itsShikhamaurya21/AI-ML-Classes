
public class MergeSort {
  public static void mergeSort(int[] arr) {
    int n = arr.length;
    if (n <= 1)
      return;
    // create two new array
    int[] a = new int[n / 2];
    int[] b = new int[n - n / 2];
    // put the elements into an array
    int idx = 0;
    for (int i = 0; i < a.length; i++)
      a[i] = arr[idx++];
    for (int i = 0; i < b.length; i++)
      b[i] = arr[idx++];

    // magic means apply recursion
    mergeSort(a);
    mergeSort(b);
    // Marge a and b
    merge(a, b, arr);

  }

  public static void merge(int a[], int b[], int c[]) {
    int n = c.length;
    // int c[] = new int[n];
    int i = 0;
    int j = 0;
    int k = 0;
    while (i < a.length && j < b.length) {
      if (a[i] < b[j])
        c[k++] = a[i++];
      else
        c[k++] = b[j++];
    }
    while (i < a.length)
      c[k++] = a[i++];
    while (j < b.length)
      c[k++] = b[j++];

  }

  public static void main(String args[]) {
    int arr[] = { 5, 2, 8, 4, 1, 6, 7, 3 };
    mergeSort(arr);
    for (int m = 0; m < arr.length; m++) {
      System.out.print(arr[m] + " ");
    }
  }
}
