# 6. Store a list of first names. Count the occurrences of ‘a’ within the list
names=["ashil","anand","ajeeshs","aljo"]
count=0
for name in names:
    count=count+name.count('a')
print("occurrences  of a in the list:",count)
