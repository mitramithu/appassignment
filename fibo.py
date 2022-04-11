
n=int(input('enter'))
n1,n2=0,1
count=0
if n<=0:
    print('enter positive integer:')
elif n==1:
    print('fibo series',n,':')
    print(n1)
else:
    print('fibo series:')
    while count<n:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1


