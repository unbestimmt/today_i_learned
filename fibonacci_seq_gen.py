a=0
b=1
cont=2 
print(" Fibonacci Sequence Generator ".center(54, "-"))
print(" ")
try:
    n=int(input("How many numbers from Fibonacci sequence do you want? "))
    if n<2:
        print("Type a number equal to or bigger than 2.")
    else:
        print("0, 1", end="")
        while cont<n:
            c=a+b
            a=b
            b=c
            print(", {}".format(c), end="")
            cont+=1
except ValueError:
    print("Invalid input. Try a whole number equal to or bigger than 2.")
print("\n")
print("-"*54)
