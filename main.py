import data
import loadData
import gauss
from ElementUni import ElementUni


if __name__ == '__main__':
    # myGrid=data.grid(loadData.loadElements("element.txt"), loadData.loadNodes("node.txt"))
    # print(myGrid.elements[0].id)
    # gaussMes=gauss.gauss(4)
    # print(gaussMes.pointPlace)
    # print(gaussMes.pointWeight)
    # print(gauss.gaussMethod(1, 3))
    uni = ElementUni(2)
    uni.printdNdEta()
    uni.printdNdKSI()