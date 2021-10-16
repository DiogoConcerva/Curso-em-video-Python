p = float(input('Digite seu peso em Kg: '))
a = float(input('Digite sua altuma: '))
imc = (p / (a * a))

if (imc < 18.5):
    print('Você está abaixo do peso, seu IMC é {:.2f}'.format(imc))
elif ((imc >= 18.5) and (imc <= 25)):
    print('Você está no peso ideal, seu IMC é {:.2f}'.format(imc))
elif ((imc > 25) and (imc <= 30)):
    print('Você está com sobrepeso, seu IMC é {:.2f}'.format(imc))
elif ((imc > 30) and (imc <= 40)):
    print('Você está obeso, seu IMC é {:.2f}'.format(imc))
else:
    print('Você está com obesidade móbida, seu IMC é {:.2f}'.format(imc))
