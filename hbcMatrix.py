import numpy as np
from gauss import gauss
from ElementUni import *
class Surface:
    def __init__(self, points, ksi, eta):
        self.ksi=ksi
        self.eta=eta
        self.points = points
        self.N = np.zeros((self.points, 4))
        # self.gauss = gauss(points)
        for i in range(self.points):
            for j in range(4):
                if j==0:
                    self.N[i][j] = 0.25 * (1-self.ksi[i % points])*(1-self.eta[i // points])
                if j==1:
                    self.N[i][j] = 0.25 * (1+self.ksi[i % points])*(1-self.eta[i // points])
                if j==2:
                    self.N[i][j] = 0.25 * (1+self.ksi[i % points])*(1+self.eta[i // points])
                if j==3:
                    self.N[i][j] = 0.25 * (1-self.ksi[i % points])*(1+self.eta[i // points])



class hbcMatrix:
    def __init__(self, x ,y, points):
        self.points=points
        self.x=x
        self.y=y
        self.gauss=gauss(points)
        self.surfacelist = []
        for i in range(4):
            ksi=[]
            eta=[]
            if(i%2 == 0):
                ksi=self.gauss.pointPlace
                for j in range(points):
                    eta.append(i-1)
            else:
                eta=self.gauss.pointPlace
                for j in range(points):
                    ksi.append(2-i)
            self.surfacelist.append(Surface(points,ksi,eta))
        for i in range(len(self.surfacelist)):
            print("Surface: ")
            print(i)
            print(self.surfacelist[i].N)

        self.uni=ElementUni(points)
        self.alfa=25
        self.detJ=0.0125
        self.hbclist=[]
        for i in range(len(self.surfacelist)):
            self.hbcM = np.zeros((4, 4))
            for j in range(points):
                arr=[]
                arr=np.array([[self.surfacelist[i].N[j][0]], [self.surfacelist[i].N[j][1]], [self.surfacelist[i].N[j][2]], [self.surfacelist[i].N[j][3]]])
                self.hbcM+=self.alfa*np.matmul(arr, arr.transpose())*self.gauss.pointWeight[j]
            self.hbcM=self.hbcM*self.detJ
            print("hbc")
            print(self.hbcM)
            self.hbclist.append(self.hbcM)
        print("HBC")
        print(sum(self.hbclist))

hbcMatrix(2, 2, 2)
