import data
import loadData
import gauss
from ElementUni import ElementUni
from jacobian import jacobian


if __name__ == '__main__':
    myGrid=data.grid(loadData.loadElements("element.txt"), loadData.loadNodes("node.txt"))
    # print(myGrid.elements[0].id[1])
    # print(myGrid.nodes[6].x)
    # gaussMes=gauss.gauss(2)
    # print(gaussMes.pointPlace)
    # print(gaussMes.pointWeight)
    # print(gauss.gaussMethod(1, 3))
    # uni = ElementUni(3)
    # uni.printdNdEta()
    # uni.printdNdKSI()
    x=[0, 0.025, 0.025, 0]
    y=[0, 0, 0.025, 0.025]
    jacobian(4, x, y)