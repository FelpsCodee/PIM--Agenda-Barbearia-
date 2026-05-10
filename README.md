# 💈 BarberShop API & Web

Sistema de agendamento funcional para barbearias desenvolvido com **FastAPI** (Backend), **SQLite** (Banco de Dados) e integração via frontend simples.

## 🛠️ Tecnologias e Dependências
- **Backend:** FastAPI & Uvicorn
- **Banco de Dados:** SQLite3
- **Validação:** Pydantic
- **Frontend:** HTML, CSS e JavaScript (Fetch API)

---

## ️ Estrutura e Explicação do Código

O projeto está dividido em módulos (arquivos) para facilitar a manutenção e escalabilidade:

- **`main.py`**: É o coração da aplicação FastAPI. Contém as rotas da API:
  - `GET /`: Serve a página inicial (`index.html`).
  - `GET /servicos`: Consulta o banco de dados e retorna a lista de serviços oferecidos.
  - `GET /horarios-disponiveis`: Recebe uma data e calcula os horários livres, filtrando os que já possuem agendamentos no banco de dados.
  - `POST /agendar`: Recebe os dados do formulário, valida se o cliente já existe pelo e-mail (cria um novo se necessário), verifica se o horário continua livre (evitando duplicidade) e salva o agendamento no banco.

- **`models.py`**: Define as regras de validação dos dados de entrada e saída usando **Pydantic**. 
  - Garante que e-mails enviados pelo frontend sejam válidos (graças ao `EmailStr`), e que as tipagens (como `id_servico` obrigatoriamente sendo um inteiro) sejam respeitadas antes de o FastAPI processar a requisição.

- **`database.py`**: Script de configuração inicial do banco. Quando executado, ele cria o arquivo `barbearia.db` (SQLite) e estrutura as tabelas relacionais `clientes`, `servicos` e `agendamentos`. Por fim, faz um "seed", inserindo os serviços iniciais da barbearia automaticamente se a tabela estiver vazia.

- **`querys.py`**: Um script auxiliar backend desenvolvido para testar a inserção de novos serviços avulsos de forma manual via código.

---

## 🚀 Como Rodar o Projeto

### 1. Preparar o Ambiente Virtual (venv)
É altamente recomendado rodar o projeto dentro de um ambiente isolado:
```bash
# Criar a venv
python -m venv venv

# Ativar a venv (Windows CMD)
venv\Scripts\activate

# Ativar a venv (Windows PowerShell)
.\venv\Scripts\activate
```

### 2. Instalar as Dependências
Com a `venv` ativada, instale as bibliotecas que estão mapeadas no projeto (incluindo dependências de validação):
```bash
pip install -r requirements.txt
pip install email-validator
```

### 3. Iniciar e Popular o Banco de Dados
Gere o banco SQLite e as tabelas rodando o arquivo de configuração de dados pela primeira vez:
```bash
python database.py
```

### 4. Rodar o Servidor Backend
Suba a API com o Uvicorn na porta 8000:
```bash
uvicorn main:app --reload
```

### 5. Acessar a Aplicação
- **Sistema Web (Frontend):** Abra seu navegador e acesse `http://127.0.0.1:8000`
- **Documentação da API (Swagger):** Acesse `http://127.0.0.1:8000/docs` para visualizar e testar os endpoints diretamente pelo navegador.
