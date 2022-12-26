import numpy as np
import matplotlib.pyplot as plt


def odeEuler(f, g, x0, y0, t):
    '''Approximate the solution of y'=f(y,t) by Euler's method.

    Parameters
    ----------
    f : function
        Right-hand side of the differential equation y'=f(t,y), y(t_0)=y_0
    y0 : number
        Initial value y(t0)=y0 wher t0 is the entry at index 0 in the array t
    t : array
        1D NumPy array of t values where we approximate y values. Time step
        at each iteration is given by t[n+1] - t[n].

    Returns
    -------
    y : 1D NumPy array
        Approximation y[n] of the solution y(t_n) computed by Euler's method.
    '''
    y, x = np.zeros(len(t)), np.zeros(len(t))
    y[0], x[0] = y0, x0
    for n in range(0, len(t)-1):
        x[n+1] = x[n] + f(x[n], y[n], t[n])*(t[n+1] - t[n])
        y[n+1] = y[n] + g(x[n], y[n], t[n])*(t[n+1] - t[n])
    return x, y


def draw_euler(t0, tend, x0, y0, f, g, title):
    t = np.linspace(t0, tend, 100)  # start, stop, liczba
    #f = lambda y, t: 0.7 * y * (1 - y / 50)
    x, y = odeEuler(f, g, x0, y0, t)
    plt.plot(t, y)
    plt.grid(True)
    # plt.axis([0, 5, -1, 0])
    plt.title(title)
    plt.show()

#b21-wpływ x na y
if __name__ == "__main__":
    t = np.linspace(0, 60, 1000)  #start, stop, liczba
    x0 = 200
    y0 = 60
    r1, r2, b12, b21, L1, L2 = 0.8, 0.8, 1, 1, 600, 1000
    xx = lambda x, y, t: r1 * x * (1 - (x + b12*y) / L1)  # wiewiórki rude
    yy = lambda x, y, t: r2 * y * (1 - (y + b21*x) / L2)  # wiewiórki szare
    x, y = odeEuler(xx, yy, x0, y0, t)
    plt.plot(t, x, color="c", linewidth=3)
    plt.plot(t, y, color="y", linewidth=3)
    plt.grid(True)
    plt.legend(['populacja P1', 'populacja P2'])
    plt.show()
    def f(Y, t):
        x, y = Y
        return [r1 * x * (1 - (x + b12 * y) / L1), r2 * y * (1 - (y + b21 * x) / L2)]


    y1 = np.linspace(0.0, 1000.0, 20)
    y2 = np.linspace(0.0, 1000.0, 20)

    Y1, Y2 = np.meshgrid(y1, y2)

    t = 0
    u, v = np.zeros(Y1.shape), np.zeros(Y2.shape)

    NI, NJ = Y1.shape

    for i in range(NI):
        for j in range(NJ):
            x = Y1[i, j]
            y = Y2[i, j]
            yprime = f([x, y], t)
            u[i, j] = yprime[0]
            v[i, j] = yprime[1]
    M = (np.hypot(u, v))
    M[M == 0] = 1.  # zamiana zer na jedyki

    Q = plt.quiver(Y1, Y2, u / M, v / M, M)

    plt.xlabel('$x$')
    plt.ylabel('$y$')
    a = [0+i for i in range(600)]
    b = [1000-5/3*i for i in a]
    #plt.axhline(y=475, color='r', linestyle='-')
    #plt.scatter(270,y=475, color='r')
    #plt.axhline(y=0, color='r', linestyle='-')
    plt.plot(a, b, color="red", linewidth=1)
    plt.show()


    # def pole_wektorowe(zakres_x, zakres_y, a, b, d):
    #     u, v = np.meshgrid(zakres_x, zakres_y)
    #     U = u * (1 - u) - a * u * v / (u + d)
    #     V = b * v * (1 - v / u)
    #     plt.quiver(u, v, U, V)
    #
    #
    #
    # a = 2.
    # b = 0.01
    # d = 0.4
    # pole_wektorowe(np.arange(0.1, 1, 0.05), np.arange(0.15, 0.3, 0.01), a, b, d)
    # plt.show()
    #