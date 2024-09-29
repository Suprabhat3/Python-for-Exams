# Input the number
n = int(input("Enter a number: "))

# Initialize sum to 0
sum_of_squares = 0

# Loop through all natural numbers up to n and add their squares
for i in range(1, n+1):
    sum_of_squares += i**2

# Output the result
print(f"The sum of squares of natural numbers up to {n} is: {sum_of_squares}")
