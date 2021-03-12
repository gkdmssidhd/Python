import sqlite3

conn = sqlite3.connect('test.db')
sql ='''
    insert into saram(id, name, age)
    values(?,?,?)

'''

data=[
    ('lee','s',24),
    ('lee','s',24),
    ('lee','s',24),
    ('lee','s',24)
]

c=conn.cursor()
c.executemany(sql, data)
c.close()

# 입력, 수정, 삭제 기능은 commit
conn.commit()
conn.close()