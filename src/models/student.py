from pydantic import BaseModel
import sqlite3


class Student(BaseModel):
    name: str
    email: str


class Database:
    def __init__(self):
        self.db = sqlite3.connect(":memory:")
        self.create_table()

    def create_table(self):
        cursor = self.db.cursor()
        cursor.execute(
            "CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)"
        )
        self.db.commit()

    def add_user(self, user: Student):
        cursor = self.db.cursor()
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)", (user.name, user.email)
        )
        self.db.commit()

    def get_all_users(self) -> list[Student]:
        cursor = self.db.cursor()
        cursor.execute("SELECT id, name, email FROM users")
        rows = cursor.fetchall()
        return [Student(name=row[1], email=row[2]) for row in rows]


db = Database()
