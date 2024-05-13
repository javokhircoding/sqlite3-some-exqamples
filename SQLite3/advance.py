import sqlite3
from argparse import ArgumentParser, Namespace




dat = str(input("What is your database name: "))
file = dat+".db"
db = sqlite3.connect(file)
print(f"Yout Database named {file} \n")

#db.execute(''' CREATE TABLE IF NOT EXISTS info(
#        ID INT PRIMARY KEY NOT NULL, 
#        NAME TEXT NOT NULL,
#        DIVISION TEXT NOT NULL,
#        PHONE TEXT NOT NULL
#    ) ''')
#db.commit()



#############################EXAMPLE
def creation(name, key):
    db.execute(''' CREATE TABLE IF NOT EXISTS name(
        ID INT PRIMARY KEY NOT NULL,
        NAME TEXT NOT NULL,
        DIVISION TEXT NOT NULL,
        PHONE TEXT NOT NULL 
    )''')
#############################


#ONE
def one(name, key):
    db.execute(''' CREATE TABLE IF NOT EXISTS {name}(
        ID INT PRIMARY KEY NOT NULL,
        {key} TEXT NOT NULL
    ) ''')
    db.commit()
    ques()
    print("Done!")


#TWO
def two(name, key1, key2):
    db.execute(''' CREATE TABLE IF NOT EXISTS {name}(
        ID INT PRIMARY KEY NOT NULL, 
        {key1} TEXT NOT NULL,
        {key2} TEXT NOT NULL
    ) ''')
    db.commit()
    ques()
    print("Done!")


#THREE
def three(name, key1, key2, key3):
    db.execute(''' CREATE TABLE IF NOT EXISTS {name}(
        ID INT PRIMARY KEY NOT NULL, 
        {key1} TEXT NOT NULL,
        {key2} TEXT NOT NULL,
        {key3} TEXT NOT NULL
    ) ''')
    db.commit()
    ques()
    print("Done!")


#FOUR
def four(name, key1, key2, key3):
    db.execute(''' CREATE TABLE IF NOT EXISTS {name}(
        ID INT PRIMARY KEY NOT NULL, 
        {key1} TEXT NOT NULL,
        {key2} TEXT NOT NULL,
        {key3} TEXT NOT NULL,
        {key4} TEXT NOT NULL
    ) ''')
    db.commit()
    ques()
    print("Done!")


#FIVE
def five(name, key1, key2, key3):
    db.execute(''' CREATE TABLE IF NOT EXISTS {name}(
        ID INT PRIMARY KEY NOT NULL, 
        {key1} TEXT NOT NULL,
        {key2} TEXT NOT NULL,
        {key3} TEXT NOT NULL,
        {key4} TEXT NOT NULL,
        {key5} TEXT NOT NULL
    ) ''')
    db.commit()
    ques()
    print("Done!")




############################FUNCTIONS
def insert(ID, NAME, DIVISION, PHONE):
    db.execute(''' INSERT INTO info(ID, NAME, DIVISION, PHONE)
        VALUES(?,?,?,?)''',(ID, NAME, DIVISION, PHONE))
    db.commit()


def update():
    db.execute(''' UPDATE info set DIVISION = "SOMEONE" WHERE ID = 1 ''')


def delete():
    db.execute(''' DELETE from info WHERE ID = 1 ''')

###################BEGINNING############################

def ques():
    q = int(input("What do you want to do(help(0)(DONE(5))): "))


    if q == 0:
        print('For: \nCreate Table(1) \nDelete(2) \nUpdate(3) \nInsert(4)')
        ques()

    elif q == 5:
        db.commit()
        db.close()
        exit()
################CREATE TABLE####################NOT YET
    elif q == 1:
        print("You've choosen Create Table")
        name = str(input("Enter the name of table: "))
        a = int(input("How much keys you want(max 5): "))
        
        if a == 1:
            b = str(input("Enter the name of key: "))
            one(name, b)


        elif a == 2:
            b, c = map(str, input("Enter the names of keys(KEY1, KEY2)").split())
            two(name, b, c)
##################DELETE########################DONE
    elif q == 2:
        de = int(input("Which ID(line) you want to delete: "))
        if de == 1:
            db.execute(''' DELETE from info WHERE ID = 1 ''')
        elif de == 2:
            db.execute(''' DELETE from info WHERE ID = 2 ''')
        elif de == 3:
            db.execute(''' DELETE from info WHERE ID = 3 ''')
        elif de == 4:
            db.execute(''' DELETE from info WHERE ID = 4 ''')
        elif de == 5:
            db.execute(''' DELETE from info WHERE ID = 5 ''')
        elif de == 6:
            db.execute(''' DELETE from info WHERE ID = 6 ''')
        elif de == 7:
            db.execute(''' DELETE from info WHERE ID = 7 ''')
        elif de == 8:
            db.execute(''' DELETE from info WHERE ID = 8 ''')
        elif de == 9:
            db.execute(''' DELETE from info WHERE ID = 9 ''')
        elif de == 10:
            db.execute(''' DELETE from info WHERE ID = 10 ''')
        db.commit()
        print("Done!")
        ques()

##################UPDATE########################NOT YET
    elif q == 3:
        de = int(input("Which ID you want to change: "))
        
        
            




#####################INSERT######################DONE
    elif q == 4:
        h = int(input("How much lines you want to add: "))
        i = 0
        while i < h:
            def insert(NAME, DIVISION, PHONE):
                db.execute(''' INSERT INTO info(
                    ID, NAME, DIVISION, PHONE)
                        VALUES(?,?,?,?)''',(i+1, NAME, DIVISION, PHONE))
            a = str(input("Enter the name: "))
            b = str(input("Enter the division: "))
            c = str(input("Enter the phone number: "))
            insert(a, b, c)
            print("Done! Go on for another")

            i +=1
            
        ques()





ques()
#delete()
#update()
#insert()
#db.commit()

#db.close()