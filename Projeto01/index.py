nome = input("Informe seu Nome: ")
sobrenome = input("Informe seu Sobrenome: ")
idade = input("Informe sua Idade: ")

# "sep" é utilizado para separar.
print(nome, sobrenome, idade, sep=" --- ")

# "end" é para colocar algo no fim de uma frase.
# Para fazer uma frase com valores recebidos dentro{} colocar -> f <- antes das ""
print(f"Seu Nome é {nome} {sobrenome} e sua Idade é de {idade} anos", end="...\n")


# Adição
print(1 + 1)
# Resposta: 2

# Subtração
print(10 - 2)
# Resposta: 8

# Multiplicação
print(5 * 2)
# Resposta: 10

# Exponenciação
print(10 ** 3)
# Resposta: 1000

# Divisão
print(12 / 2)
# Resposta: 6.0

# Divisão Inteira
print(12 // 2)
# Resposta: 6

# Módulo
print(10 % 4)
# Resposta: 2


cal_1 = 10 - 5 * 2
# Resposta: 0 
print(f"Resposta: {cal_1}")

cal_2 = (10 - 5) * 2
# Resposta: 10 
print(f"Resposta: {cal_2}")

cal_3 = 10 ** 2 * 2
# Resposta: 200 
print(f"Resposta: {cal_3}")

cal_4 = 10 ** (2 * 2)
# Resposta: 10000
print(f"Resposta: {cal_4}")

cal_5 = 10 / 2 * 4
# Resposta: 20.0 
print(f"Resposta: {cal_5}")