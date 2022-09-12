import mysql.connector
from collections import Counter


def avaa_tietokanta():
    yhteys = mysql.connector.connect(
        host='localhost',
        port=3306,
        database='flight_game',
        user='root',
        password='Nevermindme',
        autocommit=True)
    return yhteys


def etsi_lentokenttientyypit(yhteys, maakoodi):
    sql = "SELECT airport.type FROM airport "
    sql += "WHERE iso_country = '" + maakoodi + "' ORDER BY type;"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for i in range(len(tulos)):
            tulos[i] = str(tulos[i]).replace("('", "")
            tulos[i] = str(tulos[i]).replace("',)", "")
    return tulos


yhteys = avaa_tietokanta()
maakoodi = input("Syötä maakoodi: ")
lentokenttaTyypit = etsi_lentokenttientyypit(yhteys, maakoodi)

counts = dict(Counter(lentokenttaTyypit))
duplicates = {key: value for key, value in counts.items() if value > 1}

for i in duplicates:
    print(f"{i}: {duplicates.get(i)}")
