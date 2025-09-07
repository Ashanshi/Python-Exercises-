import random
def roll_dice(sides):
    result = random.randint(1, sides)
    return result
def main():
    sides = int(input("Enter the number of sides on the dice: "))
    result = 0
    while result != sides:
        result = roll_dice(sides)
        print(result)
main()