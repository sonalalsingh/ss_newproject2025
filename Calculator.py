def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

while True:
    print("Select Operation :\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Exit")

    a=float(input("Enter first number: "))
    b=float(input("Enter Second number: "))

    choice=input("Enter choice (1/2/3/4/5): ")

    if choice=='1':
        print(a," + ",b," = ",add(a,b))

    elif choice=='2':
        print(a," - ",b," = ",sub(a,b))
    elif choice=='3':
        print(a," * ",b," = ",mul(a,b))
    elif choice=='4':
        print(a," / ",b," = ",div(a,b))
    elif choice=='5':
        break
    else:
        print("invalid choice input")
