# Calculating array sum using recursion

def sum_of_list(array):
    if not array:
        return 0
    return array[0] + sum_of_list(array[1:])

array = [1,2,3,4,5,6]
total = sum_of_list(array)
print(total)
