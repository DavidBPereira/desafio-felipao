heroi = input("Digite o nome do herói: ")
exp = int(input("Digite a xp do herói: "))

        

if exp < 1000:
    print (f"O Herói de nome {heroi} está no nível de Ferro")
if exp in range(1001,2001):
    print (f"O Herói de nome {heroi} está no nível de Bronze")
if exp in range(2001,5001):
    print (f"O Herói de nome {heroi} está no nível de Prata")
if exp in range(5001,7001):
    print (f"O Herói de nome {heroi} está no nível de Ouro")
if exp in range(7001,8001):
    print (f"O Herói de nome {heroi} está no nível de Platina")
if exp in range(8001,9001):
    print (f"O Herói de nome {heroi} está no nível de Ascendente")
if exp in range(9001,10001):
    print (f"O Herói de nome {heroi} está no nível de Imortal")
if exp >= 10001:
    print (f"O Herói de nome {heroi} está no nível de Radiante")


