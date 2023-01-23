#6. Count the number of characters (character frequency) in a string.
s = str(input("Enter the String:"))
count= 0
for i in s.split(" "):
    count = count+len(i)
print("The no of characters in string:",count)
