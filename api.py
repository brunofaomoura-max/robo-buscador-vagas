from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

@app.route('/api/vagas', methods=['GET'])
def get_vagas():
    try:
        conn = sqlite3.connect('vagas.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM vagas')
        vagas = cursor.fetchall()
        conn.close()
        
        return jsonify([dict(vaga) for vaga in vagas])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)