from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/balance')
def balance():
    return jsonify({
        "account_id": "ACC-1001",
        "balance": 1500
    })

app.run(host='0.0.0.0', port=5002)
