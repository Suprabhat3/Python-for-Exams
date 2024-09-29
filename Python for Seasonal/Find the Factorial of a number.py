n = (int(input("enter a number"))) 
a = 1
b = n #this is just for print n in last
while n>=1:
    a*=n
    n-=1 
print(f"the factorial of {b} is :",a)