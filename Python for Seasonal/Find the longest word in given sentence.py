n = str(input("Enter a sentance :"))
longest = max(n.split(),key = len)
print("Longest word is ",longest)
print("And the length of longest word is",len(longest))