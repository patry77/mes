from numpy.linalg import linalg

import data
import loadData
import gauss
from ElementUni import ElementUni
from jacobian import *
from hbcMatrix import *
from agregation import *


if __name__ == '__main__':
    testnodes = [data.node(1,0, 0), data.node(2,0.025, 0), data.node(3,0.025, 0.025), data.node(4,0, 0.025)]
    # elements = [data.element([1, 2, 3, 4])]
    # grid=data.grid(elements, testnodes)
    # print(myGrid.elements[0].id[1])
    # print(myGrid.nodes[6].x)
    # gaussMes=gauss.gauss(2)
    # print(gaussMes.pointPlace)
    # print(gaussMes.pointWeight)
    # print(gauss.gaussMethod(1, 3))
    # uni = ElementUni(3)
    # uni.printdNdEta()
    # uni.printdNdKSI()
    # uni.printNtab()
    # x=[0, 0.025, 0.025, 0]
    # y=[0, 0, 0.025, 0.025]
    loading=loadData.load_data("test_mix/.txt")
    grid=data.grid(loading[2], loading[1])
    globaldata=loading[0]
    hbcp=hbcMatrix(grid, 2, globaldata)
    grid=hbcp.returnGrid()
    h=localHMatrix(2, grid, globaldata)
    grid=h.returnGrid()
    agregation=agregation(grid, globaldata)
    agregation.tempSimulation()