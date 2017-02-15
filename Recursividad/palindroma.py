a=0
def palindroma(palabra):
    print(palabra)
    global a
    if((len(palabra)==1)or(len(palabra)==0)):
        return "si es palindroma"
    else:
        if(palabra[0]==palabra[len(palabra)-1]):
            
            b=len(palabra)-1
            return palindroma(palabra[1:b])
        return "no es palindroma"
print(palindroma("aibofobia"))
    
