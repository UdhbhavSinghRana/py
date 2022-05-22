hrs=input("enter hours:")
rate=input("enter rate:")
hrs=int(hrs)
rate=float(rate)
x=hrs-40
if x>0 :
    pay=x*1.5*rate+40*rate
else :
    pay=hrs*rate
print(pay)
