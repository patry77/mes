import data
from data import *
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
                nodes.append(node(int(node_data[0]),float(node_data[1]), float(node_data[2])))
        elif data[0] == "*Element,":
            nodeid=[]
            for i in range(iteration, iteration+elements_number):
                element_data = lines[i].strip().split(',')
                int_list = list(map(int, [i.strip() for i in element_data]))
                for i in range(1, len(int_list)):
                    nodeid.append(int_list[i])
                elements.append(element(int_list, nodeid))
                nodeid=[]
        elif data[0] == "*BC":
            bc_data = lines[iteration].strip().split(',')
            bc_data = list(map(int, [i.strip() for i in bc_data]))
            for i in range(len(nodes)):
                if nodes[i].id in bc_data:
                    nodes[i].bc = 1

    return globalData(simulationTime, simulationStepTime, conductivity, alfa, tot, initialTemp, density, specificHeat), nodes, elements