import sqlite3

class Banco_projeto:
    def __init__(self, nome_banco):
        self.nome_banco = nome_banco

        try:
            self.conexao = sqlite3.connect(self.nome_banco)
            self.cursor = self.conexao.cursor()
        except sqlite3.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")

    def criar_tabela(self, nome_tabela, colunas: str):
        try:
            self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {nome_tabela} ({colunas})")
            self.conexao.commit()
            print(f"Tabela '{nome_tabela}' criada com sucesso!")
            
        except sqlite3.Error as e:
            print(f"Erro ao criar tabela: {e}")

    def criar_produto(self, nome_tabela, colunas, valores, produto_existente):
        try:
            self.cursor.execute(f"INSERT INTO {nome_tabela} ({colunas}) VALUES ({valores})")
            self.conexao.commit()
            print(f"Produto criado com sucesso!")
                
        except sqlite3.Error as e:
            print(f"Erro ao criar produto: {e}")       

    def consultar_nome(self, nome_tabela, nome):
        cursor = self.conexao.cursor()
        cursor.execute(
            f"SELECT nome FROM {nome_tabela} WHERE nome= '{nome}'")
        produto_existente = cursor.fetchone()

        return produto_existente

    def consultar_id(self, nome_tabela, id):
        cursor = self.conexao.cursor()
        cursor.execute(
            f"SELECT id FROM {nome_tabela} WHERE id= {id}")
        produto_existente = cursor.fetchone()

        return produto_existente
    
    def deletar_produto(self, nome_tabela, id):
        try:
            self.cursor.execute(f"DELETE FROM {nome_tabela} WHERE id = {id}")
            self.conexao.commit()
            print(f"Produto deletado com sucesso!")

        except sqlite3.Error as e:
            print(f"Erro ao deletar produto: {e}") 

    def atualizar_produto(self, nome_tabela, item_atualizar, novo_valor, id_produto):
        try:
            self.cursor.execute(f"UPDATE {nome_tabela} SET {item_atualizar} = ? WHERE id = ?", (novo_valor, id_produto))
            self.conexao.commit()
            print(f"Produto deletado com sucesso!")

        except sqlite3.Error as e:
            print(f"Erro ao deletar produto: {e}")             

    def vender_produto(self, nome_tabela, id_produto, qtd_venda):
        cursor = self.conexao.cursor()
        cursor.execute(
            f"SELECT qtd_estoque FROM {nome_tabela} WHERE id= {id_produto}")
        resultado = cursor.fetchone()
        valor_inteiro = int(resultado[0])
        
        if qtd_venda <= valor_inteiro:
            try:
                self.cursor.execute(f"UPDATE {nome_tabela} SET qtd_estoque = qtd_estoque - {qtd_venda} WHERE id = {id_produto}")
                self.conexao.commit()
                print(f"Produto vendido com sucesso!")

            except sqlite3.Error as e:
                print(f"Erro ao vender produto: {e}") 
            
        else:
            print("Valor de venda superior ao estoque atual.")

    def salvar_alterações(self):
        self.conexao.commit()

    def encerrar_conexao(self):
        self.conexao.close()