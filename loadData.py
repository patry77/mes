import data

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