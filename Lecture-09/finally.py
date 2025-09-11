try:
    numerator = float(input("Enter the numerator: "))
    denomenator = float(input("Enter the denomenator: "))
    result = numerator / denomenator
    print(f"The result is: {result}")

except ZeroDivisionError:
    print("Error: cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter numeric values.")
finally:
    print("Execution completed, whether an exception occurred or not.")
print("End of program")