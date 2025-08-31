# program to find smallest and largest number

number_input = input("Enter a number (or press Enter to quit): ")
# at least one number given
if number_input != "":
    number = float(number_input)
    smallest = number
    largest = number

    while number_input != "":
        number = float(number_input)
        if number < smallest:
            smallest = number
        if number > largest:
            largest = number
        number_input = input("Enter a number (or press Enter to quit): ")

    print(f"Smallest number: {smallest:.1f}")
    print(f"Largest number: {largest:.1f}")
else:
    print("No numbers were entered.")