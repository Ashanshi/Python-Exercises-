#create empty list
numbers = []

#ask number  until empty string
num = input("Enter a number: ")
while num != "":
    numbers.append(float(num))
    num = input("Enter a number: ")
numbers.sort(reverse=True)
print("The greatest numbers in descending order:")
for n in numbers[ :5]:
    print(n)