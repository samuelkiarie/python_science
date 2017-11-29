'''t = (0.1,0.1)
x= 0.0
for i in range(len(t)):
    for j in t:
        x += i + j
print i
import sys
i1 = eval(sys.argv[1])
i2 = eval(sys.argv[2])
r = i1 + i2
print " The sum of %.2f and %.2f is %.2f " %(i1, i2, r), '''
'''import sys
s = sum([float(x) for x in sys.argv[1:]])
print 'The sum of %s is: %s  ' % (' '.join(sys.argv[1:]), s)'''
# set default values:
s0 = v0 = 0; a = t = 1
import getopt, sys
options, args = getopt.getopt(sys.argv[1:], '', ['t=', 's0=', 'v0=', 'a='])
for option, value in options:
    if option == '--t':
        t = float(value)
    elif option == '--a':
        a = float(value)
    elif option == '--v0':
        v0 = float(value)
    elif option == '--s0':
        s0 = float(value)
print "An object, starting at s=%g at t=0 with initial velocity %s m/s, and subject to a constant acceleration %g m/s**2, is found at the location s=%g m after %s seconds." % (s0, v0, a, , t)
