from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/student-details')
def student():
    return jsonify({
        "name": "Kethavath Murali",
        "roll": "2023BCD0008",
        "register": "2023BCD0008"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
