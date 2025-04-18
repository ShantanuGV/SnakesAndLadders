def binary_search(arr, low, high, x):
 
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
        print(mid)
 
        # If element is present at the middle itself
        if arr[mid] == x:
            print(arr[mid])
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            print(arr[mid])
            return binary_search(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            print(arr[mid])
            return binary_search(arr, mid + 1, high, x)
 
    else:
        # Element is not present in the array
        print(arr[mid])
        return -1
 
# Test array
arr = [ 2,8,10,20,40 ]
x = 40
 
# Function call
result = binary_search(arr, 0, len(arr)-1, x)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")