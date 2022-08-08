import math

def shot_angle_calc(Xt,Xo,Yt,Yo,Vt,Vp,prnt):
    # Shot solution calculation
    alpha = math.degrees(math.atan((Xt-Xo)/(Yt-Yo)))
    theta = math.degrees(math.asin(Vt/Vp))

    # get aprox value
    alpha = get_aprox_value(alpha)
    theta = get_aprox_value(theta)
    angle = 90 - alpha - theta

    if prnt:
        line = '_____________________________________________________________________________________'
        print(line)
        print('Input vars')
        print(line)
        
        msg = 'Origin tank X position = ' + str(Xo)
        print(msg)

        msg = 'Origin tank Y position = ' + str(Yo)
        print(msg)

        msg = 'Target tank X position = ' + str(Xt)
        print(msg)

        msg = 'Target tank Y position = ' + str(Yt)
        print(msg)

        msg = 'Target tank speed = ' + str(Vt)
        print(msg)

        msg = 'Projectile speed = ' + str(Vp)
        print(msg)

        msg = 'Angle between target and projectile direction = ' + str(alpha)
        print(msg)

        msg = 'Angle between target orthogonal direction and projectile direction = ' + str(theta)
        print(msg)
        print(line)

        msg = 'Calculated angle between projectile direction and X axis = ' + str(angle)
        print(msg)
        print(line)

    return angle

def get_aprox_value(value):
    doubleValue = value * 1000
    invValue = int(doubleValue)
    result = invValue / 1000
    return result