reason = input("please enter your reason of loving programming")
filename = 'file/reason_list.txt'
if reason:
    with open(filename, 'a') as file_object:
        file_object.write(reason + " \t")