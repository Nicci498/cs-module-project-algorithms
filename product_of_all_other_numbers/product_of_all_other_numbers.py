'''
Input: a List of integers
Returns: a List of integers

find total products of array to left
find total '' to right
multiply left and right and append value to new arr

'''

def product_of_all_other_numbers(arr):
    # empty bucket for new arr
    product_arr = []
    # loop through list
    for i in range(len(arr)): 
        #get values to the left of given index
        left = arr[:i]
        # and to right
        right = arr[i + 1:]
        # combine left and right
        combined = left + right
        #initiate a bucket for products (since multiplying must be 1 not zero)
        total = 1
        #for each element in the left-right total
        for e in combined:
            #add to bucket
            total = total * e
            #append to new arr
        product_arr.append(total)

    return product_arr

        #val = total products left * total products right
        #append total to value    


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr2 = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
    # print(arr2[1:])
    # print(arr2[:4])exclusive