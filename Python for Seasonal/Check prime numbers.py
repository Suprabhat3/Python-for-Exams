n = int(input("Enter a number :"))
var = 0
if n <= 0:
    print("your number is not a prime number")
    exit()
for i in range(2,n):
    if n%i == 0:
        var += 1
        break
if var == 1:
    print("your number is not a prime number")    
else:
    print("your number is a prime number")