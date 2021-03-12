import sqlite3

conn = sqlite3.connect('test.db')
sql = '''
    insert into saram(id, name, age)
    values('park','gildong', 34)

'''

c = conn.cursor()
c.execute(sql)
c.close()

# 입력, 수정, 삭제 기능