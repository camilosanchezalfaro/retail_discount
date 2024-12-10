from flask import Flask, jsonify
from scraper import get_discounts

app = Flask(__name__)

@app.route('/api/discounts/<int:discount_percentage>', methods=['GET'])
def discounts(discount_percentage):
    try:
        data = get_discounts(discount_percentage)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
