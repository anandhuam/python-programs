# --- calculator ---


while True:
    print("\n=== Calculator ===")
    
    num1 = int(input("Enter the 1st number: "))
    num2 = int(input("Enter the 2nd number: "))
 

    print("""
    Select an operation:
    1) Addition
    2) Subtraction
    3) Multiplication
    4) Division
    5) Exit
    """)

    choice = input("Enter your choice : ")
    
    if choice == '1':
        print('Result :',num1+num2)
    elif choice == '2':
        print('Result :',num1-num2)
    elif choice == '3':
        print('Result :',num1*num2)
    elif choice == '4':
        print('Result :',num1/num2)
    else:
        print('Invalid choice !')

    print("continue?")
    c=input('y/n :')
    if c == 'n':
        print("Exiting the calculator. Goodbye!")
        break
    else:
        continue

