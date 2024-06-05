

array = []
y = 10
x = 30
# size

for n in range(y):
    array.append([])
    for n1 in range(x):
        if n  == 0 or   n  == y-1  or n1 == 0 or n1 == x-1 :
            array[n].append("X")
            # The Border or 
        elif  n1%(y) ==  n or n%(x) ==  n1 or   (n + n1%(y)  == y-1 and x > y) or (n1 + n%(x)  == x-1 and y > x) :
            array[n].append("X")
            # The X
        else: 
           array[n].append(" ") 
            # The spaces

for n in range(y):
    print(array[n])
             