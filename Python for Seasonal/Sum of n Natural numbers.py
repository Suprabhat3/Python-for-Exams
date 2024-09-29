n = int(input("Enter a number :"))
sum = 0
if n <= 0:
    print("Please enter natural number")
    exit()
for i in range (1,n+1):
    sum += i
print(f"the sum of natural numbers till {n} is :",sum)