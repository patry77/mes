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
    def tempSimulation(self, fileName):
        tauinitial = 0
        fileNum=1
        taufinal = self.globalData.simulationTime
        while tauinitial < taufinal:
            self.dtau += self.step
            H = self.H + self.C / self.step
            P = self.P + (self.C / self.step) @ self.t0
            self.t0 = linalg.solve(H, P)
            tauinitial += self.step
            print("dtau:  ", self.dtau, "  tmin:  ", min(self.t0), "  tmax:  ", max(self.t0))
            file = open(f"{fileName}/Foo{fileNum}.vtk", "w")
            file.write("# vtk DataFile Version 2.0\n")
            file.write("Unstructured Grid Example\n")
            file.write("ASCII\n")
            file.write("DATASET UNSTRUCTURED_GRID\n")
            file.write("POINTS " + str(len(self.grid.nodes)) + " float\n")
            for i in range(len(self.grid.nodes)):
                file.write(str(self.grid.nodes[i].x) + " " + str(self.grid.nodes[i].y) + " 0\n")
            file.write("CELLS " + str(len(self.grid.elements)) + " " + str(len(self.grid.elements) * 5) + "\n")
            for i in range(len(self.grid.elements)):
                file.write("4 " + str(self.grid.elements[i].idlist[0] - 1) + " " + str(self.grid.elements[i].idlist[1] - 1) + " " + str(self.grid.elements[i].idlist[2] - 1) + " " + str(self.grid.elements[i].idlist[3] - 1) + "\n")
            file.write("CELL_TYPES " + str(len(self.grid.elements)) + "\n")
            for i in range(len(self.grid.elements)):
                file.write("9\n")
            file.write("POINT_DATA " + str(len(self.grid.nodes)) + "\n")
            file.write("SCALARS Temp float 1\n")
            file.write("LOOKUP_TABLE default\n")
            for i in range(len(self.grid.nodes)):
                file.write(str(self.t0[i][0]) + "\n")
            file.close()
            fileNum+=1


