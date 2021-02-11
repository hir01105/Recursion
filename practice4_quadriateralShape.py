# ここから書いてください
class QuadrilateralShape:
    def __init__(self, lineAB, lineBC, lineCD, lineDA):
        self.lineAB = lineAB
        self.lineBC = lineBC
        self.lineCD = lineCD
        self.lineDA = lineDA
        cosThetaForABC = abs(self.lineAB.a * self.lineBC.a + self.lineAB.by * self.lineBC.by) / (math.sqrt(self.lineAB.a**2 + self.lineAB.by**2) * math.sqrt(self.lineBC.a**2 + self.lineBC.by**2))
        self.ABC = math.floor(math.degrees(math.acos(cosThetaForABC)))
        cosThetaForBCD = abs(self.lineBC.a * self.lineCD.a + self.lineBC.by * self.lineCD.by) / (math.sqrt(self.lineBC.a**2 + self.lineBC.by**2) * math.sqrt(self.lineCD.a**2 + self.lineCD.by**2))
        self.BCD = math.floor(math.degrees(math.acos(cosThetaForBCD)))
        cosThetaForCDA = abs(self.lineCD.a * self.lineDA.a + self.lineCD.by * self.lineDA.by) / (math.sqrt(self.lineCD.a**2 + self.lineCD.by**2) * math.sqrt(self.lineDA.a**2 + self.lineDA.by**2))
        self.CDA = math.floor(math.degrees(math.acos(cosThetaForCDA)))
        cosThetaForDAB = abs(self.lineDA.a * self.lineAB.a + self.lineDA.by * self.lineAB.by) / (math.sqrt(self.lineDA.a**2 + self.lineDA.by**2) * math.sqrt(self.lineAB.a**2 + self.lineAB.by**2))
        self.BAD = math.floor(math.degrees(math.acos(cosThetaForDAB)))
        

    # 四角形の名称を返します。square(正方形)、rectangle(長方形)、kite(凧)、rhombus(ひし形)、parallelogram(平行四辺形)、trapezoid(台形)があります。
    def getShapeType(self): 
        return getShapeTypeWithLines(self.lineAB, self.lineBC, self.lineCD, self.lineDA)


    def getPerimeter(self): # 四角形の周囲の長さを返します。
        return self.lineAB.length + self.lineBC.length + self.lineCD.length + self.lineDA.length

    
    def getArea(self): # 四角形の面積を返します。
        return 1/2 * self.lineAB * self.lineBC *math.sin(math.radians(self.roundedABC)) + 1/2 * self.lineCD.length * self.lineDA.length * math.sin(math.radians(self.roundedADC))

    def getAngle(self, angleString): #BAD、ABC、ADC、BCDの角度を返します。
        if angleString == "BAD":
            return self.roundedBAD
        elif angleString == "ABC":
            return self.roundedABC
        elif angleString == "ADC":
            return self.roundedADC
        elif angleString == "BCD":
            return self.roundedBCD        

  
  

    def draw(self): #// ﹍﹉ | \ /を使って、四辺形をテキストとして描画します。1文字は平面上における距離です。|は直角、/は45度、\は135度の場合に用いられます。これらの描写用の記号は対応する角度がある場合に限ります。
        if self.getShapeType() == "square(正方形)":
            lineAB = "　　"
            verticalLine = "|　"
            for i in range(0, int(self.lineAB.length)):
                lineAB+=("﹍　")
                verticalLine += "　　"
            print(lineAB)
            verticalLine += "|"

            for j in range(0, int(self.lineAB.length)):
                print(verticalLine)
            print(lineAB.replace("﹍", "﹉"))
            
        elif self.getShapeType() == "rectangle(長方形)":
            lineAB = "　　"
            verticalLine = "|　"
            for i in range(0, int(self.lineAB.length)):
                lineAB+=("﹍　")
                verticalLine += "　　"
            print(lineAB)
            verticalLine += "|"

            for j in range(0, int(self.lineBC.length)):
                print(verticalLine)
            print(lineAB.replace("﹍", "﹉"))
            
        elif self.getShapeType() == "parallelogram(平行四辺形)":
            if self.BAD == 45.0:
                line = "/　|"
                for i in range(0, int(self.lineAB.length)-1):
                    line = "　　" + line
                line = "　　" + line
                print(line)
                for x in range(0, int(self.lineAB.length)-1):
                    for j, k in enumerate(line):
                        if k == "/":
                            line = line[:j-2] + "/　　" + line[j+1:]
                    print(line)

                verticalLine = "|　"
                for l in range(0, int(self.lineAB.length)):
                    verticalLine += "　　"
                verticalLine += "|"
                argVerticalLine = int(self.lineBC.length)-int(self.lineAB.length)
                if argVerticalLine > 0:
                    for m in range(0, argVerticalLine):
                        print(verticalLine)
                line = "|　"
                for n in range(0, int(self.lineAB.length)):
                    line += "　"
                line += "/"
                print(line)
                for o in range(0, int(self.lineAB.length)-1):
                    for p, q in enumerate(line):
                        if q == "/":
                            line = line[:p-2] + "/　　" + line[p+1:]
                    print(line)      

            elif self.BAD == 135:
                line = ""
                for i in range(0, self.lineAB.length):
                    line += " ﹍"
                linespace = ""
                for j in range(0, self.lineBC.length):
                    linespace += "　"
                print(linespace + line)
        return         


