print('Software de Calc de IMC ')
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / (altura * altura)
if imc < 18.50:
    print("Abaixo do Peso!!")
elif imc >= 18.60 and imc <= 24.99:
    print('Peso Ideal Parabéns!!')
elif imc >= 25.00 and imc <= 29.99:
    print('Levemente Acima do Peso')
elif imc >= 30.00 and imc <= 34.99:
    print('Obesidade Grau 1')
elif imc >= 35.00 and imc <= 39.00:
    print('Obesidade Grau 2')
elif 40.00:
    print('Obesidade Grau 3 (Morbida)')
