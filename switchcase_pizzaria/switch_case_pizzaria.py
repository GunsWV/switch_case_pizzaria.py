print("Sabores/Preço de Pizza:")
print("1 - Pizza de Mussarela")
print("2 - Pizza de Calabresa")
print("3 - Pizza de Frango Catupiry")
print("4 - Pizza Portuguesa")
print("5 - Pizza de Nutella")
print("0 - SAIR")

#Solicita o código do produto ao usuário
codigo = int(input("Digite o codigo do produto:"))

#Use match-case para mostrar o preço com base mo código
match codigo:
    case 1:
        print("Pizza de Mussarela - Preço: R$ 40,00")
    case 2:
        print("Pizza de Calabresa - Preço: R$ 45,00")
    case 3:
        print("Pizza de Frango Catupiry - Preço: R$ 50,00")
    case 4:
        print("Pizza Portuguesa - Preço: R$ 55,00")
    case 5:
        print("Pizza de Nutella - Preço: R$ 48,98")
    case 0:
        print("Saindo do Programa...")
        exit()
    case _:
        print("Codigo inválido. Por favor, tente novamente.") 