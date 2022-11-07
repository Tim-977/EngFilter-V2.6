import sqlite3


def insert_result(name, mark,
                  comment):  # Функция, позволяющая внести отзыв и оценку в БД
    con = sqlite3.connect(name)
    cur = con.cursor()
    sqlite_insert_with_param = """INSERT INTO maintable(Mark,Comment) VALUES(?, ?)"""
    data_tuple = (mark, comment)
    cur.execute(sqlite_insert_with_param, data_tuple)
    con.commit()
    con.close()
