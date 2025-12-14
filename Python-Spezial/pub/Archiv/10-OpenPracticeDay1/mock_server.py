from flask import Flask, jsonify

app = Flask(__name__)

# Statische "Datenbank"
SCORES = {
    "CUST-001": {"score": 750, "rating": "A", "limit": 50000},
    "CUST-002": {"score": 620, "rating": "B", "limit": 10000},
    "CUST-999": {"score": 300, "rating": "D", "limit": 0}
}

@app.route('/credit-score/<customer_id>', methods=['GET'])
def get_score(customer_id):
    data = SCORES.get(customer_id)
    if data:
        return jsonify(data), 200
    else:
        return jsonify({"error": "Customer not found"}), 404

if __name__ == '__main__':
    print("Starte Credit-Score API auf Port 5000...")
    app.run(port=5000)