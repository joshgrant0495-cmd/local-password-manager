import sqlite3
from pathlib import Path


class DatabaseManager:
    def __init__(self):
        database_directory = Path("master_encryption")
        database_directory.mkdir(exist_ok=True)
        self.conn = sqlite3.connect("master_encryption/password.db")
        self.cursor = self.conn.cursor()
        self.access_table()

    def access_table(self):
        self.cursor.execute("CREATE TABLE if not exists "
                            "user_information(ID INTEGER PRIMARY KEY AUTOINCREMENT,"
                            "name TEXT, username TEXT, password TEXT, information TEXT)")

    def save_record(self, name, username, password, information):
        self.cursor.execute("INSERT INTO user_information (name, username, password, information) "
                             "VALUES (?, ?, ?, ?)", (name, username, password, information))
        self.conn.commit()

    def retrieve_names(self):
        self.cursor.execute("SELECT NAME FROM user_information")
        rows = self.cursor.fetchall()
        return [row[0] for row in rows]

    def get_db_info(self, name):
        self.cursor.execute("SELECT id, username, password, information FROM user_information WHERE NAME = ?", (name,))
        row = self.cursor.fetchone()
        if row is None:
            return None
        return {"id": row[0], "username": row[1], "password": row[2], "information": row[3]}

    def delete_record(self, id):
        self.cursor.execute("DELETE FROM user_information WHERE ID = ?", (id,))
        self.conn.commit()

    def close_database(self):
        self.conn.close()



