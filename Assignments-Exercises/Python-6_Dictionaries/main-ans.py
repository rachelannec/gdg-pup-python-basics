my_dict = {'name': 'Eren', 
           'age': 15}
print("Original dictionary:", my_dict)

# add new value pair
my_dict['hometown'] = 'Shiganshina'
print("Dictionary after adding an item:", my_dict)

# update an existing key-value pair
my_dict['age'] = 19
print("Dictionary after updating an item:", my_dict)

del my_dict['age']
print("Dictionary after removing an item:", my_dict)    
