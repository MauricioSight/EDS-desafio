# Algoritmo responsável por verificar a disponibilidade de medicamentos em estoque
def check_is_possible(prescricao, estoque):
    recipe_len = len(prescricao)
    stock_len = len(estoque)

    # Caso raro pra salvar recurso computacional
    if stock_len < recipe_len:
        return False

    recipe = list(prescricao)
    stock = list(estoque)

    recipe.sort()
    stock.sort()

    times_added = 0
    start_index = 0
    for drug in recipe:
        for i in range(start_index, stock_len):
            if drug == stock[i]:
                start_index = i + 1
                times_added += 1
                break

    if times_added == recipe_len:
        return True
    
    return False

print("check_is_possible(a, a)", check_is_possible("a", "b")) # False
print("check_is_possible(aa, b)",check_is_possible("aa", "b")) # False
print("check_is_possible(aa, aab)",check_is_possible("aa", "aab")) # True
print("check_is_possible(aba, cbaa)",check_is_possible("aba", "cbaa")) # True