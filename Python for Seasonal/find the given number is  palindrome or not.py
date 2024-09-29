num = input("enter a number :")
num_str = str(num)
reversed_num_str = num_str[::-1]
if num_str == reversed_num_str:
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
