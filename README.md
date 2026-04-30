# 💈 BarberShop API & Web

Sistema de agendamento funcional desenvolvido com **FastAPI** e **SQLite**.

## 🛠️ Tecnologias e Dependências
*   **Backend:** FastAPI & Uvicorn
*   **Banco de Dados:** SQLite3
*   **Validação:** Pydantic
*   **Frontend:** JavaScript Fetch API

---

## 🚀 Como Inicializar o Projeto

### 1. Preparar o Ambiente
Instale as dependências necessárias:

pip install -r requirements.txt

### 2. Iniciar o banco de dados
 python database.py

 ### 3. Rodar o servidor Backend
  uvicorn main:app --reload

***📝 Funcionalidades Técnicas***
Endpoint de Serviços (GET /servicos): Retorna a lista de procedimentos e preços direto do banco.

Lógica de Horários Disponíveis: O sistema verifica agendamentos existentes e filtra apenas as horas vagas entre 09:00 e 17:00.

Persistência de Clientes: Realiza a verificação por e-mail; se o cliente for novo, o sistema executa o INSERT automaticamente antes de gerar o agendamento.

Integração WhatsApp: Gera um link dinâmico no frontend para confirmação imediata via API do WhatsApp
