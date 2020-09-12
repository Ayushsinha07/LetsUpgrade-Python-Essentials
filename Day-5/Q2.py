def prime(n):
    for n in range(2,n+1):
        i=2
        for i in range(2,n):
            if(n%i==0):
                break
        else:
            print(n,"is prime")

n=2500
prime(n)
        
    
