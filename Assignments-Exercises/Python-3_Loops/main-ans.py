# for-loop for favorite foods
favorite_food = ['kanin', 'ulam', 'ice cream', 'bread']

print("Here are my favorite foods:")
for food in favorite_food:
    print(f"- {food}")



# while-loop for countdown
try:
    n = int(input("Enter a positive number to start the countdown: "))
    if n <= 0:
        print("Invalid input: Please enter a number greater than zero.")
    else:
        print
        print("Countdown:")
        while n > 0:
            print(n)
            n -= 1
        print("Countdown complete!")
except ValueError:
    print("Invalid input: Please enter a valid number.")