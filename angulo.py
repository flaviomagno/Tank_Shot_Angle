import math

# Test data
# Origin tank data
Xo = 0 # X position
Yo = 0 # Y position

# Target tank data
Xt = 1 # X position
Yt = 1 # Y position
Vt = 10 # Target tank speed

# Projectile data
Vp = 20 # Speed

# Shot solution calculation
alpha = math.degrees(math.atan((Xt-Xo)/(Yt-Yo)))
theta = math.degrees(math.asin(Vt/Vp))
angle = 90 - alpha - theta

print(alpha)
print(theta)
print(angle)