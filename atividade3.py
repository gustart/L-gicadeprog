peso = float(input("Digite seu pesso: "))
altura = float(input("Digite sua altura: "))

imc =  peso / (altura * 2)

print(f"Seu imc: {imc}")

if imc > 25:
    print("Vc está acima do peso")

if imc < 18.5:
    print("Vc está abixo do peso")

else:
    print("Seu peso está normal")


