string = 'cat'
res = []
for i in range(len(string)):
    a = ''
    for j in range(len(string)):
        if j == i:
            a += string[j].upper()
        else:
            a += string[j]
    res.append(a)
print(res) 

    
        
        
