# Input the principal amount, rate of interest, and time period
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period (in years): "))

# Calculate simple interest
interest = (principal * rate * time) / 100

# Output the result
print(f"The Simple Interest is: {interest}")
print("Total amount that you return is:",principal+interest)
