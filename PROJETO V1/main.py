from Classes.Bd_poo import Banco_projeto

banco = Banco_projeto("projeto.sqlite")
colunas = "nome, valor, qtd_estoque"
nome_tabela = "Estoque"

banco.criar_tabela(nome_tabela, "id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, valor FLOAT, qtd_estoque INT")

# TABELA DE OPÇÃO
decisao = 12

while decisao != 0: 
    decisao = int(input("""
    --------MENU--------
    1- Criar produto
    2- Vender produto
    3- Atualizar produto
    4- Deletar produto
    0- Sair
    
Digite a opção escolhida: """))

# CRIAR PRODUTO
    if decisao == 1:
        nome_produto = input("Digite o nome do produto: ")
        consulta_nome = banco.consultar_nome(nome_tabela, nome_produto)

        if consulta_nome is None:
            valor_produto = float(input(f"Digite o valor de {nome_produto}: "))
            estoque_produto = int(input(f"Informe o número de {nome_produto} em estoque: "))

            novo_valor = f"'{nome_produto}', {valor_produto}, {estoque_produto}"
            banco.criar_produto(nome_tabela, colunas, novo_valor, consulta_nome)
        
        else:
            print("Produto não criado, este produto já se encontra cadastrado.")

# VENDER PRODUTO
    elif decisao == 2:
        id_produto = input("Digite o id do produto que foi vendido: ")
        consulta_id = banco.consultar_id(nome_tabela, id_produto)

        if consulta_id is not None:
            qtd_venda = int(input(f"Digite a quantidade de produtos vendidos: "))

            banco.vender_produto(nome_tabela, id_produto, qtd_venda)
        else:
            print("Serviço não realizado, ID não identificado em nossa tabela.")

# ATUALIZAR PRODUTO
    elif decisao == 3:
        id_produto = input("Digite o ID do produto que deseja atualizar: ")
        decisao_atualizar = 9
        consulta_id = banco.consultar_id(nome_tabela, id_produto)

        if consulta_id is not None:
            while decisao_atualizar != 0:
                decisao_atualizar = int(input("""
                --------MENU--------
                1- NOME
                2- VALOR
                3- QTD_ESTOQUE
                0- RETORNAR AO MENU INICIAL.
        
                Digite a opção escolhida: """))

                if decisao_atualizar == 1:
                    nome_produto = input("Informe para qual nome deseja alterar: ")
                    item_atualizar = 'nome'

                    banco.atualizar_produto(nome_tabela, item_atualizar, nome_produto, id_produto)
                    decisao_atualizar == 0

                elif decisao_atualizar == 2:
                    valor_produto = float(input("Informe para qual preço deseja alterar: "))
                    item_atualizar = 'valor'

                    banco.atualizar_produto(nome_tabela, item_atualizar, valor_produto, id_produto)
                    decisao_atualizar == 0

                elif decisao_atualizar == 3:
                    qtd_estoque = int(input("Informe para qual quantidade de estoque deseja alterar: "))
                    item_atualizar = 'qtd_estoque'

                    banco.atualizar_produto(nome_tabela, item_atualizar, qtd_estoque, id_produto)
                    decisao_atualizar == 0
            else:
                print("Opção inválida!")
        else:
            print("Serviço não realizado, ID não identificado em nossa tabela.")

# DELETAR PRODUTO
    elif decisao == 4:
        id_produto = input("Digite o ID do produto a ser deletado: ")
        consulta_id = banco.consultar_id(nome_tabela, id_produto)

        if consulta_id is not None:
            banco.deletar_produto(nome_tabela, id_produto)
        else:
            print("Serviço não realizado, ID não identificado em nossa tabela.")

# SAIR PROGRAMA
    elif decisao == 0:
        print("Encerrando o programa...")

    else:
        print("Opção inválida!")

