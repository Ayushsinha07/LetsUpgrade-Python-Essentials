l=[]
n=int(input("Enter the size of list = "))
for i in range(1,n+1):
    m=int(input("Enter the item inside list = "))
    l.append(m)
sl=[1,1,5]
count=0
for i in l:
    if(i ==sl[count]):
        count=count+1
        
if(count==3):
    print("Listy = ",l,"-it's a Match")
else:
    print("Listy = ",l,"-it's Gone")
