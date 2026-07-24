def calc():
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def mul(a,b):
        return a*b
    def div(a,b):
        return a/b
    while True:
        print("\n1.Addition")
        print("2.Subtraction")
        print("3.Multiplication")
        print("4.Division")
        print("5.Exit")
        choice=int(input("enter your choice:"))
        if choice == 5:
            print("THANK YOU")
            break
        a=int(input("enter a:"))
        b=int(input("enter b:"))
        if choice==1:
            print("Addition:",add(a,b))
        elif choice==2:
            print("Subtraction:",sub(a,b))
        elif choice==3:
            print("Multiplication:",mul(a,b))
        elif choice==4:
            if b==0:
                print("division by 0 is not allowed")
            else:
                print("Division:",div(a,b))
        else:
            print("INVALID CHOICEE")
calc()