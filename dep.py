'''x = raw_input("enter formulae: .")   
def xy():
    return'%s',%(x)
    exec(code)
    print code'''
import sys
C = float(sys.argv[1])
F = 9.0*C/5 + 32
print F 
