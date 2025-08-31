#print all numbers between 1 and 1000 that are divisible by three
number = 1
while number <= 1000:
    if number % 3 == 0:
        print(number)
    number = number + 1