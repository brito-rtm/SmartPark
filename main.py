from movimentacao import saida_veiculos, entrada_veiculos
from relatorio import consulta_vagas, relatorio_movimentacoes
from financeiro import consulta_faturamento, tabela_precos


def menu():
    print("\n============= \033[1;37mSmart\033[m\033[1;34mPark\033[m =============")
    print("\033[1;34m[ 1 ]\033[m Registrar entrada de veículo")
    print("\033[1;34m[ 2 ]\033[m Registrar Saída de Veículos")
    print("\033[1;34m[ 3 ]\033[m Consultar vagas disponíveis")
    print("\033[1;34m[ 4 ]\033[m Consultar faturamento")
    print("\033[1;34m[ 5 ]\033[m Relatório")
    print("\033[1;34m[ 6 ]\033[m Consultar tabela de preços")
    print("=====================================")
    print("\033[1;31m[ 0 ]\033[m Encerrar sistema")
    print("=====================================")

while True:
    menu()
    try:
        opcao = int(input(f"\033[1;34mO QUE VOCÊ DESEJA?\033[m "))
    except ValueError:
        print("\033[1;30;41mOOPPSS... Digite uma opção válida!\033[m")
        continue
    if opcao == 0:
        print("\n\033[1;31mSmartPark encerrado com sucesso!\033[m")
        break

    if opcao == 1:
        entrada_veiculos()

    elif opcao == 2:
        saida_veiculos()

    elif opcao == 3:
        consulta_vagas()

    elif opcao == 4:
        consulta_faturamento()

    elif opcao == 5:
        relatorio_movimentacoes()

    elif opcao == 6:
        tabela_precos()