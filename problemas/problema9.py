def main():
    # Testes de caso
    print("check_is_possible(a, a)", check_is_possible("a", "b")) # Retorno esperado: False
    print("check_is_possible(aa, b)",check_is_possible("aa", "b")) # Retorno esperado:False
    print("check_is_possible(aa, aab)",check_is_possible("aa", "aab")) # Retorno esperado:True
    print("check_is_possible(aba, cbaa)",check_is_possible("aba", "cbaa")) # Retorno esperado:True


def check_is_possible(recipe_sequence, stock_sequence):
    """
    Algoritmo responsável por verificar a disponibilidade de medicamentos em estoque
    Arguments:
        recipe_sequence: sequencia de medicamentos que foram prescritos
        stock_sequence: sequencia de medicamentos que estão no estoque
    """
    recipe_len = len(recipe_sequence)
    stock_len = len(stock_sequence)

    # Caso raro pra salvar recurso computacional
    if stock_len < recipe_len:
        return False

    recipe = list(recipe_sequence)
    stock = list(stock_sequence)

    recipe.sort()
    stock.sort()

    # Verifica se existe relação para cada medicamento em estoque
    times_added = 0
    start_index = 0
    for drug in recipe:
        # Uso da função range para pular os que já foram relacionados
        for i in range(start_index, stock_len):
            # Caso existe relação, salva index e adiciona em um contador
            if drug == stock[i]:
                start_index = i + 1
                times_added += 1
                break

    # Caso a quantidade adicionado seja igual a quantidade de medicamentos 
    # em stock significa que é possível
    if times_added == recipe_len:
        return True
    
    return False


main()
