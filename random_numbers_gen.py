def random():
    from random import randint
    print("This program generates random numbers between 1 and 50,\
presents the sum of them and order them from lower to higher.")
    print("You get to choose how many random numbers will be presented.\n")
    try:
        n=int(input("Type the quantity of random numbers you want: "))
        print(" ")
    except:
        print("Invalid input. Try a whole number.")
        random()
    else:
        i=1
        soma=0
        lista=[]
        while i <= n:
            x = randint(1, 50)
            if x in lista:
                continue
            else:
                print("Number {} is {}.".format(i, x))
                i+=1
                soma+=x
                lista.append(x)
        print("\nThe sum of {} random numbers is {}.".format(i-1, soma))
        print("\nThe random numbers in an increasing sequence are: ")
        a = lista.copy()
        a.sort()
        for b in a:
            print("{}, ".format(b), end="")
random()
