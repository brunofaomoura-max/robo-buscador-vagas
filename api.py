from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__)
CORS(app, origins=["*"])

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'vagas.db')

@app.route('/api/vagas', methods=['GET'])
def get_vagas():
    try:
        if not os.path.exists(DB_PATH):
            return jsonify({'error': f'Banco de dados não encontrado em: {DB_PATH}'}), 404
            
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM vagas')
        vagas = cursor.fetchall()
        conn.close()
        
        return jsonify([dict(vaga) for vaga in vagas])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')