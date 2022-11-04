import sqlite3


def insert_result(name, mark, comment):
    con = sqlite3.connect(name)
    cur = con.cursor()
    sqlite_insert_with_param = """INSERT INTO maintable(Mark,Comment) VALUES(?, ?)"""
    data_tuple = (mark, comment)
    cur.execute(sqlite_insert_with_param, data_tuple)
    con.commit()
    con.close()


# insert_result('reviews.db', 1, 'Hello!!!@@!!! how are u? \n i am fine')
