def Lshift(Arr,n):
    a=[]
    b=0
    d=[]
    while b<n:
        d.append(Arr[b])
        b=b+1
    while n<len(Arr) :
        a.append(Arr[n])
        n=n+1
    c=len(d)
    i=0
    while c>0:
        a.append(d[i])
        i=i+1
        c=c-1
    print(a)         
        
