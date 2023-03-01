numbers = [1, 4, 8, 9]
print(numbers)
number = int(input())
for index in range(len(numbers)):
    check = numbers[index]
    if check == number:
        print(index)
        break
    else:
        numbers.append(number)
        numbers.sort()
        for j in range(len(numbers)):
            b = numbers[j]
            if b == number:
                print(j)
                break
        break
        
                   
