def count_i(n, somma):
    i=0
    numbers= []
    while i<n:
        numbers.append(i)
        i=i+somma
        print "Numbers now:", numbers

count_i(33, 3)


d= range(0,33, 3) 
print d
numbers= []
  
def count_i(aggiungi):
    for i in d:
        aggiungi= numbers.append(i)
        print "Numbers now:", numbers

count_i(d) 