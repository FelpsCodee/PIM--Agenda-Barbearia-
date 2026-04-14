from fastapi import FastAPI, HTTPException
import sqlite3
from models import AgendamentoRequest, ServicoResponse, Cliente


app = FastAPI()

def get_db_connection():
    conn = sqlite3.connect('barbearia.db')
    conn.row_factory = sqlite3.Row 
    return conn

@app.get("/")
def home():
    return {"voce esta na home": "Bem vindo a Barbearia, acesse a rota /servicos para ver os serviços disponíveis e a rota /agendar para criar um agendamento!\n Exemplo de requisição para criar um agendamento: \n{\n  \"id_cliente\": 1,\n  \"id_servico\": 1,\n  \"data_agendamento\": \"2026-04-15 14:00\"\n}"}

@app.get("/servicos")
def listar_servicos():
    conn = get_db_connection()
    cursor = conn.cursor()
    servicos = cursor.execute('SELECT * FROM servicos').fetchall()
    conn.close()
    return {servicos}   

@app.get("/agendar")
async def criar_agendamento(agendamento: AgendamentoRequest):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        "SELECT id_agendamento FROM agendamentos WHERE data_agendamento = ?", 
        (agendamento.data_agendamento,)
    )
    resultado = cursor.fetchone()
    if resultado:
        conn.close()
        
        raise HTTPException(status_code=400, detail="Este horário já está preenchido.")
        
    cursor.execute(
            "INSERT INTO agendamentos (id_cliente, id_servico, data_agendamento) VALUES (?, ?, ?)",
            (agendamento.id_cliente, agendamento.id_servico, agendamento.data_agendamento)
        )
    conn.commit()
    return {"message": f"Agendamento criado com sucesso!\nid_cliente: {agendamento.id_cliente}\nid_servico: {agendamento.id_servico}\ndata_agendamento: {agendamento.data_agendamento}"}

