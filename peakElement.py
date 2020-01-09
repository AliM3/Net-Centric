def peak(array, low, high, n):  
    mid = low + (high - low)/2 
    mid = int(mid) 
      
    # Compare middle element with its neighbors
    if ((mid == 0 or array[mid - 1] <= array[mid]) and 
       (mid == n - 1 or array[mid + 1] <= array[mid])): 
        return mid 
    
    # Move to the larger element
    elif (mid > 0 and array[mid - 1] > array[mid]): 
        return peak(array, low, (mid - 1), n) 
    else: 
        return peak(array, (mid + 1), high, n) 
  
# Wrapper over recursive function peak() 
def findPeak(array, n): 
    return peak(array, 0, n - 1, n)
    
