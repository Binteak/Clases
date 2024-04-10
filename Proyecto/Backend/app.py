from flask import Flask, render_template, send_from_directory, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Ruta para servir archivos estáticos (HTML, CSS, JS)
@app.route('/')
def index():
    return send_from_directory('Frontend', 'index.html')

# Ruta para servir archivos CSS
@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('Frontend', filename)


# Ruta para devolver datos JSON
@app.route('/data')
def get_data():
    data = {
        'message': 'Hola desde el backend',
        'value': 42
    }
    print('Datos enviados:', data)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)


