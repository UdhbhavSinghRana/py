largest=0
smallest=11111111111111111111111111111111111111111111111
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try : 
       num=int(num)
    except :
        print('Invalid input')
        continue
    #print(num)
    if largest<num:
        largest=num
    if smallest>num:
        smallest=num
print('Maximum is',largest)
print('Minimum is',smallest)
