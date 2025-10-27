import time
import math
import cmath

while True:
    print("What 3D shape do you want to work with?")
    time.sleep(2)
    print("A.Cube")
    print("B.Cubiod")
    print("C.Sphere")
    print("D.Cylinder")
    print("E.Cone")
    print("F.Square base pyramid")
    print("G.Triangular base pyramid")
    print("H.Triangular Prism")

    volume = input("Enter the letter to execute the operation: ")

    if volume.lower() == "a":
        l = float(input("Enter the length of one side of the cube(cm): "))
        bing = math.pow(l, 3)
        time.sleep(0.5)
        print(f"The volume of the cube is {bing}cm³")
        lmao = input("Do you want to do any other operations, Y/N:")
        if lmao.lower() == "n":
            break
    elif volume.lower() == "b":
        l = float(input("Enter the length of the cubiod(cm): "))
        w = float(input("Enter the width of the cubiod(cm): "))
        h = float(input("Enter the height of the cubiod(cm): "))
        bing = l * h * w
        time.sleep(0.5)
        print(f"The volume of the cubiod is {bing}cm³")
        lmao = input("Do you want to do any other operations, Y/N:")
        if lmao.lower() == "n":
            break
    elif volume.lower() == "c":
        r = float(input("Enter the radius of the sphere(cm): "))
        bing = 4 / 3 * math.pi * math.pow(r, 3)
        time.sleep(0.5)
        print(f"The volume of the sphere is {bing}cm³")
        lmao = input("Do you want to do any other operations, Y/N:")
        if lmao.lower() == "n":
            break
    elif volume.lower() == "d":
        r = float(input("Enter the radius of the cylinder(cm): "))
        h = float(input("Enter the height of the cylinder(cm): "))
        bing = math.pow(r, 2) * h * math.pi
        time.sleep(0.5)
        print(f"The volume of the cylinder is {bing}cm³")
        lmao = input("Do you want to do any other operations, Y/N:")
        if lmao.lower() == "n":
            break
    elif volume.lower() == "e":
        r = float(input("Enter the radius of the cone(cm): "))
        h = float(input("Enter the height of the cone(cm): "))
        bing = 1 / 3 * math.pi * math.pow(r, 2) * h
        time.sleep(0.5)
        print(f"The volume of the cone is {bing}cm³")
        lmao = input("Do you want to do any other operations, Y/N:")
        if lmao.lower() == "n":
            break
    elif volume.lower() == "f":
        b = float(input("Enter the base of the pyramid(cm): "))
        h = float(input("Enter the height of the pyramid(cm): "))
        bing = 1 / 3 * math.pow(b, 2) * h
        time.sleep(0.5)
        print(f"The volume of the pyramid is {bing}cm³")
        lmao = input("Do you want to do any other operations, Y/N:")
        if lmao.lower() == "n":
            break
    elif volume.lower() == "g":
        l = float(input("Enter the length of base of the pyramid(cm): "))
        h = float(input("Enter the height of the triangular base of the pyramid(cm): "))
        hh = float(input("Enter the height of the pyramid(cm): "))
        b = l * h * 0.5
        bing = 1 / 3 * b * hh
        time.sleep(0.5)
        print(f"The volume of the pyramid is {bing}cm³")
        lmao = input("Do you want to do any other operations, Y/N:")
        if lmao.lower() == "n":
            break
    elif volume.lower() == "h":
        l = float(input("Enter the length of prism(cm): "))
        h = float(input("Enter the triangle height(cm): "))
        b = float(input("Enter the triangle base(cm): "))
        bing = l * b * h * 0.5
        time.sleep(0.5)
        print(f"The volume of the triangular prism is {bing}cm³")
        lmao = input("Do you want to do any other operations, Y/N:")
        if lmao.lower() == "n":
            break
    else:
        print("Something went wrong, try again...")
