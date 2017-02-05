class Animail(object):
    def run(self):
        print("Animal is running")

class Dog(Animail):
    def run(self):
        print("Dog is running")

    def eat(self):
        print("Dog is eating")

class Cat(Animail):
    def run(self):
        print("Cat is running")
    def barker(self):
        print("Cat is barker")

class Tortoise(Animail):
    def run(self):
        print('Tortoise is running slowly...')

def run_twice(animal):
    animal.eat()
    animal.eat()

# run_twice(Tortoise())

class Timer(object):
    def eat(self):
        print('Start.....')
b = Timer()
run_twice(Timer())
print(isinstance(b,Animail))