i=1042000
while(i<=702648265):
    temp=i
    l=0
    s=0
    while(temp>0):
        temp=temp//10
        l=l+1
    temp=i
    while(temp>0):
        r=temp%10
        s=s+r**l
        temp=temp//10
    if(s==i):
        print("The first armstrong number is",i)
        break
    i=i+1
  

