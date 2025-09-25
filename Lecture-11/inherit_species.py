class dog:
    species = 'mammal'

    def calage(self,age):
        print('Dog age is {}'.format(age*3))

class somebread(dog):
    pass

class someotherbread(dog):
    species = 'reptile'
    def calage(self, age):
        print('Dog age is {}'.format(age*4))

frank = somebread()
print(frank.species)
frank.calage(5)

beans = someotherbread()
print(beans.species)
beans.calage(5)