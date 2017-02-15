def binaDec(num):
    if(num<10):
        return num
    else:
        //return (num%10)+binaDec(num//10)*2
        return (num%10)+binaDec(num//10)*10
print (binaDec(15))
