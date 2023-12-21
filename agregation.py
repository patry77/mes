import numpy as np
from numpy import linalg
class agregation:
    def __init__(self, grid, globalData):
        self.grid = grid
        self.globalData = globalData
        self.dtau = 0
        self.t0 = np.zeros((len(self.grid.nodes), 1))
        for i in range(len(self.grid.nodes)):
            self.t0[i] = self.globalData.initialTemp
        self.step = self.globalData.simulationStepTime
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
    def tempSimulation(self):
        tauinitial = 0
        taufinal = self.globalData.simulationTime
        while tauinitial < taufinal:
            self.dtau += self.step
            H = self.H + self.C / self.step
            P = self.P + (self.C / self.step) @ self.t0
            self.t0 = linalg.solve(H, P)
            tauinitial += self.step
            print("dtau:  ", self.dtau, "  tmin:  ", min(self.t0), "  tmax:  ", max(self.t0))

