import math

# Test data
Xt = 1 # Target tank X position
Xo = 0 # Origin tank X position
Yt = 1 # Target tank Y position
Yo = 0 # Origin tank Y position
Vt = 10 # Target tank speed
Vp = 20 # Projectile tank speed

# Shot solution calculation
alpha = math.degrees(math.atan((Xt-Xo)/(Yt-Yo)))
theta = math.degrees(math.asin(Vt/Vp))
angle = 90 - alpha - theta

print(alpha)
print(theta)
print(angle)