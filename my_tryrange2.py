import pprint
x = range(-20,45,5)
f = [(9.0/5)*i + 32 for i in x]
table = []
for i, f in zip(x, f):    
    table.append([i,f])
    pprint.pprint(table)


