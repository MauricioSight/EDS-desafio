import csv
import json

def main():
    create_json_file("../data/tb_procedimento_layout.txt", "../data/tb_procedimento.txt", "../data/tb_procedimento.json")
 

def create_json_file(layout_path, data_path, json_path):
        """
        Cria json file a partir do arquivo gerado pelo SIGTAP
        Arguments:
            layout_path: Path do arquivo de layout
            data_path: Path do arquivo dos dados
            json_path: Path do arquivo json escrito
        """
        with ( 
            open(layout_path, 'r') as layout_file, open(data_path, 'r', encoding="ISO-8859-1") as data_file, 
            open(json_path, 'w', encoding="ISO-8859-1") as json_file
        ):
            layout = csv.DictReader(layout_file)
            data = data_file.readlines()

            json_dic = {"layout": [], "data": []}

            # Pega as colunas e intervalo do index referente ao valor no arquivo
            layout_columns = []
            for column in layout:
                json_dic["layout"].append(column)

                start_index = int(column["Inicio"]) - 1
                end_index = int(column["Fim"])

                layout_columns.append({ 
                    "name": f"{column['Coluna']}", 
                    "index_range": (start_index, end_index) 
                })

            # Adiciona em 'json_dic' cada valor do arquivo csv
            for row in data:
                row_value = {}

                # Relação linha, coluna
                for column in layout_columns:
                    start_index, end_index = column["index_range"]
                    value = row[start_index:end_index].strip()

                    # Lida com valores vazios
                    if len(value) > 0:
                        row_value[column["name"]] = value
                    else:
                        row_value[column["name"]] = None

                json_dic["data"].append(row_value)         

            json.dump(json_dic, json_file)


main()
