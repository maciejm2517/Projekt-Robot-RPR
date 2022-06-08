import roboticstoolbox as rtb
import numpy as np
import math
from spatialmath import *
from spatialmath.base import *
from spatialmath.base.symbolic import *
import time
from roboticstoolbox.tools.trajectory import *


def projekcik():
    '''
    robot=rtb.DHRobot(
        [
            rtb.RevoluteDH(d=symbol('l1'), alpha=pi()/2, offset=pi()/2),
            rtb.PrismaticDH(offset=symbol('l2')),
            rtb.RevoluteDH(a=symbol('l3'))
        ], name="RPR")
    for links in robot.links:
        print(links)
    '''

    #inicjacja

    robot=rtb.DHRobot(
        [
            rtb.RevoluteDH(d=0.2, alpha=np.pi/2, offset=np.pi/2, qlim=[0,2*np.pi] ),
            rtb.PrismaticDH(offset=0.1, qlim=[0,0.2]),
            rtb.RevoluteDH(qlim=[0,2*np.pi], d=0.1),
            #rtb.RevoluteDH(offset=np.pi/2, alpha=np.pi/2, qlim=[0,0])
        ], name="RPR")

    print(robot)
    robot.teach(robot.q)

    #kinematyka prosta

    q_tmp=[symbol('θ1'),symbol('d2'), symbol('θ3')]
    T=robot.fkine(q_tmp)
    print(T)

    #kinematyka prędkości
    J=simplify(robot.jacob0(q_tmp))
    print(J)

    #kinematyka odwrotna - na kartce
    #dynamika - na kartce

if __name__ == '__main__':
    projekcik()