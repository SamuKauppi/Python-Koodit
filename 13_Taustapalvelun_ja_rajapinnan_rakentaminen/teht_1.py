from flask import Flask, request, Response
import json

app = Flask(__name__)


def onko_alkuluku(luku):
    for x in range(2, int(luku)):
        if luku % x == 0:
            return False
    return True


@app.route('/alkuluku/<luku>')
def alkuluku(luku):
    try:
        is_prime = onko_alkuluku(float(luku))

        answer = {
            "Number": luku,
            "isPrime": is_prime,
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
