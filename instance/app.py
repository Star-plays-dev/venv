import sqlite3

db = sqlite3.connect("users.db")


#Создание курсора
c = db.cursor()

c.execute("""CREATE TABLE articles (
    title text,
    full_text text,
    views integer,
    author text
)""")

db.commit()

db.close()