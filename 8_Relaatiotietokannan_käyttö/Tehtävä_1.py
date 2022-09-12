import mysql.connector


def avaa_tietokanta():
    yhteys = mysql.connector.connect(
        host='localhost',
        port=3306,
        database='flight_game',
        user='root',
        password='Nevermindme',
        autocommit=True)
    return yhteys


def tulosta_tietkan(koodi, yhteys):
    sql = "select airport.name, airport.iso_region from airport"
    sql += " where airport.ident = '" + koodi + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"Lentoasema: {rivi[0]}")
            print(f"sijaintikunta: {rivi[1]}")
    else:
        print("Koodia ei löytynyt")
    return


koodi = input("Syötä IOCA-koodi: ")
tulosta_tietkan(koodi, avaa_tietokanta())
