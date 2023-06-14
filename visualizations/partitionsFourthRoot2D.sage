# same thing as partitions2d but for omega = (fourthrootof(2), fourthrootof(4)) which is not badly approximable
n = 50 # size of n by n grid, n = 50 takes about 20 seconds to run

from sortedcontainers import SortedList

K.<fourthrootof2> = NumberField(x^4-2, embedding=1.2)

ucolors = [(255,0,0), (0,255,0), (0,0,255), (255,255,0), (0,255,255), (255,0,255), (128,128,0), (0,255,255), (255,0,255), (0,0,0)]
def calc(r):
    S = set()
    P = SortedList()
    K = {}
    for x in range(1, r + 1):
        for y in range(1, r + 1):
            e = x*fourthrootof2 + y * (fourthrootof2)^2
            e = e - int(floor(e))
            P.add(e)
            K[e] = (x, y)
    P = list(P)
    J = {}
    for i in range(1, len(P)):
        S.add(P[i] - P[i - 1])
        coord = K[P[i]]
        J[coord] = P[i] - P[i - 1]
    C = set()
    colors = {}
    col = 1
    for p in J:
        tp = len(C)
        C.add(J[p])
        if(len(C) != tp):
            colors[p] = col
            col += 1
        else:
             for i in colors:
                 if(J[p] == J[i]):
                     colors[p] = colors[i]
                     break
    return colors
ysr = calc(n) # n by n grid
sum([point((x[0], x[1]), rgbcolor = (ucolors[ysr[x]][0] / 255, ucolors[ysr[x]][1] / 255, ucolors[ysr[x]][2] / 255), size = 30) for x in ysr])