
p = 2151

#g^x mod P
g = 2
found = False
while not found :
    for x in range (2,p):
         if pow (g,x,p) == g :
            if x == p-1:
            print(g)
            found = True
            break
          g=g+1