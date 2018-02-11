i=0
elements=[]

while i<6:
    print "At the top i is %d" %i
    elements.append(i)
    
    i=i+1
    print "Numbers now: ", elements
    print "At the bottom i is %d" %i

print "The numbers: "
for el in elements:
    print el

    