counter = 0
def increment():
    global counter
    counter += 1
increment()
increment()
print(f'counter increment is: {counter}')