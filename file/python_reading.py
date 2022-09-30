file_name = 'file/learning_python.txt' 
# file_name的路径如果是'learning_python.txt'，会默认在上一级菜单中创建learning_python.txt  
with open(file_name) as file_object:
    # 1
    # contents  =  file_object.read()
    # print(contents)
    # 2
    # for content in file_object:
    #     print(content.strip())
    lines  = file_object.readlines()

for line in lines:
    print(line.replace('Python', 'JavaScript').strip())