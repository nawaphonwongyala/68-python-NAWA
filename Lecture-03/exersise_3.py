hour = float(input("Enter the number of hours worked: "))
rate = float(input("Enter the  hourly pay rate: "))

if hour > 40:
    pay = ((hour - 40) * 1.5 * rate) + (40 * rate)
else:
    pay = (hour * rate)

print ("The gross pay is",pay)