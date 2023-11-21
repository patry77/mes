from gauss import gauss
import numpy as np
class ElementUni:

    def __init__(self, points):
        self.pointQuantity = points
        self.dNdKsi = []
        self.dNdEta = []
        self.gauss = gauss(points)
        self.dNdEta = np.zeros((self.pointQuantity* self.pointQuantity, 4))
        self.dNdKsi = np.zeros((self.pointQuantity* self.pointQuantity, 4))

        for i in range(self.pointQuantity * self.pointQuantity):
            # print(i//self.pointQuantity)
            eta=self.gauss.pointPlace[i // self.pointQuantity]
            for j in range(4):
                if j == 0:
                    self.dNdKsi[i][j] = -0.25 * (1 - eta)
                if j == 1:
                    self.dNdKsi[i][j] = 0.25 * (1 - eta)
                if j == 2:
                    self.dNdKsi[i][j] = 0.25 * (1 + eta)
                if j == 3:
                    self.dNdKsi[i][j] = -0.25 * (1 + eta)

        for i in range(self.pointQuantity * self.pointQuantity):
            for j in range(4):
                if j == 0:
                    self.dNdEta[i][j] = -0.25 * (1 - self.gauss.pointPlace[i % self.pointQuantity])
                if j == 1:
                    self.dNdEta[i][j] = -0.25 * (1 + self.gauss.pointPlace[i % self.pointQuantity])
                if j == 2:
                    self.dNdEta[i][j] = 0.25 * (1 + self.gauss.pointPlace[i % self.pointQuantity])
                if j == 3:
                    self.dNdEta[i][j] = 0.25 * (1 - self.gauss.pointPlace[i % self.pointQuantity])

    def printdNdKSI(self):
        print("")
        print("dNdKSI: ")
        print(self.dNdKsi)

    def printdNdEta(self):
        print("")
        print("dNdEta: ")
        print(self.dNdEta)
