import math
def angleB(a,b,c):
    #ここから書きましょう
    pointA = Point(a)
    pointB = Point(b)
    pointC = Point(c)

    lineAB = Line(pointA, pointB)
    lineBC = Line(pointB, pointC)

    #内積を用いたcosThetaの公式
    #cosThetaForABC = abs(lineAB.a * lineBC.a + lineAB.by * lineBC.by) / math.sqrt(lineAB.a**2 + lineAB.by**2) * math.sqrt(lineBC.a**2 + lineBC.by**2)
    #ABC = math.degrees(math.acos(cosThetaForABC))

    if abs(lineAB.a*lineBC.a + lineAB.by*lineBC.by) == 0:
        return 90
    else:
        #tanThetaを用いた公式（直角の場合は使えないzeroDivisionError）
        tanTheta = abs(lineAB.a*lineBC.by - lineAB.by*lineBC.a) / abs(lineAB.a*lineBC.a + lineAB.by*lineBC.by)
        ABC = math.degrees(math.atan(tanTheta))


    return math.floor(ABC)

class Point:
    def __init__(self, xy):
        self.x = xy[0]
        self.y = xy[1]
        
class Line:
    def __init__(self, startPoint, endPoint):
        self.startPoint = startPoint
        self.endPoint = endPoint
        #長さ
        self.length = math.sqrt((startPoint.x - endPoint.x) ** 2 + (startPoint.y - endPoint.y) **2)
        #例外処置　x=0ならフラグ1 y=0ならフラグ2
        self.isSpecial = 0
        #yの次数
        self.by = -1
        #a 傾き　a = yの変化量/xの変化量
        #b y切片　b = y1 - a * x1
        #x=定数の場合（傾き0）
        if startPoint.x == endPoint.x:
            self.a = 1
            self.b = 0
            self.by = 0
            #y=0の場合
            if startPoint.y == 0 and endPoint.y == 0:
                self.isSpecial = 2
        #y=定数の場合（傾き0）
        elif startPoint.y == endPoint.y:
            self.a = 0
            self.b = startPoint.y
            self.by = 1
            #x=0の場合
            if self.b == 0:
                self.isSpecial = 1
        else:
            self.a = (startPoint.y - endPoint.y) / (startPoint.x - endPoint.x)  
            self.b = startPoint.y - (self.a * startPoint.x)

print(angleB([4, 3],[4,0], [0,0]))
print(angleB([0,0],[1,1],[1,0]))