def fiboseq():
    a=0
    b=1
    cont=0
    print(" Fibonacci Sequence Generator ".center(54, "-"))
    print(" ")
    try:
        n=int(input("How many numbers from Fibonacci sequence do you want? "))
        if n<2:
            print("Type a number equal to or bigger than 2.")
        else:
            prim = int(input("Type a number from where you want to start a sequence: "))
            print(" ")
            while True:
                c=a+b
                a=b
                b=c
                if c>prim:
                    break
            while cont<n:
                print("{}, ".format(c), end="")
                c=a+b
                a=b
                b=c
                cont+=1
    except ValueError:
        print("Invalid input. Try a whole number equal to or bigger than 2.")
    print("\n")
    print("-"*54)
    again = input(("Wanna try again? (y/n) "))
    if again.lower() == "y":
        fiboseq()
    else:
        print("Goodbye!")
fiboseq()