import math
def getShapeTypeWithLines(lineAB, lineBC, lineCD, lineDA):
    #ここから書きましょう
    message = ""
    """
    pointA = Point(ax, ay)
    pointB = Point(bx, by)
    pointC = Point(cx, cy)
    pointD = Point(dx, dy)
    
    #同じ座標に位置する点がある
    points = [pointA, pointB, pointC, pointD]
    ###
    for i in range(4):
        for j in range(4):
            if i == j:
                continue
            if points[i].x == points[j].x and points[i].y == points[j].y:
                return "not a quadrilateral"

    
    lineAB = Line(pointA, pointB)
    lineBC = Line(pointB, pointC)
    lineCD = Line(pointC, pointD)
    lineDA = Line(pointD, pointA)
    """
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
        if lineAB.a * lineBC.a + lineAB.by*lineBC.by == 0:
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
        #yの次数
        self.by = -1
        #a 傾き　a = yの変化量/xの変化量
        #b y切片　b = y1 - a * x1
        #x=定数の場合（傾き1）
        if startPoint.x == endPoint.x:
            self.a = 1
            self.b = None
            self.by = 0
            #x=0の場合
            if startPoint.x == 0 and endPoint.x == 0:
                self.isSpecial = 2
        #y=定数の場合（傾き0）
        elif startPoint.y == endPoint.y:
            self.a = 0
            self.b = startPoint.y
            self.by = 1
            #y=0の場合
            if self.b == 0:
                self.isSpecial = 1
        else:
            self.a = (startPoint.y - endPoint.y) / (startPoint.x - endPoint.x)  
            self.b = startPoint.y - (self.a * startPoint.x)
        
# square（正方形）
# 　　﹍　﹍　﹍　﹍　﹍　　
# ｜　　　　　　　　　　　｜
# ｜　　　　　　　　　　　｜
# ｜　　　　　　　　　　　｜
# ｜　　　　　　　　　　　｜
# ｜　　　　　　　　　　　｜
# 　　﹉　﹉　﹉　﹉　﹉　　
lineA = Line(Point(0,0), Point(5,0))
lineB = Line(Point(5,0), Point(5,5))
lineC = Line(Point(5,5), Point(0,5))
lineD = Line(Point(0,5), Point(0,0))

square = QuadrilateralShape(lineA, lineB, lineC, lineD)
square.draw()
# rectangle（長方形）
# 　　﹍　﹍　﹍　﹍　﹍　﹍　﹍　﹍　　
# ｜　　　　　　　　　　　　　　　　　｜
# ｜　　　　　　　　　　　　　　　　　｜
# ｜　　　　　　　　　　　　　　　　　｜
# ｜　　　　　　　　　　　　　　　　　｜
# ｜　　　　　　　　　　　　　　　　　｜
# 　　﹉　﹉　﹉　﹉　﹉　﹉　﹉　﹉　　
lineA = Line(Point(0,0), Point(8,0))
lineB = Line(Point(8,0), Point(8,5))
lineC = Line(Point(8,5), Point(0,5))
lineD = Line(Point(0,5), Point(0,0))

rectangle = QuadrilateralShape(lineA, lineB, lineC, lineD)
rectangle.draw()
# parallelogram(平行四辺形)
# 　　　　　　　
# 　　　　／　｜
# 　　／　　　｜
# ｜　　　　　｜
# ｜　　　　　｜
# ｜　　　／　　
# ｜　／　
lineA = Line(Point(0,0), Point(2,2))
lineB = Line(Point(2,2), Point(2,6))
lineC = Line(Point(2,6), Point(0,4))
lineD = Line(Point(0,4), Point(0,0))
parallelogram1 = QuadrilateralShape(lineA, lineB, lineC, lineD)
parallelogram1.draw()
# parallelogram(平行四辺形)
# 　　　　　　﹍　﹍　﹍　﹍　　
# 　　　　／　　　　　　　／　　
# 　　／　　　　　　　／　　　　
# 　　﹉　﹉　﹉　﹉　　
lineA = Line(Point(0,0), Point(4,0))
lineB = Line(Point(4,0), Point(6,2))
lineC = Line(Point(6,2), Point(2,2))
lineD = Line(Point(2,2), Point(0,0))
parallelogram2 = QuadrilateralShape(lineA, lineB, lineC, lineD)
parallelogram2.draw()
# trapezoid(台形)
# 　　　　　　﹍　﹍　　　　　　
# 　　　　／　　　　　＼　　　　
# 　　／　　　　　　　　　＼　　
# 　　﹉　﹉　﹉　﹉　﹉　﹉　　