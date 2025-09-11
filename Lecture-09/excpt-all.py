try:
    value = int(input("Enter a number: "))
    result = 10 / value
    print(f"result is {result}")
except Exception as e:
    print(f"An erro occurred: {e}")
print("End of program")