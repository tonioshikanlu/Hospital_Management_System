from flask import g

import sqlite3
## import psycopg2 as pg
## from psycopg2.extras import DictCursor


## def postgres_connect():
##     return pg.connect(
##         "dbname='testdb' user='test-user' host='localhost' password='test'")

def sqlite_connect():
    conn = sqlite3.connect(
        "test.db",
        detect_types=sqlite3.PARSE_DECLTYPES
    )
    conn.row_factory = sqlite3.Row
    return conn

def get_db():
    return sqlite_connect()

def execute(conn, stmt, *args, **kwargs):
    return sqlite_execute(conn, stmt, *args, **kwargs)

def sqlite_execute(conn, stmt, *args, **kwargs):
    cursor = conn.cursor()
    cursor.execute(stmt, *args, **kwargs)
    return [dict(r) for r in cursor.fetchall()]

## def postgres_execute(conn, stmt, *args, **kwargs):
##     with get_db() as conn:
##         with conn.cursor(cursor_factory=DictCursor) as cursor:
##             cursor.execute("SELECT * FROM Voyages")
##             return cursor.fetchall()

