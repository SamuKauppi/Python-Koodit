import json
from flask import Flask, request, Response
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
    if len(values) < 1:
        return ""
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


@app.route('/kentta/<koodi>')
def kentta(koodi):
    try:
        connection = open_database()

        name = get_from_database(connection, "name", "airport", f"where ident = '{koodi}'")
        city = get_from_database(connection, "municipality", "airport", f"where ident = '{koodi}'")

        if name == '' or city == '':
            raise ValueError('Icao-code not found')

        answer = {
            "ICAO": koodi.upper(),
            "Name": name,
            "Municipality": city
        }
    except ValueError:
        errorcode = 400
        answer = {
            "status": errorcode,
            "text": "invalid code"
        }

    json_data = json.dumps(answer, default=lambda o: o.__dict__, indent=4)
    return json_data


@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status": "404",
        "teksti": "page not found"
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=404, mimetype="application/json")


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
