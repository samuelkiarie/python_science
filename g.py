a = 20
b = -2.5
def f1(x):
     a =21
     return a*x + b
print a
def f2(x):
    global a
    a = 21
    return a*x + b
print a
print a

