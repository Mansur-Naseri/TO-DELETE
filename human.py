class Human:

   #class atrribute, constant
   MAX_ENERGY = 100

def __init__(self,  name="human", age= 0):
        self.name = "human"
        self.age = age
        self.energy = Human.MAX_ENERGY

def __repr__(self):
    return f"human(name={self.name}, age={self.age}, energey={self.energy}):"

def __str__(self):
    return  f" My name is {self.name} and i am {self.age} years old, and my energy is {self.energy}"

if __name__ == "__main__":
    person1 = Human()
    person1.__repr__()


