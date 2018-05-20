# coding = utf-8
import math

DBL_MAX = 3.402823466e+38
DBL_MIN = 1.175494351e-38

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def length(self):
        return math.sqrt(self.x*self.x + self.y*self.y)

    def __mul__(self, n):
        return Point(self.x*n, self.y*n)

    def __div__(self, n):
        return Point(self.x/n, self.y/n)
    
class OBB:
    u = []
    center = Point(0,0)
    edge = []

def dot_product(v1, v2):
    return v1.x*v2.x + v1.y*v2.y

def find_obb(pts, pts_num):
    min_area = DBL_MAX
    obb = OBB()
    for i in range(0, pts_num):
        u0 = pts[i] - pts[(i-1+pts_num)%pts_num]
        u0 = u0 / u0.length()
        u1 = Point(0-u0.y, u0.x)
        min0 = 0.0
        max0 = 0.0
        min1 = 0.0
        max1 = 0.0
        for k in range(0, pts_num):
            d = pts[k] - pts[(i-1+pts_num)%pts_num]
            dot = dot_product( d, u0 )
            if(dot < min0):
                min0 = dot
            if(dot > max0):
                max0 = dot;
            dot = dot_product( d, u1 )
            if(dot > max1):
                max1 = dot
            if(dot < min1):
                min1 = dot
        area = (max0 - min0) * (max1 - min1)
        if(area < min_area):
            min_area = area
            obb.c = pts[(i-1+pts_num)%pts_num] + (u0 * (max0 + min0) + u1 *(max1 + min1) ) * 0.5
            obb.u.append(u0)
            obb.u.append(u1)
            obb.edge.append((max0-min0)*0.5)
            obb.edge.append((max1-min1)*0.5)
    print obb.c.x, obb.c.y
    print obb.u[0].x, obb.u[0].x, obb.u[1].x, obb.u[1].y
    print obb.edge[0], obb.edge[1]
    
if __name__ == '__main__':
    pts = []
    pts.append(Point(0,0))
    pts.append(Point(2,0))
    pts.append(Point(2,2))
    pts.append(Point(0,2))

    find_obb(pts, 4)

