n = str(input("Enter a sentance :"))
count = 0
vowels = 'a','e','i','o','u'
for x in n.lower():
    if x in vowels:
        count+=1
print(f"there is {count} vowels in",n)        