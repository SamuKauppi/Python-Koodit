from flask import Flask, request
import mysql.connector


def open_database():
    _connection = mysql.connector.connect(
        host='localhost',
        port=3306,
        database='flight_game',
        user='root',
        password='Nevermindme',
        autocommit=True)
    return _connection


def execute_sql(connection, sql):
    # print(f"execute: [{sql}]")
    cursor = connection.cursor()
    cursor.execute(sql)
    values = cursor.fetchall()
    return values


# Hakee tietokannasta
def get_from_database(connection, column, table, where):
    sql = "SELECT " + column + " FROM " + table + " " + where
    values = execute_sql(connection, sql)
    values = remove_pointless(values)
    return values[0]


def remove_pointless(s):
    for i in range(len(s)):
        s[i] = str(s[i]).replace("'", "")
        s[i] = str(s[i]).replace("(", "")
        s[i] = str(s[i]).replace(")", "")
        s[i] = str(s[i]).replace(",", "")
        s[i] = str(s[i]).replace("]", "")
        s[i] = str(s[i]).replace("[", "")
    return s


app = Flask(__name__)


@app.route('/lentoaseman_tietoja')
def lentoaseman_tietoja():
    args = request.args
    koodi = str(args.get("koodi"))
    connection = open_database()

    name = get_from_database(connection, "name", "airport", f"where ident = '{koodi}'")
    city = get_from_database(connection, "municipality", "airport", f"where ident = '{koodi}'")

    vastaus = {
        "ICAO": koodi,
        "Name": name,
        "Municipality": city
    }
    return vastaus


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
