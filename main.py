import data
import loadData
import gauss
from ElementUni import ElementUni
from jacobian import jacobian
from hbcMatrix import *


if __name__ == '__main__':
    testnodes = [data.node(0, 0), data.node(0.025, 0), data.node(0.025, 0.025), data.node(0, 0.025)]
    elements = [data.element([1, 2, 3, 4])]
    grid=data.grid(elements, testnodes)
    # print(myGrid.elements[0].id[1])
    # print(myGrid.nodes[6].x)
    # gaussMes=gauss.gauss(2)
    # print(gaussMes.pointPlace)
    # print(gaussMes.pointWeight)
    # print(gauss.gaussMethod(1, 3))
    # uni = ElementUni(3)
    # uni.printdNdEta()
    # uni.printdNdKSI()
    # x=[0, 0.025, 0.025, 0]
    # y=[0, 0, 0.025, 0.025]
    # jacobian(4, x, y)
    loading=loadData.load_data("test.txt")
    # grid=data.grid(loading[2], loading[1])
    globaldata=loading[0]
    hbcMatrix(grid, 2, globaldata)
