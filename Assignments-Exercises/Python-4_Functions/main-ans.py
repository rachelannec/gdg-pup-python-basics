# function 
def create_greeting(name):
    return f"Hello {name}, welcome to the GDG Web Development Team!\nYou're doing great, and I truly believe that someday \nyou'll be an amazing developer. Life may feel challenging right \nnow, and programming can be overwhelming at times, but remember, \nall your hard work will pay off in the end. Keep pushing \nforward, you're on the right path!"

try:
    # get the user's name
    name = str(input("Enter your name: "))
    # calling the function
    greeting = create_greeting(name)

    print(f"\n{greeting}")

except ValueError:
    print("Invalid input: Please enter a valid name.")