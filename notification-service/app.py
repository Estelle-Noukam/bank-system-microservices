from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/notify')
def notify():
    return jsonify({
        "message": "Notification envoyée avec succès"
    })

app.run(host='0.0.0.0', port=5004)
