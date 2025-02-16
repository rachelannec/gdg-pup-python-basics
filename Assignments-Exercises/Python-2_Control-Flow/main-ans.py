def agecheck(age):
    try:
        age = int(age)
        if age < 0:
            raise ValueError("Age must be positive integer.")
        elif age < 13:
            print("You are categorized as: Child")
        elif age < 20:
            print("You are categorized as: Teenager")
        elif age < 60:
            print("You are categorized as: Adult")
        else:
            print("You are categorized as: Senior")
    except ValueError:
        print("Invalid input: Age must be positive integer.")

userInput = input("Enter your age: ")
agecheck(userInput)

# test
# agecheck(10) # Child
# agecheck(15) # Teenager
# agecheck(30) # Adult
# agecheck(70) # Senior
# agecheck('rawr') # Age cannot be negative.
