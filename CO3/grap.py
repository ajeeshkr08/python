from Graphics.rectangle import*
from Graphics.circle import*
from Graphics.dgraphics.cuboid import*
from Graphics.dgraphics.sphere import*
l=int(input("Enter the length of rectangale :"))
b=int(input("Enter the breadth of rectangale :"))
print("Area of Rectangle :",rectArea(l,b))
print("Perimiter of Rectangle :",rectPerimeter(l,b))

r=int(input("Enter the radius of circle :"))
print("Area of circle :",circleArea(r))
print("Perimiter of circle :",circlePerimeter(r))

l=int(input("Enter the length of cuboid :"))
b=int(input("Enter the breadth of cuboid :"))
h=int(input("Enter the height of cuboid :"))
print("Area of cuboid :",cubArea(l,b,h))
print("Perimiter of circle :",cubPerimeter(l,b,h))

r=int(input("Enter the radius of sphere :"))
print("Area of sphere :",sphereArea(r))
print("Perimiter of sphere :",spherePerimeter(r))