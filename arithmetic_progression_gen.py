print("----- Arithmetic Progression (AP) Calculator -----\n")
first = int(input("Type the first number of the AP: "))
cvalue = int(input("Type the constant value between numbers of the AP: "))
n = int(input("Type how many numbers you want in your AP sequence: "))
cont = 0
list = []
while cont < n:
    list.append(first)
    first += cvalue
    cont +=1
print("\n", list, "\n")
print("-"*50)
