st1 = 'program'
st2 = 'program'

def chek(st1, st2):
    dif1 = []
    if len(st1) == len(st2):
        list(zip(st1, st2))
        for a, b in zip(st1, st2):
            if a != b:
                dif1.append(a)
        if len(dif1) >= 1:
            print(dif1[0])
        else:
            print('0')

    else:
        print('-1')
chek(st1, st2)


        

