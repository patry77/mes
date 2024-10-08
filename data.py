import numpy as np
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
    def __init__(self, id, x, y):
        self.id=id
        self.x = x
        self.y = y
        self.bc=0

class element:
    def __init__(self, id, idlist):
        self.id = id
        self.idlist=idlist
        self.H=np.zeros((4, 4))
        self.Hbc=np.zeros((4, 4))
        self.P=np.zeros((4, 1))
        self.C=np.zeros((4, 4))

class grid:
    def __init__(self, elements, nodes):
        self.elements = elements
        self.nodes = nodes
