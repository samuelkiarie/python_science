import pprint
def f(x):
    print "f_value  f2_values"
    f_value = range(x,45,5 )
    for i in f_value:
        f2_value = (9.0/5)*i + 32
        print ' %5.2f %5.1f\n' %(i, f2_value)

f(-20)
