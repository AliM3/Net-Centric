# Maximum Subarray Sum (D&C Approach)
def maxCrossSum(array, left, mid, right) : 
      
    # Include elements on left of mid. 
    sm = 0 
    left_sum = -1000
      
    for i in range(mid, left - 1, -1) : 
        sm = sm + array[i] 
          
        if (sm > left_sum) : 
            left_sum = sm 
      
    # Include elements on right of mid 
    sm = 0; right_sum = -1000
    for i in range(mid + 1, right + 1) : 
        sm = sm + array[i] 
          
        if (sm > right_sum) : 
            right_sum = sm 
  
    # Return sum of elements on left and right of mid 
    return left_sum + right_sum; 
  
# Returns sum of maxium sum subarray in array[left..right] 
def maxSubArraySum(array, left, right) : 
    
    # If there is only one element
    if (left == right) : 
        return array[left] 
        
    mid = (left + right) // 2

    return max(maxSubArraySum(array, left, mid), 
               maxCrossSum(array, left, mid, right),
               maxSubArraySum(array, mid + 1, right))
