import psycopg2
import csv

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
def create_table(table_name, layout_path):
    with open(layout_path, 'r') as file:
        layout = csv.DictReader(file)

        layout_columns = []
        for row in layout:
            name = row['Coluna']
            type = get_postgres_type(row['Tipo'])
            size = row['Tamanho']

            layout_columns.append(f"{name} {type}({size})")
        
        columns = ','.join(layout_columns)
        create_command = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
        cur.execute(create_command)

# Inseri os dados a partir do layout e arquivo com os dados
def insert_value(table_name, layout_path, data_path):
        with open(layout_path, 'r') as layout_file, open(data_path, 'r', encoding="ISO-8859-1") as data_file:
            layout = csv.DictReader(layout_file)
            data = data_file.readlines()

            # Pega as colunas e range referente ao valor no arquivo
            layout_columns = []
            for column in layout:
                start_index = int(column["Inicio"]) - 1
                end_index = int(column["Fim"])

                layout_columns.append({ 
                    "name": f"{column['Coluna']}", 
                    "index_range": (start_index, end_index) 
                })

            # Para cada linha do arquivo, adiciona no banco
            for row in data:
                insert_columns = []
                insert_values = []

                # Relação linha, coluna
                for column in layout_columns:
                    start_index, end_index = column["index_range"]
                    value = row[start_index:end_index].strip()

                    # Lida com valores vazios
                    if len(value) > 0:
                        insert_columns.append(column["name"])
                        insert_values.append(f"'{value}'")

                columns = ','.join(insert_columns)
                values = ','.join(insert_values)
                insert_command = f"INSERT INTO {table_name} ({columns}) VALUES ({values});"
                cur.execute(insert_command)

def populate(table_data_paths):
    """
    Cria tabela e popula os dados com o formato do SIGTAP (Sistema de Gerenciamento da Tabela de Procedimentos, Medicamentos e OPM do SUS).
    Nota: Importante lembrar que precisa existir o arquivo de layout './tb_<nome-tabela>_layout.txt', contendo a formatação do arquivo de dados.
    Arguments:
        table_data_paths: lista de paths relativos ao arquivo de dados './tb_<nome-tabela>.txt'
    Returns:
        None
    """

    for table_data_path in table_data_paths:
        path, file_name = table_data_path.rsplit("tb_")
        table_name, extension = file_name.rsplit(".")
        layout_path = f"{path}tb_{table_name}_layout.{extension}"
        create_table(table_name, layout_path)
        insert_value(table_name, layout_path, table_data_path)

# É possível colocar todos os arquivos referentes as tabelas da competências do SIGTAP que o programa lidará de criar e popular
populate(["../data/tb_procedimento.txt"])

# Persiste as mudanças
conn.commit()

# Fecha a conexão
cur.close()
conn.close()