💈 BarberShop API & Web
Este é um sistema de agendamento para barbearias desenvolvido com FastAPI no backend e uma interface Web (HTML/JS) simples e funcional. O projeto permite que clientes escolham serviços, verifiquem horários disponíveis e confirmem agendamentos com integração para redirecionamento via WhatsApp.

🚀 Tecnologias Utilizadas

Backend: FastAPI (Python 3.12+)   


Banco de Dados: SQLite   

Frontend: HTML5, CSS3 e JavaScript Vanilla


Validação de Dados: Pydantic   

📂 Estrutura do Projeto
main.py: Ponto de entrada da aplicação com as rotas da API.

database.py: Script para criação do banco de dados e tabelas iniciais.

models.py: Definições dos esquemas de dados (Pydantic).

index.html: Interface do usuário para realização dos agendamentos.


barbearia.db: Arquivo do banco de dados SQLite.  

🛠️ Como Executar
1. Configurar o ambiente
Certifique-se de ter o Python instalado. Recomenda-se o uso de um ambiente virtual:

Bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
.\venv\Scripts\activate  # Windows
2. Instalar dependências
Instale os pacotes necessários listados no requirements.txt:  

Bash
pip install -r requirements.txt
3. Inicializar o Banco de Dados
Execute o script para criar o arquivo .db e popular os serviços iniciais (Corte Degradê e Barba Completa):

Bash
python database.py
4. Rodar o servidor
Inicie a aplicação com o Uvicorn:  

Bash
uvicorn main:app --reload
Acesse o sistema em: http://127.0.0.1:8000.

📝 Funcionalidades
Listagem de Serviços: Busca automática dos serviços cadastrados no banco.

Verificação de Horários: O sistema filtra horários das 09:00 às 17:00, removendo os que já possuem agendamento para a data selecionada.

Cadastro Automático: Se o e-mail do cliente não existir na base, o sistema o cadastra automaticamente antes de vincular o agendamento.

Notificação: Após o sucesso, o usuário é redirecionado para o WhatsApp com uma mensagem pronta contendo os detalhes do corte.

📊 Estrutura de Dados
O banco de dados conta com as seguintes tabelas:  

clientes: Armazena nome, telefone e e-mail (único).

servicos: Contém o nome, descrição e preço dos atendimentos.

agendamentos: Vincula clientes e serviços a uma data/hora específica.

Desenvolvido como projeto acadêmico para gestão de barbearias.