import sqlite3
import functools

class DatabaseConnection(conscr, commprot):
    def __init__(self, conscr, commprot):
        self.connecion = open(conscr, commprot)

    def __enter__(self):
        return self.connection

    def __exit__(self, type, value, traceback):
        self.connection.close()

with DatabaseConnection(SELECT * FROM users, "r") as query:
    query.read()
