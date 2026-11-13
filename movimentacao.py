import config as c

def entrada_veiculos():
    c.vagasOcupadas, c.totalEntrada_Dias, c.vagasDisponiveis
    print("\n\033[32m-> ENTRADA DE VEÍCULOS SELECIONADO\033[m")
    c.seguir = 1
    while c.seguir == 1:
        if c.vagasDisponiveis == 0:
            print("Oops... Vagas esgotadas!")
            break
        c.placa = str(input("\nDigite a placa: "))
        c.modelo = str(input("Modelo do automóvel: "))
        c.cor = str(input("Cor do veículo: "))
        c.vagasOcupadas += 1
        c.totalEntrada_Dias += 1
        c.vagasDisponiveis = c.VAGAS_MAXIMAS - c.vagasOcupadas
        print("\n===== Situação \033[1;37mSmart\033[m\033[1;34mPark\033[m =====")
        print("Vagas Máximas: ", c.VAGAS_MAXIMAS)
        print("Vagas Ocupadas: ", c.vagasOcupadas)
        print("Vagas Disponiveis: ", c.vagasDisponiveis)
        if c.vagasDisponiveis == 0:
            print("\n\033[1;30mOps... Vagas esgotadas!\033[m\n")
            break
        c.seguir = int(input("Registrar outro veículo? [1] Sim [2] Não = "))
        if c.seguir == 2:
            break

#OPÇÃO (SAÍDA DE VEÍCULOS)

def saida_veiculos():
    c.faturamento, c.vagasOcupadas, c.totalSaidas_Dias, c.vagasDisponiveis, c.totalSaidas
    if c.vagasOcupadas == 0:
        print("\n\033[1;31mNão existem veículos estacionados! Não é possível registrar uma saída!!\033[m")
    else:
        print("\n\033[32m-> SAÍDA DE VEÍCULOS SELECIONADO\033[m\n")
        c.FECHAMENTO = 22.0
        c.ABERTURA = 6.0
        c.horarioEntrada = float(input("Horário da entrada do veículo: "))
        if c.horarioEntrada < c.ABERTURA:
            print("O estacionamento só abre às 6:00!")
        elif c.horarioEntrada >= c.FECHAMENTO:
            print("O estacionamento fecha ás 22:00!")
        else:
            c.horarioSaida = float(input("Horário de saída do veículo: "))
            c.TEMPOTOTAL = c.horarioSaida - c.horarioEntrada
            c.VALOR = c.TEMPOTOTAL * 5
            c.faturamento = c.faturamento + c.VALOR
            if c.horarioSaida <= c.horarioEntrada:
                print("Digite um horário válido: ")
            elif c.TEMPOTOTAL < 1:
                print("Tempo mínimo de permanência: 1 hora.")
            elif c.horarioSaida > c.FECHAMENTO:
                print("O estacionamento fecha às 22:00!")
            else:
                c.vagasOcupadas -= 1
                c.totalSaidas_Dias += 1
                c.vagasDisponiveis += 1
                c.totalSaidas += 1
                print("\n=====================================")
                print("Muito obrigado. Volte sempre!")
                print(f"Valor: R$ {c.VALOR:.2f}")
                print("=====================================\n")
                print("\n======== \033[1;37mSituação\033[m \033[1;37mSmart\033[m\033[1;34mPark\033[m =========")
                print("\033[1;32mUma vaga foi liberada!\033[m")
                print(f"Vagas ocupadas: {c.vagasOcupadas}")
                print(f"Vagas disponiveis: {c.vagasDisponiveis}")
                print("=====================================\n")