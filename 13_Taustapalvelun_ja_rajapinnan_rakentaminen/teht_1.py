from flask import Flask, request
import json

app = Flask(__name__)


def onko_alkuluku(luku):
    for x in range(2, int(luku)):
        if luku % x == 0:
            return False
    return True


@app.route('/alkuluku')
def alkuluku():
    args = request.args
    luku = float(args.get("luku"))
    is_prime = onko_alkuluku(luku)

    vastaus = {
        "Number": luku,
        "isPrime": is_prime,
    }

    json_data = json.dumps(vastaus, default=lambda o: o.__dict__, indent=4)
    return vastaus


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
