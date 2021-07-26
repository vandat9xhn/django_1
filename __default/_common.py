import sqlite3


#

url_sql = 'D:\\web\\react-django\\react_django_1\\db.sqlite3'


def repeat_str(string, time, delimiter=','):
    return delimiter.join([string] * time)


def get_connection():
    conn = sqlite3.connect(url_sql)

    return conn


def insert_into_sqlite3(conn, table_name, col_list, data):
    cur = conn.cursor()
    str_col_list = ','.join(col_list)

    cur.executemany(
        f'Insert Or Replace Into {table_name}({str_col_list}) Values(' + repeat_str(
            '?', len(col_list)
        ) + ')',
        data
    )


def commit_sqlite3(conn):
    conn.commit()


def close_sqlite3(conn):
    conn.close()
