score1=float(input("Enter the score for test 1: "))
score2=float(input("Enter the score for test 2: "))
score3=float(input("Enter the score for test 3: "))

averagescore= (score1 + score2 + score3) / 3
print("The average score is: ",format (averagescore,'.1f'))

if averagescore > 95:
    print("Congratulation!")