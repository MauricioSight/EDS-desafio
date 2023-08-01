import psycopg2
import json

def main():
    # Simula operação POST de um API-REST
    simulate_post("../data/tb_procedimento.json")


def simulate_post(path):
    """
    Simula operação POST de um API-REST
    Arguments:
        path: Path do arquivo que seria o body da operação
    """
    with open(path, 'r') as file:
        reader = json.load(file)
        _, file_name = path.rsplit("tb_")
        table_name, _ = file_name.rsplit(".")
        post({ "table_name": table_name, "data": reader["data"], "layout": reader["layout"] })


def post(body):
    # Conecta com o banco de dados
    conn, cur = bd_connect()

    create_table(cur.execute, body["table_name"], body["layout"])
    insert_value(cur.execute, body["table_name"], body["data"])

    # Persiste as mudanças
    conn.commit()

    # Fecha a conexão
    cur.close()
    conn.close()


def bd_connect():
    """
    Conecta com o banco
    """
    conn = psycopg2.connect(database="stg_hospital", host="localhost", user="postgres", password="postgres", 
                            port="5432")
    cur = conn.cursor()

    return (conn, cur)


def create_table(execute, table_name, layout):
    """
    Cria tabela a partir do layout
    Arguments:
        execute: função de executar um comando no banco de dados
        table_name: Nome da tabela
        layout: layout
    """
    layout_columns = []
    for item in layout:
        name = item['Coluna']
        size = item['Tamanho']
        type = get_postgres_type(item['Tipo'])

        layout_columns.append(f"{name} {type}({size})")
   
    columns = ','.join(layout_columns)
    create_command = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"

    execute(create_command)


def get_postgres_type(type):
    """
    Oracle type para postgres type
    """
    if type == "VARCHAR2":
        return "VARCHAR"
    if type == "NUMBER":
        return "NUMERIC"
    return type


def insert_value(execute, table_name, data):
    """
    Inseri os dados
    Arguments:
        execute: função de executar um comando no banco de dados
        table_name: Nome da tabela
        data: dados
    """
    for item in data:
        data_columns = item.keys()
        data_values = item.values()

        # Lida com valores nulos e formatação
        insert_columns = list(map(lambda x: x if x is not None else 'NULL', data_columns))
        insert_values = list(map(lambda x: f"'{x}'" if x is not None else 'NULL', data_values))
        
        # Cria o comando de inserção
        columns = ','.join(insert_columns)
        values = ','.join(insert_values)
        insert_command = f"INSERT INTO {table_name} ({columns}) VALUES ({values});"

        execute(insert_command)


main()
