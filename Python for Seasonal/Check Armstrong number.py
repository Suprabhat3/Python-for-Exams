num = int(input("Enter a number :"))
num_str = str(num)
num_len = len(num_str) # for calculate the power
sum_of_power = 0
for digit in num_str:
    sum_of_power += int(digit)**num_len

if sum_of_power == num:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")     