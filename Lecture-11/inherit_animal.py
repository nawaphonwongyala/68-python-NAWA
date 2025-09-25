class animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "Some sound"
class dog(animal):
    def speak(self):
        return f"{self.name} says woof!"
class cat(animal):
    def speak(self):
        return f"{self.name} says meow!"
Dog = dog("Buddy")
Cat = cat("Whiskers")

print(Dog.speak())
print(Cat.speak())