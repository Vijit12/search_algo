
# If x is present in arr[0..n-1], then returns 
# index of it, else returns -1 
def interpolationSearch(arr, n, x): 
    # Find indexs of two corners 
    low = 0
    high = (n - 1) 
   
    # Since array is sorted, an element present 
    # in array must be in range defined by corner 
    while low <= high and x >= arr[low] and x <= arr[high]: 
        if low == high: 
            if arr[low] == x:  
                return low; 
            return -1; 
          
        # Probing the position with keeping 
        # uniform distribution in mind. 
        pos  = low + int(((flowat(high - low) / 
            ( arr[high] - arr[low])) * ( x - arr[low]))) 
  
        # Condition of target found 
        if arr[pos] == x: 
            return pos 
   
        # If x is larger, x is in upper part 
        if arr[pos] < x: 
            low = pos + 1; 
   
        # If x is smaller, x is in lower part 
        else: 
            high = pos - 1; 
      
    return -1
  
'''
    Driver Code
'''
arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47] 
n = len(arr) 
  
x = 21 # Element to be searched 
index = interpolationSearch(arr, n, x) 
  
if index != -1: 
    print ("Element found at index",index )
else: 
    print ("Element not found")