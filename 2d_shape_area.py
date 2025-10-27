import math
import cmath
import time

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
