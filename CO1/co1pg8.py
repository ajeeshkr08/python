#8.. Get a string from an input string where all occurrences of first character replaced with ‘$’, except first character.[eg: onion -> oni$n] 
a=input("Enter the string:")
print("string:",a)
b=a[0]+a[1:].replace(a[0],'$')
print(b)