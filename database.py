import sqlite3

def criar_banco_e_tabelas():
    conexao = sqlite3.connect('barbearia.db')
    cursor = conexao.cursor()
    
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS clientes (
                id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                telefone TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            );
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS servicos (
                id_servico INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                descricao TEXT,
                preco REAL NOT NULL
            );
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS agendamentos (
                id_agendamento INTEGER PRIMARY KEY AUTOINCREMENT,
                id_cliente INTEGER NOT NULL,
                data_agendamento TEXT NOT NULL,
                id_servico INTEGER NOT NULL,
                FOREIGN KEY (id_cliente) REFERENCES clientes (id_cliente),
                FOREIGN KEY (id_servico) REFERENCES servicos (id_servico)
            );
        ''')
    except sqlite3.Error as e:
        print(f"Erro ao criar tabelas: {e}")
        conexao.close()
        return
    

    # Popular serviços base se a tabela estiver vazia
    cursor.execute("SELECT COUNT(*) FROM servicos")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO servicos (nome, descricao, preco) VALUES (?, ?, ?)", 
                       ('Corte Degradê', 'Corte moderno com sombreado', 45.00))
        cursor.execute("INSERT INTO servicos (nome, descricao, preco) VALUES (?, ?, ?)", 
                       ('Barba Completa', 'Aparagem e hidratação', 30.00))
    
    conexao.commit()
    conexao.close()

if __name__ == "__main__":
    criar_banco_e_tabelas()
    print("Banco de dados e tabelas criados com sucesso!")