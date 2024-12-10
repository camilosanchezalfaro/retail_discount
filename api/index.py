from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/index', methods=['GET'])
def index():
    return jsonify({
        "message": "API funcionando",
        "descuentos": [
            {"nombre": "Producto 1", "descuento": 30, "link": "https://www.ejemplo.com/producto1"},
            {"nombre": "Producto 2", "descuento": 50, "link": "https://www.ejemplo.com/producto2"}
        ]
    })

if __name__ == '__main__':
    app.run()

