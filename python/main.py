import roboticstoolbox as rtb
from spatialmath.base.symbolic import *
from roboticstoolbox.tools.trajectory import *


def projekt():

    #inicjacja

    l1=0.42+0.15/2
    l2=0.5
    alpha1=np.pi/2
    offset1=np.pi/2
    theta1_min=0
    theta1_max=np.pi
    d2_min=0
    d2_max=0.4
    l3=0.221314
    theta3_min=0
    theta3_max= 2 * np.pi

    q_tmp = [symbol('θ1'), symbol('d2'), symbol('θ3')]

    robot=rtb.DHRobot(
        [
            rtb.RevoluteDH(d=l1, alpha=alpha1, offset=offset1, qlim=[theta1_min, theta1_max]),
            rtb.PrismaticDH(offset=l2, qlim=[d2_min,d2_max]),
            rtb.RevoluteDH(qlim=[theta3_min, theta3_max], d=l3),
        ], name="RPR")

    print(robot)
    robot.teach(robot.q)

    #kinematyka prosta

    T=robot.fkine(q_tmp)
    print(T)

    #kinematyka prędkości
    J=simplify(robot.jacob0(q_tmp))
    print(J)

    #kinematyka odwrotna - na kartce
    #dynamika - na kartce

if __name__ == '__main__':
    projekt()