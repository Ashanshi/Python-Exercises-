def sum_of_list(numbers):
    """Returns the sum of integers in a list"""
    total = 0
    for n in numbers:
        total += n
    return total

# Main program
numbers = [3, 5, 2, 1, 4]
result = sum_of_list(numbers)
print(f"The sum of the numbers in the list is: {result}")