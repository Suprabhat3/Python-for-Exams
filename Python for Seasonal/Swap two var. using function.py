def swap(a, b):
    a, b = b, a
    return a, b
x = input("enter first variable :")
y = input("enter second variable :")
x, y = swap(x, y)
print(f"After swapping: x = {x}, y = {y}")
