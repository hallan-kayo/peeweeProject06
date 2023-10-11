from esquema import *
from datetime import datetime
lista_categorias = [
    {'descricao' : 'Papelaria'},
    {'descricao' : 'Tecnologia'},
    {'descricao' : 'Alimento'},
    {'descricao' : 'Móveis'},
    {'descricao' : 'Eletrodomésticos'},
    {'descricao' : 'Diversos'}
]

# Categoria.insert_many(lista_categorias).execute()


cliente1 = Cliente(
    nome = "João da Silva", 
    endereco = "Rua A, 123", 
    data_registro = datetime(2021, 12, 30,7)
)

cliente2 = Cliente(
    nome = "Maria Souza", 
    endereco = "Avenida B, 456", 
    data_registro = datetime(2022,10,8,7)
)

cliente3 = Cliente(
    nome = "Carlos Santos", 
    endereco = "Rua C, 789", 
    data_registro = datetime(2022,2,7,7)
)

cliente4 = Cliente(
    nome = "Ana Oliveira", 
    endereco = "Avenida D, 1011", 
    data_registro = datetime(2023,4,6,7)
)

cliente5 = Cliente(
    nome = "Pedro Pereira",
    endereco = "Rua E, 1314", 
    data_registro = datetime(2019,6,17,7)
)

# cliente1.save()
# cliente2.save()
# cliente3.save()
# cliente4.save()
# cliente5.save()


caneta = Produtos(
    descricao = 'Caneta Bic esferográfica azul', 
    categoria = Categoria.select().where(Categoria.descricao == 'Papelaria'), 
    valor = 2.5
)
# caneta.save()

notebook = Produtos(
    descricao = 'Notebook', 
    categoria = Categoria.select().where(Categoria.descricao == 'Tecnologia'), 
    valor = 2499.99
)
# notebook.save()

mesa = Produtos(
    descricao = 'Mesa', 
    categoria = Categoria.select().where(Categoria.delete == 'Móveis'), 
    valor = 549.95
)
# mesa.save()

monitor = Produtos(
    descricao = 'Monitor', 
    categoria = Categoria.select().where(Categoria.descricao == 'Tecnologia'),
    valor = 700
)
# monitor.save()

ar = Produtos(
    descricao = 'Ar Condicionado', 
    categoria = Categoria.select().where(Categoria.descricao == 'Eletrodomésticos'),
    valor = 2999
)
# ar.save()
caderno = Produtos(
    descricao = 'Caderno', 
    categoria = Categoria.select().where(Categoria.descricao == 'Papelaria'),
    valor = 22
)
# caderno.save()

livro = Produtos(
    descricao = 'Livro', 
    categoria = Categoria.select().where(Categoria.descricao == 'Papelaria'), 
    valor = 250
)
# livro.save()

borracha = Produtos(
    descricao = 'Borracha', 
    categoria = Categoria.select().where(Categoria.descricao == 'Papelaria'), 
    valor = 1.5
)
# borracha.save()

# def preencher_venda(nome_cliente, nome_produto, quantidade,data):
#     id_cliente = Cliente.select(Cliente.id).where(Cliente.nome == nome_cliente)
#     id_produto = Produtos.select(Produtos.id).where(Produtos.descricao == nome_produto)
#     valor_produto = Produtos.select(Produtos.valor).where(Produtos.id == id_produto)
#     data_venda = datetime(data)
#     info_venda = Vendas(id_produto,id_cliente,data_venda,quantidade,valor_produto,(valor_produto*quantidade))
#     return info_venda

# def cadastrar_venda(venda):
#     venda = preencher_venda(venda.nome_cliente, venda.nome_produto, venda.quantidade)
#     venda.save()

# venda1 = Vendas('João da Silva', 'Caneta Bic esferográfica azul', 5, datetime(2023,6,17,10,20))
# # venda1.save()
# venda2 = Vendas('João da Silva', 'Notebook', 1, datetime(2023,6,17,10,20))
# # venda2.save()
# venda3 = Vendas('Carlos Santos', 'Caderno', 2, datetime(2021,10,7,15,10))
# # venda3.save()
# venda4 = Vendas('Ana Oliveira', 'Ar Condicionado', 3, datetime(2022,9,17,12,20))
# # venda4.save()
# venda5 = Vendas('Pedro Pereira', 'Notebook', 10, datetime(2022,9,11,9,27))
# # venda5.save()
# venda6 = Vendas('Maria de Souza', 'mesa', 5, datetime(2023,6,1,17,20))
# # venda6.save()
# venda7 = Vendas('Ana Oliveira', 'Borracha', 100, datetime(2022,9,3,7,0))
# # venda7.save()
# venda8 = Vendas('Ana Oliviera', 'Livro', 2, datetime(2022,9,3,7,0))
# # venda8.save()
# venda9 = Vendas('Carlos Santos', 'Ar Condicionado', 15, datetime(2022,9,12,16,50))
# # venda9.save()
# venda10 = Vendas('Maria de Souza', 'Caneta Bic esferográfica azul', 10, datetime(2023,4,17,10,20))
# # venda10.save()