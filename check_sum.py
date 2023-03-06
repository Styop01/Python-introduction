a = 16
b = 24
c = 9
def check_sum(a, b, c):
    args = [a, b, c]
    sum = 0
    for i in args:
        sum += i
    if sum < 50:        
        return print("Not Enought!")
    else:
        return print("Varification Passed")
check_sum(a, b, c)

