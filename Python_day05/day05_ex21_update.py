import sqlite3

conn = sqlite3.connect("test.db")
sql = """update saram set name=?, age=? where id=?"""

update_data = [
    ('yushin', 35, 'kim'),
    ('yun', 20, 'lee'),
    ('shin', 15, 'choi')
    ]

c = conn.cursor()
c.executemany(sql, update_data)

c.close()

# 입력수정 삭제 할때 commit 필수
conn.commit()
conn.close()