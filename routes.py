from flask import Flask, request
from data import count, calc

app = Flask("Study")


@app.route('/hello', methods=['GET'])
def hello():
    return "Hello wolrd"


@app.route('/date', methods=['POST'])
def find_date():
    body = request.get_json()

    if "date_start" in body and "date_end" in body:
        date_range = count(body["date_start"], body["date_end"])
        return {
            "interval": date_range, "status": 200
        }
    else:
        return {"mensagem": "Informe datas válidas", "status": 400}


@app.route('/calcICMS', methods=['POST'])
def calc_ICMS():
    body = request.get_json()

    if "value" in body and "debt" in body:
         result = calc(body["value"], body["debt"])
         return {
             "result_calc": result, "status": 200
         }
    else:
        return {"mensagem": "Há parametros faltando, verifique os valores enviados ", "status": 400}

app.run()
