
nome = input("Seu nome: ")

while True:
    sexo = str(input("Seu sexo: "))

    if(sexo.upper() == "M") | (sexo.upper() == "F"):
        
        altura = float(input("Sua altura: "))
        if (sexo.upper() == "M"):
            peso_ideal = (72.7 * altura) - 58
        elif (sexo.upper() == "F"):
            peso_ideal = (62.1 * altura) - 44.7

        print('Seu peso ideal é: {} para seu sexo que é {}' .format(peso_ideal, sexo))
        break
    else:
        print("Informação incorreta. Use M ou F")
        print("  ")



        
""