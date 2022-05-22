def computepay(hrs,rate) :
    hrs=int(hrs)
    hours=hrs-40
    rate=float(rate)
    payd=rate*(hrs-hours)
    if hrs>40 :
        rate=(1.5*rate)
    else :
        rate=rate
    payx=rate*hours
    pay=payd+payx
    return pay
x=input('enter hours:')
y=input('enter rate:')
x=float(x)
y=float(y)
z=computepay(x,y)
print(z)

    
