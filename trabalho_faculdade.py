print('''======= BUFFET AHP =======
[1] Festa de Aniversário
[2] Churrasco
[3] Casamento
[4] Personalizar
[5] PARTICIPANTES''')

opcao = int(input('Escolha uma das alternativas: '))
if opcao == 5:
    print('''Alessandro Girondoli Dionizio
Pedro Lucas Oliveira Santos koch
Heitor Moreira da Silva ''') 
    
    
quantidade_pessoas = int(input('Quantidade de pessoas: '))
tempo_festa = input('Tempo da festa (em horas): ') 


#OPCAO = VARIAVEL PARA CONDICIONAL IDENTIFICAR QUAL E A ESCOLHA
if opcao == 1:  # Festa de Aniversário
    print("Quantidades sugeridas para suas escolhas:")
    print('Bolo:           ', quantidade_pessoas * 100, 'Gramas')
    print('Salgados:       ', quantidade_pessoas * 20, 'Unidades')
    print('Brigadeiro:     ', quantidade_pessoas * 5, 'Unidades')
    print('Refrigerantes:  ', quantidade_pessoas * 2, 'Litros')
    print('Cachorro Quente:', quantidade_pessoas * 5, 'Unidades')

elif opcao == 2:  # Churrasco
    print("Quantidades sugeridas para suas escolhas:")
    print('Bolo:           ', quantidade_pessoas * 100, 'Gramas')
    print('Feijão Tropeiro:', quantidade_pessoas * 100, 'Gramas')
    print('Carne:          ', quantidade_pessoas * 3, 'Kilogramas')
    print('Salgados:       ', quantidade_pessoas * 15, 'Unidades')
    print('Refrigerantes:  ', quantidade_pessoas * 2, 'Litros')
    print('Bebidas Alcoólicas:', quantidade_pessoas * 3, 'Litros')
    print('Sucos:         ', quantidade_pessoas * 3, 'Litros')

elif opcao == 3:  # Casamento
    print("Quantidades sugeridas para suas escolhas:")
    print('Bolo:           ', quantidade_pessoas * 115, 'Gramas')
    print('Pratos Quentes: ', quantidade_pessoas * 2, 'Refeições')
    print('Pratos Frios:   ', quantidade_pessoas * 2, 'Unidades')
    print('Salgados:       ', quantidade_pessoas * 15, 'Unidades')
    print('Doces:         ', quantidade_pessoas * 8, 'Unidades')
    print('Refrigerantes:  ', quantidade_pessoas * 2, 'Litros')
    print('Bebidas Alcoólicas:', quantidade_pessoas * 2, 'Litros')
    print('Frutos do Mar:   ', quantidade_pessoas * 2, 'Pratos')
    print('Massas:         ', quantidade_pessoas * 2, 'Unidades')
    

elif opcao == 4:  # Personalizado
    print('''====ESCOLHA ATÉ 5 OPÇÕES====
[1] Refrigerante
[2] Carnes
[3] Salgados
[4] Frutos do Mar
[5] Doces
[6] Feijão Tropeiro
[7] Bebidas Alcoólicas''')

              #estrutura de repetição para esolher os items da personalizacao
    escolhas = []
    for i in range(5):
        escolha = int(input(f'Escolha {i + 1}: '))
        if escolha in range(1, 8):  # Verifica se a escolha é válida
            escolhas.append(escolha)
        else:
            print("Escolha inválida, tente novamente.")
            break

    print("\nVocê escolheu as seguintes opções:")
    for e in escolhas:
        print(f'Opção {e}')

    # Exibe as quantidades com base nas escolhas personalizadas
    print("\nQuantidades sugeridas para suas escolhas:")
    for e in escolhas:
        if e == 1:  # Refrigerante
            print('Refrigerante:  ', quantidade_pessoas * 2, 'Litros')
        elif e == 2:  # Carnes
            print('Carne:          ', quantidade_pessoas * 3, 'Kilogramas')
        elif e == 3:  # Salgados
            print('Salgados:       ', quantidade_pessoas * 15, 'Unidades')
        elif e == 4:  # Frutos do Mar
            print('Frutos do Mar:   ', quantidade_pessoas * 2, 'Pratos')
        elif e == 5:  # Doces
            print('Doces:         ', quantidade_pessoas * 8, 'Unidades')
        elif e == 6:  # Feijão Tropeiro
            print('Feijão Tropeiro:', quantidade_pessoas * 100, 'Gramas')
        elif e == 7:  # Bebidas Alcoólicas
            print('Bebidas Alcoólicas:', quantidade_pessoas * 3, 'Litros')

else:
    print("Opção inválida.")
    
