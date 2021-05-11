
def quick_sort(arr):
    # base case
    if len(arr) < 2:
        return arr
    else:
        # recursive case
        pivot = arr[0]
        # sub array all elements that are less than pivot
        less = [i for i in arr[1:] if i <= pivot]
        # sub array all elements that are greater than pivot
        greater = [i for i in arr[1:] if i > pivot]

        less_sorted_sub_arr = quick_sort(less)
        greater_sorted_sub_arr = quick_sort(greater)

        return less_sorted_sub_arr + [pivot] + greater_sorted_sub_arr


print(quick_sort([5, 2, 3, 1, 10]))
