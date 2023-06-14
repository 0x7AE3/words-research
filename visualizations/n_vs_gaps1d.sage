# plots the number of unique spacings for different values of n for the one dimensional case of omega = (sqrt(2))
n = 50 # plots 1,2,...,n
       # n = 500 takes around 10 seconds, though the points can really only be distinctly "seen" up to n = 50

from sortedcontainers import SortedList

K.<sqrt2> = NumberField(x^2-2, embedding=1.4)

def calc(r):
    S = set()
    P = SortedList()
    for x in range(-r, r + 1):
        e = x*sqrt2
        e = e - int(floor(e))
        P.add(e)
    P = list(P)
    for i in range(1, len(P)):
        S.add(P[i] - P[i - 1])
    return len(S)

yl = [calc(k) for k in range(1, n)] # plotting 1 to n
list_plot(yl, plotjoined = False, color = 'purple') # plotjoined can be toggled