with open('employees.txt','r') as file:
    lines = file.readlines()
for line in range(0,len(lines),3):
        name = lines[line].strip()
        id = lines[line + 1].strip()
        dept = lines[line + 2].strip()
        print(f'Name: {name}')
        print(f'ID: {id}')
        print(f'Dept: {dept}')