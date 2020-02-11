import math
import random
class Color:
    def __init__(self,x,y,z):
        self.r = x
        self.g = y
        self.b = z



class line:
    def __init__(self, x, y, a, b, col):
        self.x0 = x
        print(self.x0)
        self.x1 = a
        print(self.x1)
        self.y0 = y
        print(self.y0)
        self.y1 = b
        print(self.y0)
        self.color = col

    def rotate(self, rad):
        x0 = self.x0
        x1 = self.x1
        y0 = self.y0
        y1 = self.y1
        hyp = math.sqrt(math.pow(x0 - x1,2) + math.pow(y0 - y1, 2))
        startAngle = math.acos((x1 - x0)/hyp)
        newAngle = startAngle + rad
        newEndX = int(math.floor(x0 + math.cos(newAngle)*hyp))
        newEndY = int(math.floor(y0 + math.sin(newAngle)*hyp))
        return(line(x0,y0,newEndX,newEndY,self.color))

    def draw(self, file):
        arrayStorage = []
        for i in range(500):
            arrayStorage.append([])
            for j in range(500):
                arrayStorage[i].append(Color(250,250,250))

        x0 = self.x0
        x1 = self.x1
        y0 = self.y0
        y1 = self.y1
        col = self.color

        dx = x1 - x0
        dy = y1 - y0

        xsign = 1 if dx > 0 else -1
        ysign = 1 if dy > 0 else -1

        dx = abs(dx)
        dy = abs(dy)

        if dx > dy:
            newx, xy, yx, newy = xsign, 0, 0, ysign
        else:
            dx, dy = dy, dx
            newx, xy, yx, newy = 0, ysign, xsign, 0
        D = 2*dy - dx
        y = 0
        for x in range(dx + 1):
            arrayStorage[x0 + x*newx + y*yx][y0 + x*xy + y*newy] = col
            if D >= 0:
                y += 1
                D -= 2*dx
            D += 2*dy


        file = open(file, "w")
        file.write("P3\n500 500\n255\n")
        for i in arrayStorage:
            for j in i:

                file.write(str(j.r) + ' ' + str(j.g) + ' ' + str(j.b))
                file.write("\n")
        file.close()



arrayStorage = []
for i in range(500):
    arrayStorage.append([])
    for j in range(500):
        arrayStorage[i].append(Color(250,250,250))

def line(x0, y0, x1, y1, col):
    global arrayStorage
    dx = x1 - x0
    dy = y1 - y0

    xsign = 1 if dx > 0 else -1
    ysign = 1 if dy > 0 else -1

    dx = abs(dx)
    dy = abs(dy)

    if dx > dy:
        newx, xy, yx, newy = xsign, 0, 0, ysign
    else:
        dx, dy = dy, dx
        newx, xy, yx, newy = 0, ysign, xsign, 0
    D = 2*dy - dx
    y = 0
    for x in range(dx + 1):
        arrayStorage[x0 + x*newx + y*yx][y0 + x*xy + y*newy] = col
        if D >= 0:
            y += 1
            D -= 2*dx
        D += 2*dy


def rotatePoints(x0, y0, x1, y1, rad):
    #x0, y0 are the base point of rotation
    #Yeah i know floating points are slow but idk how else to do this
    hyp = math.sqrt(math.pow(x0 - x1,2) + math.pow(y0 - y1, 2))
    print(hyp)
    startAngle = math.acos((x1 - x0)/hyp)
    print(startAngle/math.pi)
    newAngle = startAngle + rad
    print(newAngle/math.pi)
    newEndX = int(math.floor(x0 + math.cos(newAngle)*hyp))
    newEndY = int(math.floor(y0 + math.sin(newAngle)*hyp))
    print(newEndX)
    print(newEndY)
    return([x0,y0,newEndX,newEndY])





line(100,50,300,400, Color(255, 0, 0))
line(100,50,330,20, Color(255, 0, 0))
line(330, 20, 300, 400, Color(255,0,0))
line(100,50,315,210, Color(0, 255, 0))
line(330, 20, 200, 225, Color(0,255,0))
line(300,400, 215, 35, Color(0,255,0))
line(330,400,330,20, Color(0,0,255))
line(330,400,100,400, Color(0,0,255))
line(100,400,100,20, Color(0,0,255))
line(100,20,330,20,Color(0,0,255))
# x1 = 10
# y1 = 10
# x2 = 10
# y2 = 300
#
# line(200,10,200,200,Color(100,100,100))
# for i in range(10):
#     newVect = rotatePoints(x1, y1, x2, y2, int(math.ceil(60)))
#     dx = int(math.floor(newVect[2] - newVect[0] * 3/4))
#     dy = int(math.floor(newVect[3] - newVect[1] * 3/4))
#     x1 = x2
#     y1 = y2
#     x2 = x1 + dx
#     y2 = y1 + dy
#     line(x1,y1,x2,y2, Color(int(math.ceil(random.random() * 255)), int(math.ceil(random.random() * 255)), int(math.ceil(random.random() * 255))))





file = open("image.ppm", "w")
file.write("P3\n500 500\n255\n")
for i in arrayStorage:
    for j in i:

        file.write(str(j.r) + ' ' + str(j.g) + ' ' + str(j.b))
        file.write("\n")
file.close()
