#tirando a media
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

media = (num1 + num2 + num3) / 3

print("A média dos números é:", media)


#Decidindo qual é par ou impar
num = int(input("Digite um número: "))

if num % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")


#Números pares de zero até número escrito
num = int(input("Digite um número: "))

for i in range(0, num + 1, 2):
    print(i)

#Maior e menor número em lista
numeros = [int(x) for x in input("Digite uma lista de números separados por espaço: ").split()]

maior = max(numeros)
menor = min(numeros)

print("Maior valor:", maior)
print("Menor valor:", menor)

#Média dos números pares em lista
numeros = [int(x) for x in input("Digite uma lista de números separados por espaço: ").split()]

numeros_pares = [x for x in numeros if x % 2 == 0]
media = sum(numeros_pares) / len(numeros_pares)

print("Média dos números pares:", media)

#Fatorial de número inteiro e positivo
num = int(input("Digite um número inteiro positivo: "))

if num < 0:
    print("Número deve ser positivo.")
else:
    resultado = 1
    for i in range(1, num + 1):
        resultado *= i
    print(f"O fatorial de {num} é {resultado}")


#Sequência de Fibonacci até valor escolhido
num = int(input("Digite um valor para a sequência de Fibonacci: "))

a, b = 0, 1
while a <= num:
    print(a)
    a, b = b, a + b


#Verifica se número é primo
num = int(input("Digite um número: "))

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "não é primo")
            break
    else:
        print(num, "é primo")
else:
    print(num, "não é primo")

#Criando lista com apenas nommes que começam com A
nomes = input("Digite uma lista de nomes separados por espaço: ").split()
nomes_com_A = [nome for nome in nomes if nome.startswith('A')]

print("Nomes que começam com 'A':", nomes_com_A)


#Pedra, papel e tesoura para relaxar
import random

opcoes = ["Pedra", "Papel", "Tesoura"]

usuario = input("Escolha Pedra, Papel ou Tesoura: ")
computador = random.choice(opcoes)

print(f"Computador escolheu: {computador}")

if usuario == computador:
    print("Empate!")
elif (usuario == "Pedra" and computador == "Tesoura") or \
     (usuario == "Papel" and computador == "Pedra") or \
     (usuario == "Tesoura" and computador == "Papel"):
    print("Você venceu!")
else:
    print("Computador venceu!")






