# CALCULADORA PYTHON
print("\n******************* Python Calculator *******************")

def soma(x,y):
    return (x + y)

def sub(x,y):
    return (x - y)

def mult(x,y):
    return (x * y)

def div(x,y):
    return (x / y)

print ('\nSelecione o numero da operação abaixo: \n')
print('1 - SOMA: \n2 - SUBTRAÇÃO: \n3 - MULTIPLICAÇÃO \n4 - DIVISÃO')

numero = int(input('Digite sua Opção [1/2/3/4]: '))
while (numero > 5):
    print('Numero Digitado é Invalido !! \nReinicie o Programa e tente de Novo !! ')
    
    break

if (numero == 1):
    n1 = float(input('Digite um numero: '))
    n2 = float(input('Digite outro numero: '))
    print('{:.2f} + {:.2f} \nO valor da Soma será {:.2f}'.format(n1,n2,soma(n1,n2)))

elif(numero == 2):
    n1 = float(input('Digite um numero: '))
    n2 = float(input('Digite outro numero: '))
    print('{:.2f} - {:.2f} \nO valor da Subtração será {:.2f}'.format(n1,n2,sub(n1,n2)))

elif(numero == 3):
    n1 = float(input('Digite um numero: '))
    n2 = float(input('Digite outro numero: '))
    print('{:.2f} * {:.2f} \nO valor da Multiplicação será {:.2f}'.format(n1,n2,mult(n1,n2)))

elif(numero == 4):
    n1 = float(input('Digite um numero: '))
    n2 = float(input('Digite outro numero: '))
    print('{:.2f} / {:.2f} \nO valor da Divisão será {:.2f}'.format(n1,n2,div(n1,n2)))        
