import sqlite3

conn = sqlite3.connect('./saveFiles/biography.db')
curs = conn.cursor()

curs.execute("update people set pay=? where name=?",
             (900, '홍길동36'))

curs.execute("delete from people where pay=?", (1200,))

conn.commit()
print('레코드 update/delete 및 commit 완료')