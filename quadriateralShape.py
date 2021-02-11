import math
def getShapeType(ax,ay,bx,by,cx,cy,dx,dy):
    #ここから書きましょう
    message = ""
    pointA = Point(ax, ay)
    pointB = Point(bx, by)
    pointC = Point(cx, cy)
    pointD = Point(dx, dy)
    
    #同じ座標に位置する点がある
    points = [pointA, pointB, pointC, pointD]
    for i in range(4):
        for j in range(4):
            if i == j:
                continue
            if points[i].x == points[j].x and points[i].y == points[j].y:
                return "not a quadrilateral"

    #if pointA == pointB or pointA == pointC or pointA == pointD or pointB == pointC or pointB == pointD or pointC == pointD:
    #    return "not a quadrilateral"
    lineAB = Line(pointA, pointB)
    lineBC = Line(pointB, pointC)
    lineCD = Line(pointC, pointD)
    lineDA = Line(pointD, pointA)
    #点と点を結んだ上に点がある
    isSpecialCountForX = 0
    isSpecialCountForY = 0
    #if (lineAB.a == lineBC.a and lineAB.b == lineBC.b) or (lineAB.a == lineCD.a and lineAB.b == lineCD.b) or (lineAB.a == lineDA.a and lineAB.b == lineDA.b) or (lineBC.a == lineCD.a and lineBC.b == lineCD.b) or (lineBC.a == lineDA.a and lineBC.b == lineDA.b) or (lineDA.a == lineCD.a and lineDA.b == lineCD.b):
    if (lineAB.a == lineBC.a and lineAB.b == lineBC.b) or (lineAB.a == lineDA.a and lineAB.b == lineDA.b) or (lineBC.a == lineCD.a and lineBC.b == lineCD.b) or (lineCD.a == lineDA.a and lineCD.b == lineDA.b):
        if lineAB.isSpecial != 0 or lineBC.isSpecial != 0 or lineCD.isSpecial != 0 or lineDA.isSpecial != 0:
            lines = [lineAB, lineBC, lineCD, lineDA]
            for line in lines:
                if line.isSpecial == 1:
                    isSpecialCountForX += 1
                if line.isSpecial == 2:
                    isSpecialCountForY += 1
            
            if isSpecialCountForX > 1 or isSpecialCountForY > 1:
                return "not a quadrilateral"
        else:
            return "not a quadrilateral"

    #平行四辺形グループ
    if lineAB.length == lineCD.length and lineBC.length == lineDA.length:
        if lineAB.a * lineBC.a + -1*-1 == 0 or (lineAB.a == 0 and lineBC.a == 0):
            if lineAB.length == lineBC.length:
                message = "square(正方形)"
            else:
                message = "rectangle(長方形)"
        elif lineAB.length == lineBC.length == lineCD.length == lineDA.length:
            message = "rhombus(ひし形)"
        else:
            message = "parallelogram(平行四辺形)"
    #台形
    elif lineAB.a == lineCD.a or lineBC.a == lineDA.a:
        message = "trapezoid(台形)"
    #凧
    elif (lineAB.length == lineBC.length and lineCD.length == lineDA.length) or (lineAB.length == lineDA.length and lineCD.length == lineBC.length):
        message = "kite(凧)"
    #その他
    else:
        message = "other（その他）"

    return message

class Point:
    def __init__(self, x, y):
            self.x = x
            self.y = y

class Line:
    def __init__(self, startPoint, endPoint):
        self.startPoint = startPoint
        self.endPoint = endPoint
        #長さ
        self.length = math.sqrt((startPoint.x - endPoint.x) ** 2 + (startPoint.y - endPoint.y) **2)
        #例外処置　x=0ならフラグ1 y=0ならフラグ2
        self.isSpecial = 0
        #a 傾き　a = yの変化量/xの変化量
        #b y切片　b = y1 - a * x1
        #x=定数の場合（傾き0）
        if startPoint.x == endPoint.x:
            self.a = 0
            self.b = 0
            #y=0の場合
            if startPoint.y == 0 and endPoint.y == 0:
                self.isSpecial = 2
        #y=定数の場合（傾き0）
        elif startPoint.y == endPoint.y:
            self.a = 0
            self.b = startPoint.y
            #x=0の場合
            if self.b == 0:
                self.isSpecial = 1
        else:
            self.a = (startPoint.y - endPoint.y) / (startPoint.x - endPoint.x)  
            self.b = startPoint.y - (self.a * startPoint.x)
        
        

#print(getShapeType(532,363,532,971,190,971,190,363))
#print(getShapeType(0,0,1,0,1,1,4,-5))
#print(getShapeType(1,1,2,2,3,3,4,4))
print(getShapeType(0,0,0,1,1,1,0,0))