def potencia(n,m):
    if(m==0):
        return 1
    else:
        return n*potencia(n,m-1)

print(potencia(100,1))    
