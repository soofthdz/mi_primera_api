from flask import Flask, jsonify, request

app = Flask(__name__)

## simular datos
clientes = {
    101: {'id': 101, 'nombre': 'Carlos Ramos', 'saldo': 150.50}, 
    102: {'id': 102, 'nombre': 'Glinda Flores', 'saldo': 320.00}
    }

@app.get("/")
def inicio():
    return jsonify(
        {
            'mensaje': 'Bienvendios a la API clientes',
            'version': 1.0,
            'endpoints': ["/clientes", "/clientes/<id>"]
        }
    )
    
@app.get("/clientes")
def obtener_clientes():
    return jsonify(list(clientes.values()))


@app.get("/clientes/<int:id>")
def obtener_cliente():
    cliente = clientes.get(id)
    if cliente:
        return jsonify(cliente)
    return jsonify({'error': 'Cliente no encontrado'}), 404

if __name__ == "__main__":
    app.run(debug=True)