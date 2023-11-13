import numpy as np
from data import grid
from ElementUni import ElementUni
class jacobian:
    def __init__(self, points, x, y):
        self.x=x
        self.y=y
        self.points=points*points
        elementuni=ElementUni(points*points)
        H=np.zeros((self.points, self.points))
        dndy = np.zeros((self.points, self.points))
        dndx = np.zeros((self.points, self.points))
        for i in range(points):
            for j in range(points):
                dxdeta = 0
                dydeta = 0
                dxdksi = 0
                dydksi = 0
                for k in range(4):
                    dxdeta += self.x*elementuni.dNdEta[j][k]
                    dxdksi += self.x*elementuni.dNdKsi[j][k]
                    dydeta += self.y*elementuni.dNdEta[j][k]
                    dydksi += self.y*elementuni.dNdKsi[j][k]
                jMatrix = [[dxdksi, dydksi], [dxdeta, dydeta]]
                detjmatrix = np.linalg.det(jMatrix)


