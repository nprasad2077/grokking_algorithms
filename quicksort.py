
def quicksort(array):
    if len(array) < 2:
        return array    # solve for base case
    else:
        pivot = array[0]    # Recursive Case
        # Sub-array of all elements less than pivot.
        less = [i for i in array[1:] if i <= pivot]

        # Sub-array of all elements greater than pivot.
        greater = [i for i in array[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([10, 5, 2, 3]))
print(quicksort([5, 10, 3, 2]))


# If you always choose a random element in the array as the pivot, quicksort will complete in O(n log n) time on average. Quicksort is one of the fastest sorting algorithms out there, and it’s a very good example of D&C.
