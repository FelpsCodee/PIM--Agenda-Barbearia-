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
    return {"voce esta na home": "Bem-vindo à API da Barbearia!"}

@app.get("/servicos")
def listar_servicos():
    conn = get_db_connection()
    cursor = conn.cursor()
    servicos = cursor.execute('SELECT * FROM servicos').fetchall()
    conn.close()
    return {"serviços": servicos}   

@app.post("/agendar")
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
    return {
    "status": "sucesso",
    "message": "Agendamento criado com sucesso!",
    "detalhes": {
        "id_cliente": agendamento.id_cliente,
        "id_servico": agendamento.id_servico,
        "data": agendamento.data_agendamento
    }
}
    
@app.get("/clientes")
def listar_clientes():
    conn = get_db_connection()
    cursor = conn.cursor()
    clientes = cursor.execute('SELECT * FROM clientes').fetchall()
    conn.close()
    return {"clientes": clientes}

@app.get("/horarios-disponiveis")
def listar_horarios_disponiveis(data:str):
     
    horarios_cortes = ["09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00"]
    conn = get_db_connection()
    cursor = conn.cursor()
    agendados = cursor.execute("SELECT data_agendamento FROM agendamentos WHERE data_agendamento LIKE ?", (f"{data}%",) ).fetchall()
    conn.close()
    
    horas_ocupadas = [row['data_agendamento'].split(" ")[1] for row in agendados]
    disponiveis = [h for h in horarios_cortes if h not in horas_ocupadas]
    return {"data": data, "horarios_livres": disponiveis}


@app.get("/servico/{id_servico}")
def obter_servico(id_servico: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    servico = cursor.execute("SELECT * FROM servicos WHERE id_servico = ?", (id_servico,)).fetchone()
    conn.close()
    
    if servico is None:
        raise HTTPException(status_code=404, detail="Serviço não encontrado.")
    
    return ServicoResponse(
        id_servico=servico['id_servico'],
        nome=servico['nome'],
        descricao=servico['descricao'],
        preco=servico['preco']
    )
    
@app.get("/meus-agendamentos/{id_cliente}")
def listar_agendamentos_cliente(id_cliente: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Tecnicamente: Selecionamos colunas de 'a' (agendamentos) e 's' (servicos)
    query = """
        SELECT a.data_agendamento, s.nome, s.preco
        FROM agendamentos AS a
        INNER JOIN servicos AS s ON a.id_servico = s.id_servico
        WHERE a.id_cliente = ?
        ORDER BY a.data_agendamento DESC
    """
    
    agendamentos = cursor.execute(query, (id_cliente,)).fetchall()
    conn.close()
    
    if not agendamentos:
        return {"mensagem": "Nenhum agendamento encontrado.", "id_cliente": id_cliente}

    return {
        "id_cliente": id_cliente,
        "agendamentos": [dict(row) for row in agendamentos]
    }