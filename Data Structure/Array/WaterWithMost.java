public class WaterWithMost {
  public static int WaterWithMost(int arr[]) {
    int maxWater = 0;
    int i = 0, j = arr.length - 1;
    while (i < j) {
      int water = 0;
      if (arr[i] < arr[j]) {
        water = arr[i] * (j - i);
        i++;
      } else {
        water = arr[j] * (j - i);
        j--;
      }
      maxWater = Math.max(water, maxWater);
    }
    return maxWater;
  }

  public static void main(String args[]) {
    int arr[] = { 1, 8, 7, 3, 2, 6, 7, 7 };
    System.out.println(WaterWithMost(arr));
  }
}
