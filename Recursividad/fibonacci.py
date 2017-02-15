pos=3
n1=0
n2=1

def fib(a):
    global pos,n1,n2
    if(a==0):
        return n1
    if(a==1):
        return n2
    if(a==pos):
        return (n1+n2)
    else:
        n1,n2,pos=n2,n1+n2,pos+1
        return fib(a)

print(fib(8))    
    

    
    
