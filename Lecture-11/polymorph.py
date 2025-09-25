class animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")
    
class dog(animal):
    def speak(self):
        return "Woof!"

class cat(animal):
    def speak(self):
        return "Meow!"

def make_animal_speak(animal):
    print(animal.speak())

Dog = dog()
Cat = cat()

make_animal_speak(Dog)
make_animal_speak(Cat)