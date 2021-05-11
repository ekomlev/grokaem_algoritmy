# Naming convention: https://www.python.org/dev/peps/pep-0008/#:~:text=Use%20the%20function%20naming%20rules,invoke%20Python's%20name%20mangling%20rules.

def binary_search(list_1, item):
    low = 0
    high = len(list_1)-1

    while low <= high:
        mid = int((low + high)/2)
        guess = list_1[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))  # returns 1 as an index of element in list
