year = int(input("enter your year :"))
if year%400 == 0:
    print("your year is leep year")
elif year%4 == 0 and year%100 != 0:
    print("your year is leep year")
else:
    print("your year is not leep year")