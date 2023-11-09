import math


class gauss:
    pointPlace = []
    pointWeight = []
    points = 0

    def __init__(self, points):
        self.points = points
        if self.points == 2:
            self.pointPlace.append(-1 * math.sqrt(1 / 3))
            self.pointPlace.append(math.sqrt(1 / 3))
            self.pointWeight.append(1)
            self.pointWeight.append(1)
        if self.points == 3:
            self.pointPlace.append(-1 * math.sqrt(3 / 5))
            self.pointPlace.append(0)
            self.pointPlace.append(math.sqrt(3 / 5))
            self.pointWeight.append(5 / 9)
            self.pointWeight.append(8 / 9)
            self.pointWeight.append(5 / 9)
        if self.points == 4:
            self.pointPlace.append(-1 * math.sqrt((3 / 7) + (2 / 7) * math.sqrt(6 / 5)))
            self.pointPlace.append(-1 * math.sqrt((3 / 7) - (2 / 7) * math.sqrt(6 / 5)))
            self.pointPlace.append(math.sqrt((3 / 7) - (2 / 7) * math.sqrt(6 / 5)))
            self.pointPlace.append(math.sqrt((3 / 7) + (2 / 7) * math.sqrt(6 / 5)))
            self.pointWeight.append(18 - math.sqrt(30) / 36)
            self.pointWeight.append(18 + math.sqrt(30) / 36)
            self.pointWeight.append(18 + math.sqrt(30) / 36)
            self.pointWeight.append(18 - math.sqrt(30) / 36)


def fun1d(x):
    return 5 * x * x + 3 * x + 6


def fun2d(x, y):
    return 5 * x * x * y * y + 3 * x * y + 6


def gaussMethod(dimen, points):
    gaussPoints = gauss(points)
    print(gaussPoints.pointWeight[1])
    result = 0
    if dimen == 1:
        for i in range(points):
            result += fun1d(gaussPoints.pointPlace[i]) * gaussPoints.pointWeight[i]
    if dimen == 2:
        for i in range(points):
            for j in range(points):
                result += fun2d(gaussPoints.pointPlace[i], gaussPoints.pointPlace[j]) * gaussPoints.pointWeight[i] * \
                          gaussPoints.pointWeight[j]
    return result
