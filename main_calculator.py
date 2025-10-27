import time
import math
import cmath

while True:
    print("What operations do you want to do?")
    time.sleep(1)
    print("A.Basic math operations ")
    print("B.SquareRoots or powers ")
    print("C.Value of Constants ")
    print("D.Rounding ")
    print("E.Factorials ")
    print("F.Quadratic Formula ")
    print("G.2D shapes area ")
    print("H.3D shapes volume ")
    operation1 = input("Enter the letter you want to work with:")
    if operation1.lower() == "a":
        num1 = float(input("Enter your first number:"))
        num2 = float(input("Enter your second number:"))

        operation = input("Select an operation, +,-,*,/:")
        if operation == "+":
            print(num1 + num2)
            time.sleep(2)
            repitation = input("Do you want to do any other operations, Y/N:")
            if repitation.lower() == "n":
                break
        elif operation == "-":
            print(num1 - num2)
            time.sleep(2)
            repitation = input("Do you want to do any other operations, Y/N:")
            if repitation.lower() == "n":
                break
        elif operation == "*":
            print(num1 * num2)
            time.sleep(2)
            repitation = input("Do you want to do any other operations, Y/N:")
            if repitation.lower() == "n":
                break
        elif operation == "/":
            print(num1 / num2)
            time.sleep(2)
            repitation = input("Do you want to do any other operations, Y/N:")
            if repitation.lower() == "n":
                break
    elif operation1.lower() == "b":
        print("Do you want to work with SquareRoots or Powers?")
        time.sleep(2)
        operation2 = input("Enter the first letter of the operation to execute:")
        if operation2.lower() == "p":
            print("Type down what do u want to calculate the power of?")
            time.sleep(2)
            base = float(input("Enter the base:"))
            power = float(input("Enter the power:"))
            print(f"The answer is {math.pow(base, power)}")
            repitation = input("Do you want to do any other operations, Y/N:")
            if repitation.lower() == "n":
                break
        elif operation2.lower() == "s":
            print("Enter the number")
            squareroot = float(input("Square Root of:"))
            time.sleep(1)
            print(math.sqrt(squareroot))
            lmao = input("Do you want to do any other operations, Y/N:")
            if lmao.lower() == "n":
                break
    elif operation1.lower() == "c":
        print("What constant value you are looking for?")
        time.sleep(2)
        print("Select one: Pi, e, inf, tau")
        constants = input("Enter one of the constants:")
        if constants.lower() == "pi":
            print(f"Pi is{math.pi}")
            lmao = input("Do you want to do any other operations, Y/N:")
            if lmao.lower() == "n":
                break
        elif constants.lower() == "e":
            print(f"Euler's number is{math.e}")
            lmao = input("Do you want to do any other operations, Y/N:")
            if lmao.lower() == "n":
                break
        elif constants.lower() == "inf":
            print(math.inf)
            lmao = input("Do you want to do any other operations, Y/N:")
            if lmao.lower() == "n":
                break
        elif constants.lower() == "tau":
            print(math.tau)
            lmao = input("Do you want to do any other operations, Y/N:")
            if lmao.lower() == "n":
                break
        else:
            print("Error 500")
    elif operation1.lower() == "d":
        rounded_value = float(input("Enter the number you want to round:"))
        print(f"Your number is {math.ceil(rounded_value)}")
        lmao = input("Do you want to do any other operations, Y/N:")
        if lmao.lower() == "n":
            break
    elif operation1.lower() == "e":
        print("Which numbers factorial do you want to get?")
        factorial = int(input("Enter the number:"))
        time.sleep(1)
        print(f"Factoral of {factorial} is {math.factorial(factorial)}")
        lmao = input("Do you want to do any other operations, Y/N:")
        if lmao.lower() == "n":
            break
    elif operation1.lower() == "f":
        print("Input the value of a b c below...")
        a = int(input("Enter the value of a: "))
        b = int(input("Enter the value of b: "))
        c = int(input("Enter the value of c: "))

        lol = math.pow(b, 2)
        lol1 = lol - 4 * a * c

        lol2 = cmath.sqrt(lol1)

        lol3 = -b + lol2

        lol4 = lol3 / 2

        # negative value of the square root

        lol5 = -b - lol2

        lol6 = lol5 / 2

        print(f"x = {lol4.real} or x = {lol6.real}")
        lmao = input("Do you want to do any other operations, Y/N:")
        if lmao.lower() == "n":
            break
    elif operation1.lower() == "g":
        while True:
            print("What equation do you want to work with?")
            print("A. Area of rectangle or square ")
            print("B. Area of Triangle ")
            print("C. Area of Parallelogram ")
            print("D. Area of Circle ")
            print("E. Area of Trapezium ")
            print("F. Area of Ellipse")
            print("G. Area of Regular Hexagon")
            print("H. Area of Sector")

            areas = input("Enter the letter to execute the operation: ")

            if areas.lower() == "a":
                h = float(input("Enter the height/length(cm): "))
                b = float(input("Enter the base/width(cm): "))
                bing = h * b
                time.sleep(0.5)
                print(f"The area of rectangle or square is {bing}cm²")
                time.sleep(1)
                lmao = input("Do you want to do any other operations, Y/N:")
                if lmao.lower() == "n":
                    break
            elif areas.lower() == "b":
                h = float(input("Enter the height/length(cm): "))
                b = float(input("Enter the base/width(cm): "))
                bing = 0.5 * b * h
                time.sleep(0.5)
                print(f"The area of triangle is {bing}cm²")
                time.sleep(1)
                lmao = input("Do you want to do any other operations, Y/N:")
                if lmao.lower() == "n":
                    break
            elif areas.lower() == "c":
                h = float(input("Enter the vertical height(cm): "))
                b = float(input("Enter the base(cm): "))
                bing = h * b
                time.sleep(0.5)
                print(f"The area of parallelogram is {bing}cm²")
                lmao = input("Do you want to do any other operations, Y/N:")
                if lmao.lower() == "n":
                    break
            elif areas.lower() == "d":
                r = float(input("Enter the radius(cm): "))
                bing = math.pi * math.pow(r, 2)
                time.sleep(0.5)
                print(f"The area of circle is {bing}cm²")
                lmao = input("Do you want to do any other operations, Y/N:")
                if lmao.lower() == "n":
                    break
            elif areas.lower() == "e":
                a = float(input("Enter the length of the first Parallel side(cm): "))
                b = float(input("Enter the length of the second Parallel side(cm): "))
                h = float(input("Enter the vertical height(cm): "))
                bing = ((a + b) / 2) * h
                time.sleep(0.5)
                print(f"The area of the trapezium is {bing}cm²")
                lmao = input("Do you want to do any other operations, Y/N:")
                if lmao.lower() == "n":
                    break
            elif areas.lower() == "f":
                a = float(input("Enter the longest radius(cm): "))
                b = float(input("Enter the shortest radius(cm): "))
                bing = a * b * math.pi
                time.sleep(0.5)
                print(f"The area of ellipse is {bing}cm²")
                lmao = input("Do you want to do any other operations, Y/N:")
                if lmao.lower() == "n":
                    break
            elif areas.lower() == "g":
                s = float(input("Enter the side length of the hexagon(cm): "))
                bing = ((math.sqrt(3) * 3) / 2) * math.pow(s, 2)
                time.sleep(0.5)
                print(f"The area of regular hexagon is {bing}cm²")
                lmao = input("Do you want to do any other operations, Y/N:")
                if lmao.lower() == "n":
                    break
            elif areas.lower() == "h":
                print("Do you want to use Radians or Degrees?")
                time.sleep(2)
                radiandegree = input("Enter the first letter of the word to run the operation: ")
                if radiandegree.lower() == "r":
                    r = float(input("Enter the radius of the circle(cm): "))
                    x = float(input("Enter the value of the angle in radians(θ): "))
                    g = math.pow(r, 2)
                    bing = 0.5 * g * x
                    time.sleep(0.5)
                    print(f"The area of sector is {bing}cm²")
                    lmao = input("Do you want to do any other operations, Y/N:")
                    if lmao.lower() == "n":
                        break
                elif radiandegree.lower() == "d":
                    r = float(input("Enter the radius of the circle(cm): "))
                    x = float(input("Enter the value of the angle in degrees(θ): "))
                    g = math.pow(r, 2)
                    bing = x / 360 * g * math.pi
                    time.sleep(0.5)
                    print(f"The area of sector is {bing}cm²")
                    lmao = input("Do you want to do any other operations, Y/N:")
                    if lmao.lower() == "n":
                        break
                else:
                    print(f"You can only enter R or D, you entered {radiandegree}")

    elif operation1.lower() == "h":
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
