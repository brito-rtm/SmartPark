import config as c

def consulta_faturamento():
    global valor_medio
    print("\n========== FATURAMENTO ==========")
    print(f"Faturamento acumulado: R$ {c.faturamento:.2f}")
    print(f"Total de saídas: {c.totalSaidas}")
    if c.totalSaidas > 0:
        valor_medio = c.faturamento / c.totalSaidas
        print(f"Média por saída: R$ {valor_medio:.2f}")
    else:
        print("Média por saída: R$ 0.00")

def tabela_precos():
    print("\n========== TABELA DE PREÇOS ==========")
    print(f"Tarifa por hora: R$ {c.TARIFA_HORA:.2f}")
    for hora in range(1, 6):
        valor = c.TARIFA_HORA * hora
        print(f"{hora} hora(s): R$ {valor:.2f}")