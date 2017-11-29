def makelist(start, stop,step):
   digits = start
   results= []
   while digits <= stop:
        results.append(digits)
        digits = digits + step
   return results
mylist = makelist(1,40,2)
print 'mylist', mylist
my_list2 = [q+1 for q in mylist]
print'my_list2', my_list2

