password = str(input())
def check_email(password)
if len(password) >= 6 and len(password) <= 16:
    a = 0
    b = 0
    c = 0
    for i in password:
        if i == '@' or i == '.':
            a += 1
            for j in password:
                if ord(j) >= ord('0') and ord(j) <= ord('9'):
                    b += 1
                    for z in password:
                        if ord(z) >= ord('A') and ord(z) <= ord('Z'):
                            c += 1
    if a > 0 and b > 0 and c > 0:
        print("Right Password")
else:
    print("Wrong Password!!!")
