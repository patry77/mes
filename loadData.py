import data
from data import *

def loadData(file):
    with open(file, 'r') as file:
        lines = file.read().splitlines()
    simulationTime, simulationStepTime, conductivity, alfa, tot, initialTemp, density, specificHeat, nodes, elements = lines
    return simulationTime, simulationStepTime, conductivity, alfa, tot, initialTemp, density, specificHeat, nodes, elements
def loadElements(file):
    elements = []
    with open(file, 'r') as file:
        lines = file.read().splitlines()
        for i in lines:
            i = i.split(",")
            int_list = []
            for y in i:
                integer = int(y)
                int_list.append(integer)
            elements.append(data.element(int_list))
    return elements
def loadNodes(file):
    nodes = []
    with open(file, 'r') as file:
        lines = file.read().splitlines()
        for i in lines:
            i = i.split(",")
            int_list = []
            for y in i:
                integer = float(y)
                int_list.append(integer)
            nodes.append(data.node(int_list[0], int_list[1]))
    return nodes

def load_data(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    global_data = None
    nodes = []
    elements = []
    nodes_number = 0
    elements_number = 0
    iteration = 0
    for line in lines:
        iteration += 1
        data = line.strip().split(' ')
        # print(data)
        if data[0] == "SimulationTime":
            simulationTime = int(data[1])
        elif data[0] == "SimulationStepTime":
            simulationStepTime = int(data[1])
        elif data[0] == "Conductivity":
            conductivity = int(data[1])
        elif data[0] == "Alfa":
            alfa = int(data[1])
        elif data[0] == "Tot":
            tot = int(data[1])
        elif data[0] == "InitialTemp":
            initialTemp = int(data[1])
        elif data[0] == "Density":
            density = int(data[1])
        elif data[0] == "SpecificHeat":
            specificHeat = int(data[1])
        elif data[0] == "Nodes":
            nodes_number = int(data[2])
        elif data[0] == "Elements":
            elements_number = int(data[2])
        elif data[0] == "*Node":
            for i in range(iteration, iteration+nodes_number):
                node_data = lines[i].strip().split(',')
                # print(node_data)
                nodes.append(node(float(node_data[1]), float(node_data[2])))
        elif data[0] == "*Element,":
            for i in range(iteration, iteration+elements_number):
                element_data = lines[i].strip().split(',')
                int_list = list(map(int, [i.strip() for i in element_data]))
                # print(element_data)
                elements.append(element(int_list))
    return globalData(simulationTime, simulationStepTime, conductivity, alfa, tot, initialTemp, density, specificHeat), nodes, elements