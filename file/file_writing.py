filename = 'file/programming.txt'

# with open(filename, 'w') as file_object:
#     file_object.write("i love programming.\n")
#     file_object.write("i love to create new things. \n")

with open(filename, 'a') as file_object:
    file_object.write("i love programming.\n")
    file_object.write("i love to create new things. \n")