peso_na_terra = float(input("Digite seu peso: "))
peso_no_planeta = peso_na_terra / 2

print ("Escolha um planeta:")
opera = int(input("1- mercurio, 2-Vênus, 3-marte, 4-Júpter, 5-saturno, 6-Urano: "))


if opera == 1:
    print("Seu peso em mercurio é:" )
    print(peso_no_planeta * 0.37)

elif opera == 2:
    print("Seu peso em Vênus é:" )
    print( peso_no_planeta * 0.88)

elif opera == 3:
    print("Seu peso em marte é:")
    print(peso_no_planeta * 0.38)


if opera == 4:
    print("Seu peso em Júpter é:")
    print(peso_no_planeta * 2.64)

elif opera == 5:
    print("Seu peso em saturno é:" )
    print( peso_no_planeta * 1.15)

elif opera == 6:
    print("Seu peso em urano é:")
    print( peso_no_planeta * 1.17)