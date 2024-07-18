from graphics import *
allsprites = []
allforces = []

window = GraphWin(width = 500, height = 500)

window.setCoords(0, 0, 100, 100) # set the coordinates of the window; bottom left is (0, 0) and top right is (10, 10)



#* important component. allows things to act like 2D vectors while really just being 1D actors
class Force:
    vectorY = 0
    vectorX = 0
    
    @staticmethod 
    def addForce(sprite, newForce):
        index = allsprites.index(sprite)
        global allforces
        
        # vector addition
        allforces[index].vectorY += newForce.vectorY
        allforces[index].vectorX += newForce.vectorX
        
        
    
#* Class to calculate a forcefield around a particle. 
class ForceField:
    originX = 0
    originY = 0
    
    def updateInhabitants():
        global allsprites
        for i in allsprites:
            distance = i.distancesq()
            
            
            
        
#* important component
class Particle:
    # position components, previousX is vital to verlet calculation
    positionX = 75
    previousX = 50
    positionY = 50
    
    # determines size and how forces interact with the mass. 
    mass = 0
    
    point = object
    # determines generation of a forcefield
    forcefield = object
    # allows the average force calculation
    numberOfForces = 0

    def __init__(self, mass):
        self.mass = mass
        self.point = Circle(Point(self.positionX, self.positionY), self.mass)
        
        # appends self to a global list of all sprites on screen (allows for collision detection)
        allsprites.append(self)

    # overloading constructor to allow particles to generate forcefields
    def __init__(self, mass, fieldType):
        # call default constructor
        self(mass)
        
        # e for electric, g for gravitational
        if (fieldType == "e"):
            print('yay')
        elif (fieldType == "g"):
            print("ew")
            
    
    def draw(self):
        self.point.undraw()
        self.point.draw(window)
        self.point.setFill("black")

    def verlet(self, force):
        # prep canvas
        self.point.undraw()
        
        # applies the differential equation for step = s
        # x<s+1> = 1/2a^2 + (x<s-1> - x<s>)/2 + x<s> 
        # for both force vector components f.vectorY and f.vectorX 
        
        
        
        # wherein (referring to force.py and canvas documentation) right and up is positive.
        
        self.previousX = self.positionX
        self.positionX += force
        self.positionY += force
        self.point = Circle(Point(self.positionX, self.positionY), self.mass)
        self.draw()

    def distancesq(self, target):
        return (self.positionX -target.positionX)**2 + (self.y-target.positionY)**2
    
    # overload of distancesq for point
    def distancesq(self, point):
        return (self.positionX - point.x)**2 + (self.positionY - point.y)**2
    
    def isColliding(self):
        allsprites


#* execution script
p1 = Particle(mass = 1)

floor = Rectangle(Point(0,0), Point(10,100))
floor.setFill("black")

for i in allsprites:
    p1.draw()

def tick():
    p1.verlet(1)
    update(30)
    
