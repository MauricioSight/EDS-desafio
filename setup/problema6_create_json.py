import csv
import json

# Cria json file a partir do arquivo gerado pelo SIGTAP
def create_json_file(layout_path, data_path, json_path):
        with open(layout_path, 'r') as layout_file, open(data_path, 'r', encoding="ISO-8859-1") as data_file, open(json_path, 'w', encoding="ISO-8859-1") as json_file:

            layout = csv.DictReader(layout_file)
            data = data_file.readlines()

            json_dic = {"layout": [], "data": []}

            # Pega as colunas e range referente ao valor no arquivo
            layout_columns = []
            for column in layout:
                json_dic["layout"].append(column)

                start_index = int(column["Inicio"]) - 1
                end_index = int(column["Fim"])

                layout_columns.append({ 
                    "name": f"{column['Coluna']}", 
                    "index_range": (start_index, end_index) 
                })

            # Para cada linha do arquivo, adiciona no banco
            for row in data:
                row_value = {}
                for column in layout_columns:
                    start_index, end_index = column["index_range"]
                    value = row[start_index:end_index].strip()
                    if len(value) > 0:
                        row_value[column["name"]] = value
                    else:
                        row_value[column["name"]] = None
                json_dic["data"].append(row_value)         

            json.dump(json_dic, json_file)

create_json_file("../data/tb_procedimento_layout.txt", "../data/tb_procedimento.txt", "../data/tb_procedimento.json")