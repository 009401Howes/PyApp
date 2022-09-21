#App
t = "1"
DebugMode = False
while(t == "1"):
    AppOpened = input("Type an app to open, or type 'help' to see a list of apps/commands\n ")
    if DebugMode == True:
        print(AppOpened)
#Calculator
    if AppOpened == "calculator":
        CalculatorOpen = True
        while(CalculatorOpen == True):
            inp = input("+(1), -(2), X(3), ÷(4) or exit(5): ")
            if DebugMode == True:
                print(inp)
            if inp == "1":
                            # Store input numbers
                num1 = input("Enter first number: ")
                if DebugMode == True:
                    print(num1)
                num2 = input("Enter second number: ")
                if DebugMode == True:
                    print(num2)
                # Add two numbers
                sum = float(num1) + float(num2)
                if DebugMode == True:
                    print(sum)
                # Display the sum
                print("{0} + {1} = {2}".format(num1, num2, sum))
            elif inp == "2":
                                        # Store input numbers
                num1 = input("Enter first number: ")
                if DebugMode == True:
                    print(num1)
                num2 = input("Enter second number: ")
                if DebugMode == True:
                    print(num2)
                # Add two numbers
                sum = float(num1) - float(num2)
                if DebugMode == True:
                    print(sum)
                # Display the sum
                print("{0}  {1} = {2}".format(num1, num2, sum))
            elif inp == "5":
                CalculatorOpen = False
    #exit
    elif AppOpened == "exit":
        exit()
    elif AppOpened == "settings":
        print("What setting would you like to change?\nThe options are:\n")
    else:
        print ("Unknown command\nplease try again")
