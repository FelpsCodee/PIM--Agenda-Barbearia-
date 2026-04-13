import sqlite3

def criar_banco_e_tabelas():
  
  try:
      conexao = sqlite3.connect('barbearia.db')
      print("Conexão com o banco de dados criada com sucesso!")
  except sqlite3.Error as e:
      print(f"Erro ao conectar ao banco de dados: {e}")
      return
    
  with conexao as conn:
      cursor = conexao.cursor()
      cursor.execute('''
          CREATE TABLE IF NOT EXISTS clientes (
              id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
              telefone TEXT NOT NULL,
              nome TEXT NOT NULL,
              email TEXT NOT NULL
          );
      ''')
      print("Tabela 'clientes' criada com sucesso!")
      
      cursor.execute('''
          CREATE TABLE IF NOT EXISTS servicos (
              id_servico INTEGER PRIMARY KEY AUTOINCREMENT,
              nome TEXT NOT NULL,
              descricao TEXT,
              preco REAL NOT NULL
          );
      ''')
      print("Tabela 'servicos' criada com sucesso!")
      
      cursor.execute('''
          CREATE TABLE IF NOT EXISTS agendamentos (
              id_agendamento INTEGER PRIMARY KEY AUTOINCREMENT,
              id_cliente INTEGER NOT NULL,
              data_agendamento TEXT NOT NULL,
              id_servico TEXT NOT NULL,
              FOREIGN KEY (id_cliente) REFERENCES clientes (id_cliente),
              FOREIGN KEY (id_servico) REFERENCES servicos (id_servico)
          );
      ''')
      print("Tabela 'agendamentos' criada com sucesso!")
      
      #AQUI VAMOS INSERIR DADOS DE TESTE PARA VER SE AS TABELAS ESTÃO FUNCIONANDO CORRETAMENTE
      
      cursor.execute("INSERT INTO clientes (nome, telefone, email) VALUES (?, ?, ?)", 
                       ('José Almeida', '11999999999', 'felipe@email.com'))
      cursor.execute("INSERT INTO clientes (nome, telefone, email) VALUES (?, ?, ?)", 
                       ('Ana Silva', '11888888888', 'ana@email.com'))


      cursor.execute("INSERT INTO servicos (nome, descricao, preco) VALUES (?, ?, ?)", 
                       ('Corte Degradê', 'Corte moderno com sombreado', 45.00))
      cursor.execute("INSERT INTO servicos (nome, descricao, preco) VALUES (?, ?, ?)", 
                       ('Barba Completa', 'Aparagem e hidratação', 30.00))

      cursor.execute("INSERT INTO agendamentos (id_cliente, id_servico, data_agendamento) VALUES (?, ?, ?)", 
                       (1, 1, '2026-04-15 14:00'))
        
      cursor.execute("INSERT INTO agendamentos (id_cliente, id_servico, data_agendamento) VALUES (?, ?, ?)", 
                       (2, 2, '2026-04-15 15:30'))

      print("Dados populados com sucesso para testes!")
      
if __name__ == "__main__":
    criar_banco_e_tabelas()
