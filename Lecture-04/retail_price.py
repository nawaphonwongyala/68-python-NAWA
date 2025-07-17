keep_going = 'y'
while keep_going.lower() == 'y':
    wholecost = float(input('Enter the item\'s wholesale cost: '))
    retailprice = wholecost * 2.5
    print(f'Retail price: ${retailprice:.2f}')
    keep_going = input('Do yo want to continue? (Enter y for yes): ')