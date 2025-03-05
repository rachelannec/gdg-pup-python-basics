#  opening a file in read mode and printing its contents
try:
    with open('sample-ans.txt', 'r') as file:
        contents = file.read()
        print("Contents of the file:")
        print(contents)
except FileNotFoundError:
    print("The file 'sample-ans.txt' was not found.")

# writing to a new file
with open('newfile-ans.txt', 'w') as file:
    file.write("This is a new file\nThe title of the lyrics on sample-ans.txt is My Immortal by Evanescence.\n")
    print("\nNew file created with content:")

# verifying content in the new file by reading it
with open('newfile.txt', 'r') as file:
    newfile_contents = file.read()
    print(newfile_contents)