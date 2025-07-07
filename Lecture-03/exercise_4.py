print("Please select operation\n1. Add\n2. Subtract\n3. Multiply\n4. Divide")

select = int(input("Select operations form 1,2,3,4: "))
first = float(input("Enter first number: "))
second = float(input("Enter second number: "))

if select == 1:
    print(f"{first} + {second} = {first + second}")
elif select == 2:
    print(f"{first} - {second} = {first - second}")
elif select == 3:
    print(f"{first} * {second} = {first * second}")
elif select == 4:
    print(f"{first} / {second} = {first / second}")
else:
    print("Invalid input! Please select from 1,2,3,4.")