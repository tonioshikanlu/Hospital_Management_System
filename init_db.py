
from voyager.db import get_db

def main():
    with get_db() as conn:
        with open('sqlite-schema.sql') as f:
            conn.executescript(f.read())
        conn.commit()
        with open('test-data.sql') as f:
            conn.executescript(f.read())
        conn.commit()

if __name__ == '__main__':
    main()
