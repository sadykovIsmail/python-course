def merge_sort(arr):
    # Base case: a list of 0 or 1 elements is already sorted
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])   # Recursively sort left half
    right = merge_sort(arr[mid:])  # Recursively sort right half

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0  # Pointers into the left and right halves

    # Compare front elements of each half and take the smaller one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append any remaining elements (at most one side will have leftovers)
    result.extend(left[i:])
    result.extend(right[j:])
    return result
