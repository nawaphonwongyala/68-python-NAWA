heroes = ['Ironman','Thor','Hulk','Spiderman']

def show_heroes():
    print("Current heroes: ")
for hero in heroes:
    print('-',hero)

def add_heroes(name):
    heroes.append(name)
    print(f"{name} added")

def insert_heroes(index, name):
    heroes.insert(index, name)
    print(f"{name} inserted in position {index}")

def remove_heroes(name):
    heroes.remove(name)
    print(f"{name} has been removed")

def sort_heroes():
    heroes.sort
    
    