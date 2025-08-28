num_emps = int(input('How many emps rec you want?: '))
with open('employees.txt', 'w') as emp_file:
    for count in range(1, num_emps + 1):
        print('Enter data for emps: ',count, sep='')
        name = input('Name: ')
        id_num = input('ID number: ')
        dept = input('Department: ')

        emp_file.write(name + '\n')
        emp_file.write(id_num + '\n')
        emp_file.write(dept + '\n')
        print()
print('Employee rec written to employees.txt')