

# factorial: 5! = 5*4*3*2*1
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)


# sum of list elements via recursion
def sum_list(my_list):
    if len(my_list) == 0:
        return 0
    else:
        return my_list[0] + sum_list(my_list[1:])


# calculate items in list
def items_count(my_list):
    if my_list == []:
        return 0
    else:
        return 1 + items_count(my_list[1:])


# the biggest item in list
def max_item(my_list):
    if len(my_list) == 2:
        return my_list[0] if my_list[0] > my_list[1] else my_list[1]
    sub_max_item = max_item(my_list[1:])
    return my_list[0] if my_list[0] > sub_max_item else sub_max_item


# binary search by recursion
def find_index(my_list, element, low, high):
    if high >= low:                                      # Check base case
        mid = (high + low) // 2
        if my_list[mid] == element:                      # If element is present at the middle itself
            return mid
        elif my_list[mid] > element:                     # If element is smaller than mid, then it can only be present in left subarray
            return find_index(my_list, element, low, mid - 1)
        else:                                            # Else the element can only be present in right subarray
            return find_index(my_list, element, mid + 1, high)

    else:                                                # Element is not present in the array
        return -1


m_list = [3, 4, 9, 1]
my_sorted_list = [2, 3, 4, 5, 6, 7, 9]

print("Factorial from 3 is " + str(factorial(3)))  # factorial
print("Sum of elements in list: " + str(m_list) + " is: " + str(sum_list(m_list)))  # sum of list elements
print("Count of list elements in list: " + str(m_list) + " is: " + str(items_count(m_list)))  # count of list elements
print("Max item in list: " + str(m_list) + " is: " + str(max_item(m_list)))  # max item in list elements
print("Binary search in list: " + str(my_sorted_list) + " for element 5 is: " + str(find_index(my_sorted_list, 5, 0, len(my_sorted_list)-1)))  # binary search in sort list
