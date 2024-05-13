from advance import one

q = int(input("What do you want to do(help(00) for help): "))


if q == 00:
    print('For: \nCreate Table(1) \nDelete Table(2) \nUpdate Table elements(3) \nInsert(4)')
    print("Use this programm again!")


elif q == 1:
    name = input("Enter the name of table: ")
    a = input("How much keys you want: ")
    if a == 1:
        b = input("Enter the name of key: ")
        one(name, b)
