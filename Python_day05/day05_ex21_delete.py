import sqlite3

conn = sqlite3.connect("test.db")
sql = """delete from saram where name='{}'"""

del_name = 'lee'

c = conn.cursor()
c.execute(sql.format())

c.close()

# 입력수정 삭제 할때 commit 필수
conn.commit()
conn.close()