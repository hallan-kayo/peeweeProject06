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
    categoria = Categoria.select().where(Categoria.descricao == 'Móveis'), 
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

def cadastrar_venda(nome_cliente, nome_produto, quantidade_itens, data_venda):
    venda = Vendas(
        cliente = Cliente.select().where(Cliente.nome == nome_cliente),
        produto = Produtos.select().where(Produtos.descricao == nome_produto),
        quantidade = quantidade_itens,
        data = data_venda,
        valor_unitario = Produtos.select(Produtos.valor).where(
            Produtos.id == Produtos.select().where(Produtos.descricao == nome_produto)),
        valor_total = (Produtos.select().where(
            Produtos.id == Produtos.select().where(
                Produtos.descricao == 'Notebook').get()).get().valor*quantidade_itens)
    )
    venda.save()


# cadastrar_venda('João da Silva', 'Caneta Bic esferográfica azul', 5, datetime(2023,6,17,10,20))
# cadastrar_venda('João da Silva', 'Notebook', 1, datetime(2023,6,17,10,20))
# cadastrar_venda('Carlos Santos', 'Caderno', 2, datetime(2021,10,7,15,10))
# cadastrar_venda('Ana Oliveira', 'Ar Condicionado', 3, datetime(2022,9,17,12,20))
# cadastrar_venda('Pedro Pereira', 'Notebook', 10, datetime(2022,9,11,9,27))
# cadastrar_venda('Maria Souza', 'Mesa', 5, datetime(2023,6,1,17,20))
# cadastrar_venda('Ana Oliveira', 'Borracha', 100, datetime(2022,9,3,7,0))
# cadastrar_venda('Ana Oliveira', 'Livro', 2, datetime(2022,9,3,7,0))
# cadastrar_venda('Carlos Santos', 'Ar Condicionado', 15, datetime(2022,9,12,16,50))
# cadastrar_venda('Maria Souza', 'Caneta Bic esferográfica azul', 10, datetime(2023,4,17,10,20))

# ----------------------------------------------------------------------------------------------------------

# q1 = Produtos.select(Produtos.valor).where(Produtos.descricao == "Notebook").get()
# print(q1.valor)

# q1 = Produtos.select().where(
#     Produtos.id == Produtos.select().where(Produtos.descricao == 'Notebook').get()).get().valor
q2 = Produtos.select(Produtos.id).where(Produtos.descricao == 'Caneta Bic esferográfica azul').get().id
# print(q1)
# print(q2)

update1=Produtos.update({Produtos.valor:4}).where(Produtos.id == Produtos.select(Produtos.id).where(
    Produtos.descricao == 'Caneta Bic esferográfica azul'))
# update1.execute()

update2=Produtos.update({Produtos.valor:2}).where(Produtos.id == Produtos.select(Produtos.id).where(
    Produtos.descricao == 'Caneta Bic esferográfica azul'))
# update2.execute()

update3=Produtos.update({Produtos.valor:1.5}).where(Produtos.id == Produtos.select(Produtos.id).where(
    Produtos.descricao == 'Caneta Bic esferográfica azul'))
# update3.execute()