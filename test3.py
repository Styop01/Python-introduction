str1 = "GoodMorning"
str2 = "Morning"
def strStr(str1, str2):
    a = len(str1) - len(str2)
    new_st = str1[a:]
    list(zip(str2, new_st))
    for x, y in list(zip(str2, new_st)):
        if x == y:
            print(a)
            break
strStr(str1, str2)



