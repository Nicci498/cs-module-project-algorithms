'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # outer loop
    for i in range(len(arr)):
        matched = False
        for j in range(len(arr)):
            if arr[i] == arr[j] and i != j:
                matched = True
        if not matched:
            return arr[i]
    
    return -1



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")