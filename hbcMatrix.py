import numpy as np
from gauss import gauss
class Surface:
    def __init__(self, points):
        self.points = points
        self.N = np.zeros((self.points, 4))
        self.gauss = gauss(points)
        for i in range(self.points):
            for j in range(4):
                if j==0:
                    self.N[i][j] = 0.25 * (1-self.gauss.pointPlace[i % points])*(1-self.gauss.pointPlace[i // points])
                if j==1:
                    self.N[i][j] = 0.25 * (1+self.gauss.pointPlace[i % points])*(1-self.gauss.pointPlace[i // points])
                if j==2:
                    self.N[i][j] = 0.25 * (1+self.gauss.pointPlace[i % points])*(1+self.gauss.pointPlace[i // points])
                if j==3:
                    self.N[i][j] = 0.25 * (1-self.gauss.pointPlace[i % points])*(1+self.gauss.pointPlace[i // points])
