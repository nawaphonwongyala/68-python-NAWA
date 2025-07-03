weight = input("Enter your weight in kilograms: ")
weight = float(weight)

height = input("Enter your height in meters: ")
height = float(height)

bmi = weight / (height * height)
print ("your BMI is ", format(bmi,'.2f'))