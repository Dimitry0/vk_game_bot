import sqlite3 as sql

con = sql.connect('userss.db')

with con:
    db = con.cursor()
    db.execute("""CREATE TABLE IF NOT EXISTS `userss`
        (id INTEGER PRIMARY KEY AUTOINCREMENT DEFAULT 0, 
        vk_id STRING,
        clicks INTEGER DEFAULT 0)
        """)
    con.commit()

class UsersInfo:

    def rows():
        db.execute("SELECT COUNT(*) FROM 'userss'")
        con.commit()
        values = db.fetchone()
        return int(values[0])

    def is_reg(user_vk_id):
        db.execute(f"SELECT * FROM 'userss' WHERE vk_id= '{user_vk_id}'")
        con.commit()
        values = db.fetchone()
        if values is None:
            return False
        else:
            return True

    def insert(user_vk_id):
        db.execute(f"INSERT INTO 'userss' (vk_id) VALUES (?)", (user_vk_id,))
        con.commit()

    def get_clicks(user_vk_id):
        db.execute(f"SELECT clicks FROM 'userss' WHERE vk_id= '{user_vk_id}'")
        con.commit()
        values = db.fetchone()
        return values[0]

    def update_clicks(user_vk_id, clicks):
        db.execute(f"UPDATE 'userss' SET clicks = {clicks} WHERE vk_id = {user_vk_id}")
        con.commit()

    def update_stavka(user_vk_id, stavka):
        db.execute(f"UPDATE 'userss' SET stavka = {stavka} WHERE vk_id = {user_vk_id}")

        con.commit()


    def get_top(count):
        db.execute(f"SELECT vk_id, clicks FROM 'userss' ORDER BY clicks DESC LIMIT {count}")
        con.commit()
        values = db.fetchall()
        return values
    def get_profile(user_id):
        db.execute(f"SELECT clicks FROM userss WHERE vk_id = {user_id}")
        con.commit()
        value = db.fetchall()
        return value