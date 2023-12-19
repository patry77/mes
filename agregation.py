import numpy as np
from numpy import linalg
class agregation:
    def __init__(self, grid, globalData):
        self.grid = grid
        self.globalData = globalData
        self.H = np.zeros((len(self.grid.nodes), len(self.grid.nodes)))
        self.P = np.zeros((len(self.grid.nodes), 1))
        self.C = np.zeros((len(self.grid.nodes), len(self.grid.nodes)))
        for i in range(len(self.grid.elements)):
            localH = self.grid.elements[i].H + self.grid.elements[i].Hbc
            for j in range(4):
                self.P[self.grid.elements[i].idlist[j] - 1] += self.grid.elements[i].P[j]
                for k in range(4):
                    self.H[self.grid.elements[i].idlist[j] - 1][self.grid.elements[i].idlist[k] - 1] += localH[j][k]
                    self.C[self.grid.elements[i].idlist[j] - 1][self.grid.elements[i].idlist[k] - 1] += self.grid.elements[i].C[j][k]
        print("H")
        print(self.H)
        print("C")
        print(self.C)
        print("P")
        print(self.P)
        print("T")
        print(linalg.solve(self.H, self.P))
