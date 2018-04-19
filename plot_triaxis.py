from pylab import *


def get_func_pic(dir):
    with open('{}/capacity'.format(dir)) as capacity,\
            open('{}/current'.format(dir)) as current,\
            open('{}/voltage'.format(dir)) as voltage:
        cap=[int(i) for i in capacity]
        cur=[-int(i) / 1000 for i in current]
        vol=[int(i) / 1000 for i in voltage]
    x=[i for i in range(1, 1 + len(cap))]

    _, ax1=subplots()
    ax2=ax1.twinx()
    ax3=ax2.twinx()
    ax1.plot(x, cap, 'r')
    ax2.plot(x, cur, 'g')
    ax3.plot(x, vol, 'b')

    ax1.set_xlabel('time (s)', fontsize=16)
    ax1.set_ylim(0, 110)
    ax1.set_ylabel('capcity (%) ', fontsize=16, color='r')
    ax2.set_ylim(-200, 2350)
    ax2.set_ylabel('current (mA) ', fontsize=16, color='g')
    ax3.set_ylim(3700, 4250)
    ax3.set_ylabel('voltage (mV) ', fontsize=16, color='b')
    show()

dir=input('directory name:\n')
get_func_pic(dir)
