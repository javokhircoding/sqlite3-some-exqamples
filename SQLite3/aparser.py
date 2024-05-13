import sqlite3
from argparse import ArgumentParser, Namespace




dat = str(input("What is your database name: "))
file = dat+".db"
db = sqlite3.connect(file)
print(f"Yout Database named {file} \n")





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
