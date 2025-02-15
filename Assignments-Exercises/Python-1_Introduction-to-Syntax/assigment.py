# naguluhan po ako doon sa instructions sa totoo lang >.<

# name = 'John Doe'
# age = 25
# height = 6.1
# is_student = True or 'Yes'

name = input('Enter your name: ')
age = int(input('Enter your age: '))
height = float(input('Enter your height: '))
is_student = bool(input('Are you a student? '))

print('\n')
print(f'Hello, {name}!')
print(f'You are {age} years old and {height} feet tall.')
if is_student == True:
    print('You are a student.')
else:   
    print('You are not a student.')
      

print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of height:", type(height))
print("Type of is_student:", type(is_student))
