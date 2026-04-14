from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/auth')
def auth():
    return jsonify({
        "user": "estelle",
        "authenticated": True
    })

app.run(host='0.0.0.0', port=5001)
