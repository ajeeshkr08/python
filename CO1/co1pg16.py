# 16. Create a single string separated with space from two strings by swapping the 
#  character at position 1. 
s1 = "Thonny"
s2 = "Python"
print("string1:",s1)
print("string2:",s2)
s = s2[0]+s1[1:]+" "+s1[0]+s2[1:]
print("string:",s)