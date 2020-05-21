'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # set window size
    window_min = 0
    window_max = k
    # set new arr
    max_vals = []
    #loop
    for _ in nums:
        window = nums[window_min:window_max]
        max_vals.append(max(window))
        # if window max is still in list bounds, move it up a place
        if window_max < len(nums):
            window_min += 1
            window_max += 1
        else: 
            break
    return max_vals


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
