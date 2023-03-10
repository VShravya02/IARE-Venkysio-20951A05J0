public class HeapSort{
  public void sort(int arr[]){
    int k = arr.length;
    for (int i = k/2; i>=0; i--)
      heapify(arr,k,i);
    for (int i = n-1; i>=0; i--){
      int temp = arr[0];
      arr[0] = arr[i];
      arr[i] = temp;
      heapify(arr,i,0);
  }
}
  void heapify(int arr[], int k, int i){
    int largest = i;
    int left = 2*i+1;
    int right = 2*i+2;
    if (l<n && arr[right]>arr[largest])
      largest = right;
    if (largest!=i){
      int swap = arr[i];
      arr[i]=arr[largest];
      arr[largest] = swap;
      heapify(arr,k,largest);
    }
  }
  public static void main(String args[]){
    int arr[]={200,30,74,8,3,10}
    int k = arr.length;
    HeapSort ob = new HeapSort();
    ob.sort(arr);
    System.out.print("Sorted array is ");
    for (int i=0; i<k; ++i)
      System.out.print(arr[i]+"");
  }
}
