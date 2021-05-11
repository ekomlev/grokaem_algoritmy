
# сортировка выбором
def selection_sort(arr):
    new_arr = []
    for _ in range(len(arr)):
        smallest_index = find_smallest(arr)
        new_arr.append(arr.pop(smallest_index))  # arr.pop() - removes the item at the given index from the list and returns the removed item.
    return new_arr


def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


print(selection_sort([5, 2, 3, 1, 10]))

