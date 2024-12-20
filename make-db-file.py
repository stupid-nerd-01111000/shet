from sqlite3 import connect


con = connect('my-site.db')

cur = con.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS acount_info(id, usrname, number)')


res = cur.execute("SELECT id FROM acount_info")
res.fetchone()