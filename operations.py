def convert(input):
    from fractions import Fraction
    if "/" in input:
        return float(Fraction(input))
    else:
        return float(input)  
def another():
        while True:
            yn = input("Would you like to ask another? (Y/N): ")
            if(yn=="y") or (yn=="Y") or (yn=="yes") or (yn=="Yes"):
                whichone()
            if(yn=="n") or (yn=="N") or (yn=="no") or (yn=="No"):
                exit()
            else:
                print("Please answer with Y or N.")
                continue
def operation():
    a=(input("Add, Subtract, Divide, or Multiply:  "))

    if(a=="Add") or (a=="add") or (a=="adding") or (a=="Adding") or (a=="+") or (a=="a") or (a=="A"):
        while True:
            b=(input("First Number: "))
            c=(input("Second Number: "))
            try:
                added=float(b)+float(c)
                string=str(added)
                total=string.rstrip('0')
                print("Sum:", total)
                another()
            except ValueError:
                print("Please try again with numbers.")
                continue

    if(a=="subtract") or (a=="Subtract") or (a=="Subtracting") or (a=="subtracting") or (a=="-") or (a=="s") or (a=="S"):
        while True:
            b=(input("First Number: "))
            c=(input("Second Number: "))
            try:
                subtracted=float(b)-float(c)
                string=str(subtracted)
                total=string.rstrip('0')
                print("Difference:", total)
                another()
            except ValueError:
                print("Please try again with numbers.")
                continue
       
    if(a=="multiply") or (a=="Multiply") or (a=="Multiplying") or (a=="multiplying") or (a=="x") or (a=="X") or (a=="*") or (a=="m") or (a=="M"):
        while True:
            b=(input("First Number: "))
            c=(input("Second Number: "))
            try:
                multiplied=float(b)*float(c)
                string=str(multiplied)
                total=string.rstrip('0')
                print("Product:", total)
                another()
            except ValueError:
                print("Please try again with numbers.")
                continue
    
    if(a=="divide") or (a=="divide") or (a=="dividing") or (a=="Dividing") or (a=="/") or (a=="d") or (a=="D"):
        while True:
            b=(input("First Number: "))
            c=(input("Second Number: "))
            if(c=="0"):
                print("Quotient: undefined")
                another()

            try:
                divided=float(b)/float(c)
                string=str(divided)
                total=string.rstrip('0')
                print("Quotient:", total)
                another()

            except ValueError:
                print("Please try again with numbers.")
                continue

    else:
        print("Please pick either Add, Subtract, Multiply, or Divide.")
        operation()
def equation():
    
    from fractions import Fraction
    global c
    a_1 = input("Insert your first 'x' coordinate here: ")
    b_1 = input("Insert your first 'y' coordinate here: ")
    c_1 = input("Insert your second 'x' coordinate here: ")
    d_1 = input("Insert your second 'y' coordinate here: ")
    a = convert(a_1)
    b = convert(b_1)
    c = convert(c_1)
    d = convert(d_1)
    def graphing():
        from pyautogui import press, typewrite, hotkey
        import webbrowser
        import time
        graphed = input("Would you like your equation graphed? (Y/N): ")
        while True:
            if(graphed=="y") or (graphed=="Y") or (graphed=="yes") or (graphed=="Yes"):    
                            webbrowser.open_new("https://www.desmos.com/calculator")
                            time.sleep(1)
                            typewrite(printed)
                            another()
            if(graphed=="n") or (graphed=="N") or (graphed=="no") or (graphed=="No"):
                            another()
            else:
                print("Please answer with Y or N.")
                continue
    while True:
        yn=input(f"Are your coodinates ({a}, {b}) ({c}, {d}): ")

        try:

            if(a==b==c==d) or ((a==c) and (b==d)):
                print("Please give 2 different points.")
                equation()

            if((int(a)==0) and (int(c)==0)) or ((float(c)-float(a))==0):
                print("Your slope is: 0")
                printed=str(f"x={a.rstrip}")
                print(printed)
                graphing()

            if((int(b)==0) and (int(d)==0)) or ((float(d)-float(b))==0):
                print("Your slope is: 0")
                printed=str(f"y={b}")
                print(printed)
                graphing()

            if(int(a)==0) and (int(c)==0) or ((float(a)-float(c))==0):
                slope=0
                print(f"y={float(str(c).rstrip('0'))-float(str(a).rstrip('0'))}")
                graphing()

            else:
                if(yn=="y") or (yn=="Y") or (yn=="yes") or (yn=="Yes"):
                    slope = (float(d)-float(b))/(float(c)-float(a))
                    yint_strip=str(b-slope*a).rstrip('.0')
                    slope_strip=str(slope).rstrip('.0')
                    print("Your slope is:", slope_strip)
                    print(f"Your equation in point-slope form is: y-{str(b).rstrip('.0')}={slope_strip}(x-{str(a).rstrip('.0')})")
                    yint_strip=str(b-slope*a).rstrip('.0')
                    slope_strip=str(slope).rstrip('.0')
                    printed=str(f"y={slope_strip}x+{yint_strip}")
                    print(f"Your equation in slope-intercept form is: {printed}")
                    graphing()

                if(yn=="n") or (yn=="N") or (yn=="no") or (yn=="No"):
                    print("Please insert your coordinates again.")
                    equation()

                else:
                    print("Please answer with Y or N.")
                    continue
        except ValueError:
            print("Please only enter numbers.")
            equation()
def whichone():
    options = ["Operations", "Solve for the equation of a line"]

    for i, choice in enumerate(options, start=1):
        print(f"{i}. {choice}")


    while True:
        try:
            number = int(input("Please enter the number corresponding to your choice: "))
            if 1 <= number <= len(options):
                break
            else:
                print("Please pick one of the choices.")
        except ValueError:
            print("Please only enter numbers.")

    if(number==1):
        operation()
    if(number==2):
        equation()
whichone()