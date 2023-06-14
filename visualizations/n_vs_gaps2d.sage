# plots the number of unique spacings for different values of n for the two dimensional case of omega = (cuberoot(2), cuberoot(4))
n = 50 # plots 1,2,...,n
       # n = 50 takes around 10 seconds

from sortedcontainers import SortedList

K.<cuberoot2> = NumberField(x^3-2, embedding=1.2)

def calc(r):
    S = set()
    P = SortedList()
    for x in range(1, r + 1):
        for y in range(1, r + 1):
            e = x*cuberoot2 + y * (cuberoot2)^2
            e = e - int(floor(e))
            P.add(e)
    P = list(P)
    for i in range(1, len(P)):
        S.add(P[i] - P[i - 1])
    return len(S)

yl = [calc(k) for k in range(1, n)] # plotting 1 to n
list_plot(yl, plotjoined = True, color = 'purple')