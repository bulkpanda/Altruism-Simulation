""" IMPORTANT INTITIAL NOTES:
ACTIONS INCLUDED: Movement, capture, sharing, death, hunger
Range of interaction = 0.1
Game board size = 1x1
Number of animals = 100
Game board space per animal (GBS)= 0.01
Area of interaction (AOI) = pi*0.1^2 = 0.0314
Density = AOI/GBS = 3.14
Number of food = 20
Content of food = 5
Net inward food flux = 100
Net outward food flux = 100 (Assuming 100 percent survival)



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
            foodshared = self.food*self.a*(1/(2 + 100*abs(self.a - a)))*(1/float(n))
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

    def consume(self,hunger):
        self.food = self.food - hunger

        
class Food:
    """This class stores coordinates of food particles"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.near = []
        self.content = 5

    """This function finds the number of animals around self """
    def numberanimals(self, animals):

        for i in range(len(animals)):
            if norm(self, animals[i]) < R :
                self.near.append(i)

        return len(self.near)

    def capture(self, animals):

        n= len(self.near)
        for i in self.near:
            animals[i].food = animals[i].food + self.content/float(n)
            
        

"""This function calculates the distance between two objects (may be animal or food)"""
def norm(a,b):
    dis = math.sqrt( (a.x - b.x)**2 + (a.y - b.y)**2)
    return dis

"""Definitions end; code starts here"""
animals = []
foods = []
numberfood = 20
numberanimals = 100
iterations = 100
hunger = 1

"""This creates the initial array of animals"""
for i in range(numberanimals):
    b = Animal(random.random(),random.random(),10*random.random(),random.random())
    animals.append(b)

"""This initialises the array 'near' for each animal"""
for i in range(len(animals)):
    animals[i].numberanimals(animals)

"""This is the main simulation"""
for j in range(iterations):
    foods = []
    """Food generation for each iteration"""
    for i in range(numberfood):
        f = Food(random.random(),random.random())
        foods.append(f)

    """Capture Event"""
    for i in range(len(foods)):
        foods[i].numberanimals(animals)
        foods[i].capture(animals)
    
    """Share event"""
    randomlist = list(range(len(animals)))
    random.shuffle(randomlist)
    for i in randomlist:
        animals[i].share(animals)

    """Move event"""
    for i in range(len(animals)):
        animals[i].move()

    """Consumption Event"""
    for i in range(len(animals)):
        animals[i].consume(hunger)

    """Death"""
    iterate = 0
    while iterate < len(animals):
        if animals[iterate].food < 0:
            del animals[iterate]
        else:
            iterate = iterate + 1

    """Initialises array 'near' after every move event. For more information see comment above Animal.move(self) """
    for i in range(len(animals)):
        animals[i].numberanimals(animals)

    
    

lista = []
listnumber = []

for i in range(0,20):
    lista.append(i/20)
    listnumber.append(0)
    for j in range(len(animals)):
        if animals[j].a < i/20 and animals[j].a> (i/20-0.05):
            listnumber[i] = listnumber[i] + 1
            

plt.scatter(lista,listnumber)
plt.show()
