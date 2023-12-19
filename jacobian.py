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
            tmpC=[]
            for i in range(pointsSq):
                tmpHx=np.array([[dNdx[i][0]], [dNdx[i][1]], [dNdx[i][2]], [dNdx[i][3]]])
                tmpHy=np.array([[dNdy[i][0]], [dNdy[i][1]], [dNdy[i][2]], [dNdy[i][3]]])
                tmpN = np.array([[elementuni.NTab[i][0]], [elementuni.NTab[i][1]], [elementuni.NTab[i][2]], [elementuni.NTab[i][3]]])
                det=1/detJMatrix[i]
                k = self.globalData.conductivity
                ipC = self.globalData.density * self.globalData.specificHeat * tmpN @ tmpN.T * det
                ipH=k*(tmpHx @ tmpHx.T + tmpHy @ tmpHy.T)*det
                tmpH.append(ipH)
                tmpC.append(ipC)
            H=np.zeros((4, 4))
            C=np.zeros((4, 4))
            for i in range(pointsSq):
                H+=tmpH[i]*gaussg.pointWeight[i//points]*gaussg.pointWeight[i%points]
                C+=tmpC[i]*gaussg.pointWeight[i//points]*gaussg.pointWeight[i%points]
            self.grid.elements[l].H=H
            self.grid.elements[l].C=C
    def returnGrid(self):
        return self.grid




