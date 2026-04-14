from pydantic import BaseModel
from typing import List, Optional

class Cliente(BaseModel):
    id_cliente: int
    nome: str
    email: str
    telefone: str

class ServicoResponse(BaseModel):
    id_servico: int
    nome: str
    descricao: Optional[str] = None
    preco: float
    
class AgendamentoRequest(BaseModel):
    id_cliente: int
    id_servico: int
    data_agendamento: str
    
  