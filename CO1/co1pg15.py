# 15. Print out all colors from color-list1 not contained in color-list2. 
list1 = ['Red','Pink','Orange','Yellow','Purple','Green','Blue','Brown']
list2 = ['Red','Pink','Yellow','Purple','Green','Blue']
l = [ i for i in list1 if i not in list2]
print("Color not contained in color-list2:",l)