string = "Morning"
number = 2
bool = True
def strMove(string, number, bool):
    new_ls = []
    if bool == True:
        x = len(string) - number
        for i in range(len(string)):
            a = string[i]
            if i >= x:
                new_ls.append(a)
        for j in range(len(string[:x])):
            b = string[j]
            new_ls.append(b)
        for z in new_ls:
            print(z, end='')
    else:
        x = len(string) - number
        for i in range(len(string)):
            a = string[i]
            if i >= number:
                new_ls.append(a)
        for j in range(len(string[x:])):
            b = string[j]
            new_ls.append(b)
        for z in new_ls:
            print(z, end='')
strMove(string, number, bool)
