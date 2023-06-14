# simulate() takes in two parameters n and theta
# The points are plotted sequentially starting from (-n * theta) mod 1 all the way to (n * theta) mod 1, for a total of 2n + 1 points
# simulate() outputs a video of the simulation (may take some time to load depending on the value of n)

k = 1 / (2 * pi)
k1 = 9 / 10
k2 = 11 / 10

# pts = []
lns = []
zero = line([(0, k * 3 / 4), (0, k * 5 / 4)], rgbcolor = (1/4, 1, 1/8))

def ani(x, y):
    cir = circle((0, 0), k, color = 'red')
    # p1 = [x, y]
    # pt = point(p1)
    # pts.append(pt)
    ln = line([(k1 * x, k1 * y), (k2 * x, k2 * y)])
    lns.append(ln)
    # ret = cir + ln
    # for i in range(len(pts)):
    #     ret += pts[i]
    # return ret
    rt = cir + zero + ln
    for i in range(len(lns)):
         rt += lns[i]
    return rt

def simulate(n, theta):
    # del pts[:]
    del lns[:]
    dis = [ani(k * cos(2*pi*(i * theta - floor(i * theta))), k * sin(2*pi*(i * theta - floor(i * theta)))) for i in srange(0, n + 1)] + [ani(k * cos(2*pi*(i * theta - floor(i * theta))), k * sin(2*pi*(i * theta - floor(i * theta)))) for i in srange(-n, 0)]
    c = animate(dis, xmin = -0.3, ymin = -0.3, xmax = 0.3, ymax = 0.3,figsize=[4, 4], axes = False)
    c.show(delay = 20)

simulate(30, sqrt(2))