import math

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
                    self.N[i][j] = 0.25 * (1-self.ksi[i])*(1-self.eta[i])
                if j==1:
                    self.N[i][j] = 0.25 * (1+self.ksi[i])*(1-self.eta[i])
                if j==2:
                    self.N[i][j] = 0.25 * (1+self.ksi[i])*(1+self.eta[i])
                if j==3:
                    self.N[i][j] = 0.25 * (1-self.ksi[i])*(1+self.eta[i])



class hbcMatrix:
    def __init__(self, grid, points, globalData):
        self.grid=grid
        self.points=points
        self.gauss=gauss(points)
        self.surfacelist = []
        self.globalData=globalData
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
        # for i in range(len(self.surfacelist)):
        #     print("Surface: ")
        #     print(i)
        #     print(self.surfacelist[i].N)

        self.uni=ElementUni(points)
        # self.alfa=self.globalData.alfa
        self.alfa=25

        # self.tot=self.globalData.tot
        self.tot=1200
        self.hbclist=[]
        self.plist=[]
        element = grid.elements[0]
        nodes = []
        for j in range(len(grid.nodes)):
            if (grid.nodes[j].id in element.idlist):
                nodes.append(grid.nodes[j])
        for i in range(len(self.surfacelist)):
            self.hbcM = np.zeros((4, 4))
            self.pM=np.zeros((4, 1))
            if(i==3):
                self.L = math.sqrt(pow(nodes[i].x - nodes[0].x, 2) + pow(nodes[i].y - nodes[0].y, 2))
                if(nodes[i].bc == 0 or nodes[0].bc == 0):
                    print("pomijam")
                    continue
            else:
                self.L = math.sqrt(pow(nodes[i].x - nodes[i+1].x, 2) + pow(nodes[i].y - nodes[i+1].y, 2))
                if (nodes[i].bc == 0 or nodes[i+1].bc == 0):
                    print("pomijam")
                    continue
            self.detJ = self.L / 2

            for j in range(points):
                arr=[]
                arr=np.array([[self.surfacelist[i].N[j][0]], [self.surfacelist[i].N[j][1]], [self.surfacelist[i].N[j][2]], [self.surfacelist[i].N[j][3]]])
                self.hbcM+=self.alfa*np.matmul(arr, arr.transpose())*self.gauss.pointWeight[j]
                self.pM+=arr*self.gauss.pointWeight[j]
                print("arr")
                print(arr)
            # print("pM")
            # print(self.pM)
            self.pM=self.pM*self.tot*self.detJ*self.alfa
            self.hbcM=self.hbcM*self.detJ
            # print("hbc")
            # print(self.hbcM)
            # print("p")
            # print(self.pM)
            self.plist.append(self.pM)
            self.hbclist.append(self.hbcM)
        print("HBC")
        print(sum(self.hbclist))
        print("P")
        print(sum(self.plist))


