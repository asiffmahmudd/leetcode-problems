def isBoomerang(self, points: List[List[int]]) -> bool:
    a, b, c = points[0], points[1], points[2]
    return a[0]*(b[1]-c[1]) + b[0]*(c[1]-a[1]) + c[0]*(a[1]-b[1]) != 0