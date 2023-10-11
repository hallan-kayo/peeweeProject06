from peewee import (PostgresqlDatabase, Model, TextField, DateField, ForeignKeyField, FloatField, DateTimeField, IntegerField)

bd = PostgresqlDatabase('Lista06', port = 5432, user = 'postgres', password = '121427')

class BaseModel(Model):
    class Meta():
        database = bd

class Catetoria(BaseModel):
    descricao = TextField()

class Cliente(BaseModel):
    nome = TextField()
    endereco = TextField()
    data_registro = DateField()

class Produtos(BaseModel):
    descricao = TextField()
    id_categoria = ForeignKeyField(Catetoria, backref='produtos')
    valor = FloatField()

class Historico_precos(BaseModel):
    id_produto = ForeignKeyField(Produtos, backref= 'historico_precos')
    valor = FloatField()
    data = DateTimeField()

class Vendas(BaseModel):
    id_produto = ForeignKeyField(Produtos, backref='vendas')
    id_cliente = ForeignKeyField(Cliente, backref='vendas')
    quantidade = IntegerField()
    valor_unitario = FloatField()
    valor_total = FloatField()

lista_tables = [Catetoria, Cliente, Produtos, Historico_precos, Vendas]

# bd.connect()
# bd.create_tables(lista_tables)
# bd.close()