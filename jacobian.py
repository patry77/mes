import numpy as np
from ElementUni import ElementUni
from gauss import gauss
class localHMatrix:
    def __init__(self, points, grid, globalData):
        self.points=points
        self.grid=grid
        self.globalData=globalData
        gaussg=gauss(points)
        elementuni=ElementUni(self.points)
        pointsSq=points**2

        for l in range(len(self.grid.elements)):
            nodes=[]
            detJMatrix = []
            dNdx = np.zeros((pointsSq, 4))
            dNdy = np.zeros((pointsSq, 4))
            for j in range(len(self.grid.elements[l].idlist)):
                for k in range(len(self.grid.nodes)):
                    if self.grid.elements[l].idlist[j] == self.grid.nodes[k].id:
                        nodes.append(self.grid.nodes[k])
            for i in range(pointsSq):
                dxdeta = 0
                dydeta = 0
                dxdksi = 0
                dydksi = 0
                for j in range(4):
                    dxdeta += nodes[j].x*elementuni.dNdEta[i][j]
                    dxdksi += nodes[j].x*elementuni.dNdKsi[i][j]
                    dydeta += nodes[j].y*elementuni.dNdEta[i][j]
                    dydksi += nodes[j].y*elementuni.dNdKsi[i][j]
                jMatrix = np.array([[dxdksi, dydksi], [dxdeta, dydeta]])
                detJMatrix.append(1/np.linalg.det(jMatrix))
                inverseJMatrix = np.array([[dydeta, -dydksi], [-dxdeta, dxdksi]])
                for j in range(4):
                    helpTab = np.matmul((detJMatrix[i]*inverseJMatrix), np.array([[elementuni.dNdKsi[i][j]], [elementuni.dNdEta[i][j]]]))
                    dNdx[i][j] = helpTab[0][0]
                    dNdy[i][j] = helpTab[1][0]

            tmpH=[]
            for i in range(pointsSq):
                tmpHx=np.array([[dNdx[i][0]], [dNdx[i][1]], [dNdx[i][2]], [dNdx[i][3]]])
                tmpHy=np.array([[dNdy[i][0]], [dNdy[i][1]], [dNdy[i][2]], [dNdy[i][3]]])
                det=1/detJMatrix[i]
                k = self.globalData.conductivity
                ipH=k*(tmpHx @ tmpHx.T + tmpHy @ tmpHy.T)*det
                # ipMxH = k * ((mxDNdX @ mxDNdX.T + (mxDNdY @ mxDNdY.T)) * detTab[i]
                tmpH.append(ipH)
            H=np.zeros((4, 4))
            for i in range(pointsSq):
                H+=tmpH[i]*gaussg.pointWeight[i//points]*gaussg.pointWeight[i%points]
            self.grid.elements[l].H=H
    def returnGrid(self):
        return self.grid


import math

import numpy as np
from gauss import gauss
from ElementUni import *
class Surface:
    def __init__(self, points, ksi, eta):
        self.ksi=ksi
        self.eta=eta
        # print("ksi")
        # print(ksi)
        # print("eta")
        # print(eta)
        self.points = points
        self.N = np.zeros((self.points, 4))
        # self.gauss = gauss(points)
        for i in range(self.points):
            for j in range(4):
                if j==0:
                    self.N[i][j] = 0.25 * (1-self.ksi[i])*(1-self.eta[i])
                if j==1:
                    self.N[i][j] = 0.25 * (1+self.ksi[i])*(1-self.eta[i])
                if j==2:
                    self.N[i][j] = 0.25 * (1+self.ksi[i])*(1+self.eta[i])
                if j==3:
                    self.N[i][j] = 0.25 * (1-self.ksi[i])*(1+self.eta[i])



class localCMatrix:
    def __init__(self, points, grid, globalData):
        self.points=points
        self.grid=grid
        self.globalData=globalData
        gaussg=gauss(points)
        elementuni=ElementUni(self.points)
        pointsSq=points**2

        for l in range(len(self.grid.elements)):
            nodes=[]
            detJMatrix = []
            dNdx = np.zeros((pointsSq, 4))
            dNdy = np.zeros((pointsSq, 4))
            for j in range(len(self.grid.elements[l].idlist)):
                for k in range(len(self.grid.nodes)):
                    if self.grid.elements[l].idlist[j] == self.grid.nodes[k].id:
                        nodes.append(self.grid.nodes[k])
            for i in range(pointsSq):
                dxdeta = 0
                dydeta = 0
                dxdksi = 0
                dydksi = 0
                for j in range(4):
                    dxdeta += nodes[j].x*elementuni.dNdEta[i][j]
                    dxdksi += nodes[j].x*elementuni.dNdKsi[i][j]
                    dydeta += nodes[j].y*elementuni.dNdEta[i][j]
                    dydksi += nodes[j].y*elementuni.dNdKsi[i][j]
                jMatrix = np.array([[dxdksi, dydksi], [dxdeta, dydeta]])
                detJMatrix.append(1/np.linalg.det(jMatrix))
                inverseJMatrix = np.array([[dydeta, -dydksi], [-dxdeta, dxdksi]])
                for j in range(4):
                    helpTab = np.matmul((detJMatrix[i]*inverseJMatrix), np.array([[elementuni.dNdKsi[i][j]], [elementuni.dNdEta[i][j]]]))
                    dNdx[i][j] = helpTab[0][0]
                    dNdy[i][j] = helpTab[1][0]

            tmpC=[]
            for i in range(pointsSq):
                tmpCx=np.array([[dNdx[i][0]], [dNdx[i][1]], [dNdx[i][2]], [dNdx[i][3]]])
                tmpCy=np.array([[dNdy[i][0]], [dNdy[i][1]], [dNdy[i][2]], [dNdy[i][3]]])
                ro = self.globalData.density
                cp = self.globalData.specificHeat
                det=1/detJMatrix[i]
                ipC=ro*cp*(tmpCx @ tmpCx.T + tmpCy @ tmpCy.T)*det
                # ipMxH = k * ((mxDNdX @ mxDNdX.T + (mxDNdY @ mxDNdY.T)) * detTab[i]
                tmpC.append(ipC)
            C=np.zeros((4, 4))
            for i in range(pointsSq):
                C+=tmpC[i]*gaussg.pointWeight[i//points]*gaussg.pointWeight[i%points]
            # self.grid.elements[l].C=C
            print("C")
            print(C)