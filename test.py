import angle

# Test data
# Origin tank data
Xo = 0 # X position
Yo = 0 # Y position

# Target tank data
Xt = 1 # X position
Yt = 1 # Y position
Vt = 10 # Target tank speed

# Projectile data
Vp = 20 # Projectile speed

# If you want or not the function to print msgs
prnt = True

a = angle.shot_angle_calc(Xt,Xo,Yt,Yo,Vt,Vp,prnt)
msg = 'Calculated shot angle = ' + str(a)
print(msg)