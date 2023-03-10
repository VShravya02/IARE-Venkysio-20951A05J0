def Heapify(arr,k,i):
  largest = i
  left = 2*i+1
  right = 2*i+2
  if left<k and arr[left]>arr[largest]:
    largest=left
  if right<k and arr[right]>arr[largest]:
    largest=right
  if largest!=i:
    arr[i],arr[largest]=arr[largest],arr[i]
    Heapify(arr,k,largest)
 def HeapSort(arr):
  n=len(arr)
  for i in range(k//2-1,-1,-1):
    heapify(arr,k,i)
  for i in range(n-1,0,-1):
    arr[0],arr[i]=arr[i],arr[0]
    swap
    heapify(arr,i,0)
    return arr
arr=[89,29,90,82,12,1]
sorted_arr=HeapSort(arr)
print("Sorted array is: ", sorted_arr)
  
