import config as c

def consulta_vagas():
    c.percentual_ocupacao = (c.vagasOcupadas / c.VAGAS_MAXIMAS) * 100
    print("\n========== CONSULTA DE VAGAS ==========")
    print(f"Capacidade total: {c.VAGAS_MAXIMAS}")
    print(f"Vagas ocupadas: {c.vagasOcupadas}")
    print(f"Vagas disponíveis: {c.vagasDisponiveis}")
    print(f"Percentual de ocupação: {c.percentual_ocupacao:.2f}%")

def relatorio_movimentacoes():
    print("\n========== RELATÓRIO DE MOVIMENTAÇÕES ==========")
    print(f"Total de entradas: {c.totalEntrada_Dias}")
    print(f"Total de saídas: {c.totalSaidas_Dias}")
    print(f"Veículos estacionados: {c.vagasOcupadas}")
    print(f"Faturamento acumulado: R$ {c.faturamento:.2f}")