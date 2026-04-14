from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/pay')
def pay():
    auth_response = requests.get('http://auth-service:5001/auth').json()
    account_response = requests.get('http://account-service:5002/balance').json()
    notification_response = requests.get('http://notification-service:5004/notify').json()

    return jsonify({
        "status": "Paiement traité avec succès",
        "auth": auth_response,
        "account": account_response,
        "notification": notification_response
    })

app.run(host='0.0.0.0', port=5003)
