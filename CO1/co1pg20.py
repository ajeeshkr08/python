# 20. From a list of integers, create a list removing even numbers.
l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print("list:")
print(l)
for i  in l:
	if i%2 == 0:
	    l.remove(i)
print("list after removing EVEN numbers:")
print(l)