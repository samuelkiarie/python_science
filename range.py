C_step = 0.5
C_start = -5
n = 16
Cdegrees = [0.0]*n; Fdegrees = [0.0]*n
for i in range(n):
    Cdegrees[i] = C_start + i*C_step
    Fdegrees[i] = (9.0/5)*Cdegrees[i] + 32
    print Fdegrees[i]
