# peeweeProject06
projeto de Banco de Dados para manipulação de um banco de dados postgres através do python com pewee e psycopg

# Código para criar gatilho de inserção da tabela de histórico_precos
Esse trigger é ativado sempre que um novo produto é inserido na tabela Produtos e também sempre que o valor do produto
é alterado na respectiva tabela.

```
CREATE OR REPLACE FUNCTION insere_historico_preco()
RETURNS trigger AS 
$$
BEGIN
	IF NEW.valor <> OLD.valor OR OLD.id IS NULL THEN
        INSERT INTO historico_precos (produto_id, valor, data)
        VALUES (NEW.id, NEW.valor, Now());
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER insere_historico_preco_trigger
AFTER INSERT OR UPDATE ON produtos
FOR EACH ROW
execute function insere_historico_preco();
```