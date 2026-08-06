import sqlite3
from datetime import datetime

NOME_BANCO = "vagas.db"

def conectar():
    return sqlite3.connect(NOME_BANCO)

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vagas (
            id INTEGER PRIMARY KEY,
            titulo TEXT,
            empresa TEXT,
            cidade TEXT,
            estado TEXT,
            url TEXT,
            nivel TEXT,
            data_publicacao TEXT,
            data_salvo TEXT
        )
    """)

    conn.commit()
    conn.close()

def salvar_vaga(vaga):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR IGNORE INTO vagas (
            id, titulo, empresa, cidade, estado,
            url, nivel, data_publicacao, data_salvo
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        vaga["id"],
        vaga["titulo"],
        vaga["empresa"],
        vaga["cidade"],
        vaga["estado"],
        vaga["url"],
        vaga["nivel"],
        vaga["data_publicacao"],
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    nova = cursor.rowcount > 0
    conn.commit()
    conn.close()
    return nova

def buscar_todas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM vagas ORDER BY data_salvo DESC")
    vagas = cursor.fetchall()
    conn.close()
    return vagas