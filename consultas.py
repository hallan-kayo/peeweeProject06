from esquema import *

# 1 - Liste todo o histórico de preços (valor, data) do produto "Caneta Bic esferográfica azul".
q1 = Historico_precos.select(Historico_precos.valor, Historico_precos.data).where(
    Historico_precos.produto == Produtos.select(Produtos.id).where(Produtos.descricao == 'Caneta Bic esferográfica azul').get()
)

for row in q1:
    print(row.valor, '  ', row.data)

#2 - Liste descrição e preço de todos os produtos da categoria "Papelaria", ordenados no menor para o maior preço.
q2 = Produtos.select(Produtos.descricao, Produtos.valor).join(Categoria).where(
    Produtos.categoria == Categoria.select(Categoria.id).where(Categoria.descricao == 'Papelaria').get()
).order_by(Produtos.valor)

for row in q2:
    print( 'Produto: ', row.descricao, ', Valor: ', row.valor)

# 3 - Recupere os nomes dos clientes que fizeram ao menos uma compra com valor superior a 
# R$ 5.000,00 no mês de setembro/2022. Exiba-os em ordem alfabética.
q3 = Cliente.select(Cliente.nome).join(Vendas).where(
    (Vendas.valor_total > 5000) & (Vendas.data.between('2022-9-1', '2022-10-1'))
).order_by(Cliente.nome).distinct()

for row in q3.objects():
    print(row.nome)