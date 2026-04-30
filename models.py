from pydantic import BaseModel,EmailStr
from typing import Optional
from datetime import date

class ClienteBase(BaseModel):
    nome: str
    email: EmailStr
    telefone: str

class ServicoResponse(BaseModel):
    id_servico: int
    nome: str
    descricao: Optional[str] = None
    preco: float

class AgendamentoRequest(BaseModel):
    nome_cliente: str
    email_cliente: EmailStr
    telefone_cliente: str
    id_servico: int
    data_agendamento: str
    
  