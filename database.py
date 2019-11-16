import psycopg2 as pg2

def read_users():
    conn = pg2.connect("dbname='python_lab_game' user='postgres' host='localhost' password='davopro112'") #make connection
    cur = conn.cursor() # make cursor

    cur.execute('SELECT * FROM users') #make query
    print(cur.fetchall()) #fetch some shit

    conn.close() #closes connection