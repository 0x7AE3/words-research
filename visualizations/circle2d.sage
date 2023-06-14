# simulate() takes in one parameter n
# The points are plotted starting from (1, 1) and then adding a new "layer" every time, so next (1, 2), (2, 2) and (2, 1) would be plotted and so on.
# total of n * n points are plotted
# simulate() outputs a video of the simulation (may take some time to load depending on the value of n)
# n = 10 takes around 30 seconds, simulation grows quadratically with n

K.<cuberoot2> = NumberField(x^3-2, embedding=1.2) # omega = (cuberoot2, cuberoot4)
cuberoot4 = cuberoot2 * cuberoot2
k = 1 / (2 * pi)
k1 = 9 / 10
k2 = 11 / 10

# pts = []
lns = []
zero = line([(0, k * 3 / 4), (0, k * 5 / 4)], rgbcolor = (1/4, 1, 1/8))

def M(u, v):
    uv = u *cuberoot2 + v * cuberoot4
    uv = uv - int(floor(uv))
    return uv

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

def simulate(n):
    # del pts[:]
    del lns[:]
    dis = []
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            dis.append(ani(k * cos(2*pi*(M(j, i))), k * sin(2*pi*(M(j, i)))))
        for j in range(i - 1, 0, -1):
            dis.append(ani(k * cos(2*pi*(M(i, j))), k * sin(2*pi*(M(i, j)))))
    # dis = [ani(k * cos(2*pi*(i * theta - floor(i * theta))), k * sin(2*pi*(i * theta - floor(i * theta)))) for i in srange(0, n + 1)] + [ani(k * cos(2*pi*(i * theta - floor(i * theta))), k * sin(2*pi*(i * theta - floor(i * theta)))) for i in srange(-n, 0)]
    c = animate(dis, xmin = -0.3, ymin = -0.3, xmax = 0.3, ymax = 0.3,figsize=[4, 4], axes = False)
    c.show(delay = 20) # delay in hundrethds of a second

simulate(10)