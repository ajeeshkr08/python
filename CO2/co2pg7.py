#7. Add ‘ing’ at the end of a given string. If it already ends with ‘ing’, then add ‘ly’ 
s = "Construct following pattern using nested loop"
c = "ing"
r = 'ly'
new=""
for i in s.split(" "):
    if i[-3:] == c:
        new = new+" "+i+r
    else:
        new = new+" "+i+c
        
print(new)
