name = input("please enter your name")
filename = 'file/guest_list.txt'
if name:
    print("hello, dear " + name + " !")
    with open(filename, 'a') as file_object:
        file_object.write(name + " \n")