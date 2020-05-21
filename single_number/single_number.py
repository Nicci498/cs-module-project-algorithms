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

def dict_single_number(arr):
    counts = {}
    for x in arr:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    for num in counts:
        if counts[num] == 1:
            return num

def arr_single_number(arr):
    no_dupes = []
    for i in arr:
        if i not in no_dupes:
            no_dupes.append(x)
        else:
            no_dupes.remove(i)
    return no_dupes[0]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")