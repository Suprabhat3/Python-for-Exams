# Input number of terms
n_terms = int(input("enter a number :"))
a, b = 0, 1
count = 0
if n_terms <= 0:
    print("Please enter a positive integer.")
elif n_terms == 1:
    print("Fibonacci sequence up to", n_terms, "term:")
    print(a)
else:
    print(f"Fibonacci sequence to {n_terms} is :")
    while count < n_terms:
        print(a, end=" ")
        # Update the terms
        temp = a  
        a = b     
        b = temp + b  
        count += 1

