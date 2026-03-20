import mysql.connector
import pytest

def tetstmysql_connection():
    # Establish a connection to the MySQL database
    conn = mysql.connector.connection(
        host="localhost",
        port = "8080",
        user = "root",
        password = "password",
        database = "database"
    )
    # create cursor
    cursor = conn.cursor()

    cursor.execute()

    print(cursor.fetchall())

def test_solve_longes_suvstring():
    s = "abcabdccdef"
    longest = ""
    for i in range(len(s)):
        temp = ""
        for j in range(i, len(s)):
            if s[j] not in temp:
                temp += s[j]
            else:
                break
        if len(temp) > len(longest):
            longest = temp
    print(longest)