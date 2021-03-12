import sqlite3

conn = sqlite3.connect("test.db")
sql = '''select * from saram order by name desc'''

c = conn.cursor()
c.execute(sql)

#print(c.fetchone())
#fetchall() 은 전부다 가져옴


for s in c.fetchmany(3) :
    print(s)

c.close()
conn.close()