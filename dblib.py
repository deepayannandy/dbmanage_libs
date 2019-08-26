import sqlite3

conn = sqlite3.connect('dny.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS chat(query TEXT, responce TEXT)")

def data_entry(x,y):
    c.execute("INSERT INTO chat VALUES(?,?)",(x,y))
    conn.commit()
    c.close()
    
    print("Saved successfully!")

def read_all_db():
    conn = sqlite3.connect('dny.db')
    c = conn.cursor()
    c.execute('SELECT * FROM chat')
    data = c.fetchall()
    for row in data:
        print(row)
def find_reply(x):
    conn = sqlite3.connect('dny.db')
    c = conn.cursor()
    c.execute('SELECT responce FROM chat WHERE query = ?',(x,))
    data = c.fetchall()
    if len(data)==0:
        return("null")
    else:
        d=data[0]
        #print(data)
        #print(type(d[0]))
        return(d[0])

create_table()
