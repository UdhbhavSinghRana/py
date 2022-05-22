hrs=input("Enter hrs:")
rate=input("Enter rate:")
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
print(pay)
