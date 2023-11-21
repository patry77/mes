import numpy as np
from data import grid
from ElementUni import ElementUni
from gauss import gauss
class jacobian:
    def __init__(self, points, x, y):
        self.x=x
        self.y=y
        self.points=points
        # self.grid=grid
        gaussg=gauss(points)
        elementuni=ElementUni(self.points)
        pointsSq=points**2
        detJMatrix=[]
        k=30
        dNdx=np.zeros((pointsSq, 4))
        dNdy=np.zeros((pointsSq, 4))
        for i in range(pointsSq):
            dxdeta = 0
            dydeta = 0
            dxdksi = 0
            dydksi = 0
            for j in range(4):
                dxdeta += self.x[j]*elementuni.dNdEta[i][j]
                dxdksi += self.x[j]*elementuni.dNdKsi[i][j]
                dydeta += self.y[j]*elementuni.dNdEta[i][j]
                dydksi += self.y[j]*elementuni.dNdKsi[i][j]
            jMatrix = np.array([[dxdksi, dydksi], [dxdeta, dydeta]])
            # print(jMatrix)
            detJMatrix.append(1/np.linalg.det(jMatrix))
            # elementuniKsitab = np.zeros((pointsSq, pointsSq))
            # elementuniEtatab = np.zeros((pointsSq, pointsSq))
            # for j in range(pointsSq):
            #     for k in range(pointsSq):
            #         elementuniKsitab[i][j] = elementuni.dNdKsi[i][j]
            #         elementuniEtatab[i][j] = elementuni.dNdEta[i][j]

            inverseJMatrix = np.array([[dydeta, -dydksi], [-dxdeta, dxdksi]])
            # print(inverseJMatrix)
            for j in range(4):
                print(np.array([[elementuni.dNdKsi[i][j]], [elementuni.dNdEta[i][j]]]))
                helpTab = np.matmul((detJMatrix[i]*inverseJMatrix), np.array([[elementuni.dNdKsi[i][j]], [elementuni.dNdEta[i][j]]]))
                dNdx[i][j] = helpTab[0][0]
                dNdy[i][j] = helpTab[1][0]
        # print(dxdeta)
        # print(dxdksi)
        print(dNdx)
        # print(dNdy)
        tmpH=[]
        for i in range(pointsSq):
            tmpHx=np.array([[dNdx[i][0]], [dNdx[i][1]], [dNdx[i][2]], [dNdx[i][3]]])
            tmpHy=np.array([[dNdy[i][0]], [dNdy[i][1]], [dNdy[i][2]], [dNdy[i][3]]])
            ipH=k*(np.matmul(tmpHx, tmpHx.transpose()) + np.matmul(tmpHy, tmpHy.transpose()))*1/detJMatrix[i]
            # print(ipH)
            tmpH.append(ipH)
        # print(tmpH)
        H=np.zeros((4, 4))
        for i in range(pointsSq):
            H+=tmpH[i]*gaussg.pointWeight[i//points]*gaussg.pointWeight[i%points]
        # print(H)


