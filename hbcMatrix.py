import math
from ElementUni import *
import numpy as np
from gauss import gauss

'''
Macierz Hbc - zmodifikowana macierz H, uwzgledniajaca warunki brzegowe
Wektor P - wektor globalny obciążeń, reprezentuje obciążenia na powierzchni, takie jak np. zewnetrzne strumienie ciepla
alfa - współczynnik wymiany ciepła
tot - temperatura otoczenia
klasa hbcMatrix - klasa reprezentujaca macierz Hbc i wektor P
klasa Surface - klasa reprezentujaca powierzchnie elementu zawierajaca funkcje ksztaltu
sposób wykorzystania warunków brzegowych:
    - jeżeli węzeł należy do powierzchni, na której występuje warunek brzegowy, to jego współczynnik przy temperaturze
    jest równy 1, a w wektorze P jest wartość temperatury, która jest wymuszona przez warunek brzegowy
    - jeżeli węzeł nie należy do powierzchni, na której występuje warunek brzegowy, to jego współczynnik przy temperaturze
    jest równy 0, a w wektorze P jest wartość temperatury, która jest wymuszona przez warunek brzegowy pomnożona
    przez współczynnik przy temperaturze
działanie programu krok po kroku:
    - tworzymy listę powierzchni elementu
    - dla każdej powierzchni obliczamy macierz Hbc i wektor P
    - sumujemy macierze Hbc i wektory P dla każdej powierzchni
    - dodajemy macierz Hbc do macierzy H
    - dodajemy wektor P do wektora P
'''


class Surface:
    def __init__(self, points, ksi, eta):
        self.ksi=ksi
        self.eta=eta
        self.points = points
        self.N = np.zeros((self.points, 4))
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
        self.uni=ElementUni(points)
        self.alfa=self.globalData.alfa
        self.tot=self.globalData.tot
        for i in range (len(self.grid.elements)):
            nodes = []
            self.hbclist = []
            self.plist = []
            for j in range(len(self.grid.elements[i].idlist)):
                for k in range(len(self.grid.nodes)):
                    if self.grid.elements[i].idlist[j] == self.grid.nodes[k].id:
                        nodes.append(self.grid.nodes[k])
            for j in range(len(self.surfacelist)):
                self.hbcM = np.zeros((4, 4))
                self.pM=np.zeros((4, 1))
                if(j==3):
                    self.L = math.sqrt(pow(nodes[j].x - nodes[0].x, 2) + pow(nodes[j].y - nodes[0].y, 2))
                    if(nodes[j].bc == 0 or nodes[0].bc == 0):
                        # print("pomijam")
                        continue
                else:
                    self.L = math.sqrt(pow(nodes[j].x - nodes[j+1].x, 2) + pow(nodes[j].y - nodes[j+1].y, 2))
                    if (nodes[j].bc == 0 or nodes[j+1].bc == 0):
                        # print("pomijam")
                        continue
                self.detJ = self.L / 2

                for k in range(points):
                    arr=[]
                    arr=np.array([[self.surfacelist[j].N[k][0]], [self.surfacelist[j].N[k][1]], [self.surfacelist[j].N[k][2]], [self.surfacelist[j].N[k][3]]])
                    self.hbcM+=arr @ arr.T*self.gauss.pointWeight[k]
                    self.pM+=arr*self.gauss.pointWeight[k]
                self.pM=self.pM*self.tot*self.detJ*self.alfa
                self.hbcM=self.hbcM*self.detJ*self.alfa
                self.plist.append(self.pM)
                self.hbclist.append(self.hbcM)
            hbc=np.zeros((4, 4))
            for j in range(len(self.hbclist)):
                hbc+=self.hbclist[j]
            self.grid.elements[i].Hbc=hbc
            p=np.zeros((4, 1))
            for j in range(len(self.plist)):
                p+=self.plist[j]
            self.grid.elements[i].P=p
    def returnGrid(self):
        return self.grid


