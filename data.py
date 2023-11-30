class globalData:
    def __init__(self, simulationTime, simulationStepTime, conductivity, alfa, tot, initialTemp, density, specificHeat):
        self.simulationTime = simulationTime
        self.simulationStepTime = simulationStepTime
        self.conductivity = conductivity
        self.alfa = alfa
        self.tot = tot
        self.initialTemp = initialTemp
        self.density = density
        self.specificHeat = specificHeat

class node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.bc=0

class element:
    def __init__(self, id):
        self.id = id

class grid:
    def __init__(self, elements, nodes):
        self.elements = elements
        self.nodes = nodes
