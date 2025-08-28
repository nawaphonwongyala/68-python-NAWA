with open('example.txt','r') as file:
    contents = file.readline()
    while contents:
        print(contents.strip())
        contents = file.readline()