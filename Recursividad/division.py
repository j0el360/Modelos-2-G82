def division(n,m):
    if(m==0):
        return "division por 0"
    if(m>n):
        return 0
    else:
        return division(n-m,m)+1
   
        

print(division(10,5))

        
