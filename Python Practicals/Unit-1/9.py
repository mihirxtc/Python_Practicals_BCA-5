# 9. Write a menu driven python program which perform the following:
# Find area of circle
# Find area of triangle
# Find area of square and rectangle
# Find Simple Interest
# Exit.

choice = 0
while(choice!=5):
    print("1. Find area of circle")
    print("2. Find area of triangle")
    print("3. area of square and rectangle")
    print("4. Find Simple interest")
    print("5. Exit.")

    choice = int(input("Enter your choice: "))
    if choice==1:
        PI = 3.14
        radius = float(input("Please enter the radius of a circle: "))
        area = PI * radius * radius
        circumference = 2 * PI * radius
        print(" Area of a Circle = %.2f" %area)
        print(" Circumference of a Circle = %.2f" %circumference)

    elif choice==2:
        a = float(input("Enter first side: "))
        b = float(input("Enter second side: "))
        c = float(input("Enter third side: "))

        # Calculate the semi-perimeter
        s = (a + b + c) / 2

        # Calculate the area
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        print("The are of the triangle is %0.2f" %area)

    elif choice==3:
        side = int(input("Enter side length of Square: "))
        area_square = side * side
        print ("Area of Square : ", area_square )
    
        width = float(input("Please Enter the Width of a Rectangle: "))
        height = float(input("Please Enter the Height of a Rectangle: "))

        # Calculate the area
        Area = width * height

        # Calculate the Perimeter
        Perimeter = 2 * (width + height)
        print("\n Area of a Rectangle is: %.2f" %Area)
        print("\n Perimeter is: %.2f" %Area)

    elif choice==4:
        p = int(input("Enter P: "))
        r = int(input("Enter R: "))
        n = int(input("Enter N: "))
        i = (p * r * n) / 100
        print(i)

    elif choice==5:
        exit()

    else:
        print("Bye Bye!")