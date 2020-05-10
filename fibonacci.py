no= int(input("Enter a Number"))
n=0
m=1

counter=0

while counter<no:
    print(n)
    f=n+m
    n=m
    m=f
    counter +=1
