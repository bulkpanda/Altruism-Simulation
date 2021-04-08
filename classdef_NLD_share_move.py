import random
import math
from matplotlib import pyplot as plt

R = 0.1

class Animal:
    """This class stores coordinates, food and evolution parameter(a) for the animal"""
    def __init__(self,x,y,food,a):
        self.x = x
        self.y = y
        self.a = a
        self.food = food
        self.r = 0.1
        self.near = []

    """This function finds the number of animals around self, note that 'animals' is a list of animals. Also initialises array 'near' """
    def numberanimals(self, animals):

        self.near = []
        
        for i in range(len(animals)) :
            if norm(self,animals[i]) < R and id(self) != id(animals[i]):
                self.near.append(i)

        return len(self.near)

    """This calculates food shared to another animal having sharing parameter a if there are n total animals around current animal"""
    def sharingfunc(self, a, n):
        if n>0:
            foodshared = self.food*self.a*(1/(2 + 10*abs(self.a - a)))*(1/float(n))
        else:
            foodshared = 0

        return foodshared

    """This shares food that self has with other animals"""
    def share(self, animals):
        n = len(self.near)
        foodshared = 0
        
        for i in self.near:
            animals[i].food = animals[i].food + self.sharingfunc(animals[i].a,n)
            foodshared = foodshared + self.sharingfunc(animals[i].a,n)

        self.food = self.food - foodshared
        print(foodshared)

    """This moves the animal to another point in a radius r around itself."""
    """IMPORTANT NOTE: After very call of move, numberanimals must be called to initialise the array near"""
    def move(self):
        theta = 2*math.pi*random.random()
        """Theta is the angle the animal is going to move"""
        radius = R*random.random()
        """radius is the distance the animal will move"""
        self.x  = self.x + math.cos(theta)*radius
        self.y  = self.y + math.sin(theta)*radius

        
class Food:
    """This class stores coordinates of food particles"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.near = []

    """This function finds the number of animals around self """
    def numberanimals(self, animals):

        for i in range(len(animals)):
            if norm(self, animals[i]) < R :
                self.near.append[i]

        return len(self.near)
            
        

"""This function calculates the distance between two objects (may be animal or food)"""
def norm(a,b):
    dis = math.sqrt( (a.x - b.x)**2 + (a.y - b.y)**2)
    return dis

"""Definitions end; code starts here"""
animals = []

for i in range(50):
    b = Animal(random.random(),random.random(),random.random(),random.random())
    animals.append(b)

for i in range(len(animals)):
    animals[i].numberanimals(animals)

for i in range(100):
    randomlist = list(range(len(animals)))
    random.shuffle(randomlist)
    for i in randomlist:
        animals[i].share(animals)

    for i in range(len(animals)):
        animals[i].move()

    for i in range(len(animals)):
        animals[i].numberanimals(animals)

lista = []
listfood = []

for i in range(len(animals)):
    lista.append(animals[i].a)
    listfood.append(animals[i].food)

plt.scatter(lista,listfood)
plt.show()
