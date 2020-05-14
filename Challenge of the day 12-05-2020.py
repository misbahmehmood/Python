def even_digits(x,y):
    alist=[]
    for i in range(x, y+1):

        for digit in str(i):
            if int(digit) % 2 ==0:
               alist.append(i)
        else:
            break
    return alist
print(even_digits(1000, 3000))

