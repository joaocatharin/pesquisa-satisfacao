# Pesquisa de satisfação - TudoWeb
# 50 entrevistados

qtd_excelente = 0
qtd_ruim = 0

print("=== Pesquisa de Satisfação - Atendimento TudoWeb ===\n")

for i in range(1, 51):
    print(f"--- Entrevistado {i}/50 ---")
    
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    
    # Validação da opinião com estrutura de decisão
    while True:
        print("Opinião sobre o atendimento:")
        print("1 - EXCELENTE")
        print("2 - BOM")
        print("3 - RUIM")
        opiniao = int(input("Digite a opção (1, 2 ou 3): "))
        
        if opiniao == 1:
            qtd_excelente += 1
            print(f"Registrado: {nome} ({idade} anos) - EXCELENTE")
            break
        elif opiniao == 2:
            print(f"Registrado: {nome} ({idade} anos) - BOM")
            break
        elif opiniao == 3:
            qtd_ruim += 1
            print(f"Registrado: {nome} ({idade} anos) - RUIM")
            break
        else:
            print("Opção inválida! Digite apenas 1, 2 ou 3.\n")
    
    print()  # Linha em branco para separar os entrevistados

# Resultados finais
print("=" * 50)
print("RESULTADO DA PESQUISA")
print("=" * 50)
print(f"a) Quantidade de respostas EXCELENTE: {qtd_excelente}")
print(f"b) Quantidade de respostas RUIM: {qtd_ruim}")
print("=" * 50)