# 2. Display future leap years from current year to a final year entered by user. 
y=int(input("Enter the year limit:"))
b=int(2022)
print("Leap years:")
for i in range(b,y):
    if i%4==0 and i%100!=0:
        print(i)