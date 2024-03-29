#Python QuickSort

def partition(array, low, high):
  i = low - 1
  pivot = array[high]
  
  for j in range(low, high):
  
    if array[j] <= pivot:
      i += 1
      array[i], array[j] = array[j], array[i]
  
  array[i + 1], array[high] = array[high], array[i +1]
  
  return (i + 1)
  
def quicksort(array, low, high):
  if low < high:
    pIndex = partition(array, low, high)
    
    quicksort(array, low, pIndex - 1)
    quicksort(array, pIndex + 1, high)
    
