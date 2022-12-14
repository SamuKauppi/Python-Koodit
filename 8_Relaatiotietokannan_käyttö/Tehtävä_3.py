import mysql.connector
from geopy import distance


def avaa_tietokanta():
    yhteys = mysql.connector.connect(
        host='localhost',
        port=3306,
        database='flight_game',
        user='root',
        password='Nevermindme',
        autocommit=True)
    return yhteys


def etsi_lentoasemat(yhteys, maakoodi_a, maakoodi_b):
    sql = "SELECT airport.latitude_deg, airport.longitude_deg FROM airport "
    sql += "WHERE airport.ident = '" + maakoodi_a + "' or airport.ident = '" + maakoodi_b + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos


yhteys = avaa_tietokanta()
maakoodi_a = input("Syötä ensimmäinen koodi: ")
maakoodi_b = input("Syötä toinen koodi: ")

kaksi_asemaa = etsi_lentoasemat(yhteys, maakoodi_a, maakoodi_b)
if len(kaksi_asemaa) > 0:
    gap = distance.distance(kaksi_asemaa[0], kaksi_asemaa[1]).km
    print(f"Lentoasemien välinen etäisyys on: {gap:0.3f}km")
