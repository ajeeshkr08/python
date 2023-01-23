import calculator as cal
a = int(input("Enter the number a:"))
b= int(input("Enter the number b:"))
print("1.add")
print("2.substract")
print("3.Multiply")
print("4.Divide")
print("0.exit")
c = ""
while c !=0:
    c = int(input("Enter the choice."))
    if c== 1:
        print(a,"+",b,"=",cal.sum(a,b))
    elif c == 2:
        print(a,"-",b,"=",cal.sub(a,b))
    elif c == 3 :
        print(a,"*",b,"=",cal.mul(a,b))
    elif c == 4:
        print(a,"/",b,"=",cal.div(a,b))
    else:
        pirnt("inalid choice..")
    print("1.add")
    print("2.substract")
    print("3.Multiply")
    print("4.Divide")
    print("0.exit")
