'''
Input: a List of integers
Returns: a List of integers


Traverse the given array ‘arr’ from left to right.
maintain count of non-zero elements in array 
every non-zero element arr[i], put the element at ‘arr[count]’ and increment ‘count’
After complete traversal, all non-zero elements have already been shifted to front end and ‘count’ is set as index of first 0. Now all we need to do is that run a loop which makes all elements zero from ‘count’ till end of the array.
'''

def moving_zeroes(arr):
   return [num for num in arr if num != 0] + \
       [zero for zero in arr if zero == 0]
#zero times diff of lengths
        
    

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
    