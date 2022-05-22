import math
def differ():
    q=1
    degree=int(input("enter the highest or (lowest for negative power) power of varibale:"))
    polynomial=''
    differ=''
    while degree>-1:
        if degree==0:
            a=int(input("enetr constant value:"))
            degree=degree-1
        else:
            a=int(input("enter the value of constant of variable with power"+" "+str(degree)+":"))
            degree=degree-1
        if a<0:
            a=-1*a
            e=a*(degree+1)
            polynomial=polynomial+"-"+str(a)+"x"+"^"+str(degree+1)
            differ=differ+"-"+str(e)+"x"+"^"+str(degree)
        else :
            e=a*(degree+1)
            polynomial=polynomial+"+"+str(a)+"x"+"^"+str(degree+1)
            differ=differ+"+"+str(e)+"x"+"^"+str(degree)
        
    print("polynomial is:",polynomial)
    print("differntiation is:",differ)
    
