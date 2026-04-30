
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
from models import AgendamentoRequest 
from datetime import date
from fastapi.responses import FileResponse
from fastapi import FastAPI, HTTPException


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db_connection():
    conn = sqlite3.connect('barbearia.db')
    conn.row_factory = sqlite3.Row 
    return conn

@app.get("/")
async def read_index():
    return FileResponse('index.html')

@app.get("/servicos")
def listar_servicos():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        servicos = cursor.execute('SELECT * FROM servicos').fetchall()
        conn.close()
        return {"servicos": [dict(row) for row in servicos]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/horarios-disponiveis")
def listar_horarios_disponiveis(data: date):
    try:
        data_str = data.isoformat()
        horarios_padrao = ["09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00"]
        conn = get_db_connection()
        cursor = conn.cursor()
        agendados = cursor.execute("SELECT data_agendamento FROM agendamentos WHERE data_agendamento LIKE ?", (f"{data_str}%",)).fetchall()
        conn.close()
        horas_ocupadas = [row['data_agendamento'].split(" ")[1] for row in agendados if " " in row['data_agendamento']]
        disponiveis = [h for h in horarios_padrao if h not in horas_ocupadas]
        return {"data": data_str, "horarios_livres": disponiveis}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/agendar")
async def criar_agendamento(req: AgendamentoRequest):
    if len(req.data_agendamento.strip()) < 16:
        raise HTTPException(status_code=400, detail="Selecione data e horário.")
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id_cliente FROM clientes WHERE email = ?", (req.email_cliente,))
        cliente = cursor.fetchone()
        if not cliente:
            cursor.execute("INSERT INTO clientes (nome, email, telefone) VALUES (?, ?, ?)", (req.nome_cliente, req.email_cliente, req.telefone_cliente))
            id_cliente = cursor.lastrowid
        else:
            id_cliente = cliente['id_cliente']
        cursor.execute("SELECT id_agendamento FROM agendamentos WHERE data_agendamento = ?", (req.data_agendamento,))
        if cursor.fetchone():
            raise HTTPException(status_code=400, detail="Horário ocupado.")
        cursor.execute("INSERT INTO agendamentos (id_cliente, id_servico, data_agendamento) VALUES (?, ?, ?)", (id_cliente, req.id_servico, req.data_agendamento))
        conn.commit() 
        return {"status": "sucesso", "message": "Agendamento confirmado!"}
    except Exception as e:
        conn.rollback() 
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()