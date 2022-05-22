largest=0
smallest=100000000000000000000000000000000000000000000000000000000
while True :
    num=input('enter a numer:')
    if num =='done' :
        break
    try :
        num=float(num)
    except :
        num=str(num)
        print('invalid input')
        break
    if num>largest :
        largest=num
        #print('maximum',num)
    if num<smallest :
        smallest=num
        #print('minimum',num)
print('maximum=',largest)
print('minimum',smallest)
