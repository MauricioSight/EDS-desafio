import psycopg2
import json

# Conecta com o banco
conn = psycopg2.connect(
    database="stg_hospital",
    host="localhost",
    user="postgres",
    password="postgres",
    port="5432"
)
cur = conn.cursor()


# Oracle para postgres
def get_postgres_type(type):
    if type == "VARCHAR2":
        return "VARCHAR"
    if type == "NUMBER":
        return "NUMERIC"
    return type


# Criação da tabela a partir do layout
def create_table(table_name, layout):
    layout_columns = []
    for item in layout:
        name = item['Coluna']
        size = item['Tamanho']
        type = get_postgres_type(item['Tipo'])

        layout_columns.append(f"{name} {type}({size})")
   
    columns = ','.join(layout_columns)
    create_command = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
    cur.execute(create_command)


# Inseri os dados a partir do layout e arquivo com os dados
def insert_value(table_name, data):
    for item in data:
        data_columns = item.keys()
        data_values = item.values()

        insert_columns = list(map(lambda x: x if x is not None else 'NULL', data_columns))
        insert_values = list(map(lambda x: f"'{x}'" if x is not None else 'NULL', data_values))

        columns = ','.join(insert_columns)
        values = ','.join(insert_values)
        insert_command = f"INSERT INTO {table_name} ({columns}) VALUES ({values});"
        cur.execute(insert_command)


def post(body):
    create_table(body["table_name"], body["layout"])
    insert_value(body["table_name"], body["data"])


# Simular operação POST de um API-REST
def simulate_post(path):
    with open(path, 'r') as file:
        reader = json.load(file)

        _, file_name = path.rsplit("tb_")
        table_name, _ = file_name.rsplit(".")

        post({ "table_name": table_name, "data": reader["data"], "layout": reader["layout"] })


simulate_post("../data/tb_procedimento.json")

# Persiste as mudanças
conn.commit()

# Fecha a conexão
cur.close()
conn.close()