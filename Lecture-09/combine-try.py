try:
    value = int(input("Enter a number: "))
    result = 10 / value
except ValueError:
    print("Error: Invalid input. Please enter number.")
except ZeroDivisionError:
    print("Error: cannot divide by zero.")
else:
    print(f"The result is {result}")
finally:
    print("Execution completed")