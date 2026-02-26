def quick_sort(arr):
    # Base case: a list of 0 or 1 elements is already sorted
    if len(arr) <= 1:
        return arr[:]  # Return a copy to avoid mutating the original

    pivot = arr[0]  # Always use the first element as pivot

    # Three-way partition: separates duplicates into their own bucket
    less = []
    equal = []
    greater = []

    for x in arr:
        if x < pivot:
            less.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            greater.append(x)

    # Recursively sort the less-than and greater-than partitions
    return quick_sort(less) + equal + quick_sort(greater)
