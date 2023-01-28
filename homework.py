


########5

inp = int(input("Size Of The Image:" ))
for i in range(inp): 
    if i == inp-1 or i == 0 :
        print(" *" * inp)
    else:
        print(" *" + (inp - 2) * "  " + " *" ) 


