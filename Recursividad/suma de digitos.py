
def sumdigitos(n):
   
    if(n==0):
        return n
    else:
        return sumdigitos(n//10)+(n%10)
   

print(sumdigitos(2678))
    
