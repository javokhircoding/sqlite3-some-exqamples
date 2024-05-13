import sqlite3 


db = sqlite3.connect("Data.db")

db.execute(''' CREATE TABLE IF NOT EXISTS info(
    ID INT PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    DIVISION TEXT NOT NULL,
    PHONE TEXT NOT NULL 
) ''')


i = 0
while i < 6:
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
    db.commit()



db.commit()
db.close()