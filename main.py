#x = int(input('Digite um número inteiro: '))
#y=  int(input('Digite outro número inteiro: '))
#
#res = f'O resultado da soma de {x} com {y} é {x + y}.'
#print(res) 

#preco = float(input('Digite o preco do produto:'))
#percentual = float(input('Digite o percentual de desconto (0-100%):'))

#desconto = preco * (percentual / 100)
#final = preco - desconto

#print(f'O preco do produto foi de {preco} e recebeu um desconto de {percentual}% equivalente a {desconto} logo o valor final foi de {final}')

#n_km = int(input('Digite a quantidade de Km rodados com o carro alugado:'))
#n_dia = int(input('Digite a quantidade de dias que o carro foi alugado:'))

#custo_km = (n_km * 0.15)
#custo_dia = (n_dia * 60)
#custo_total = custo_km + custo_dia

#print(f'Voce rodou {n_km}km no veiculo e teve um custo de R${custo_km} em Km rodados.')
#print(f'Voce alugou o carro por {n_dia} dias e teve um custo de R${custo_dia} em diarias.')
#print(f'Voce teve um custo total de R${custo_total} com a locadora.')

#frase = input('Digite uma frase:')
#tam = len(frase)
#
#frase2 = frase[:int(tam/2)]

#print(frase2[-2:])

# x = int(input('Digite um valor inteiro: '))
# 
# y = int(input('Digite um segundo valor inteiro: '))
# 
# if (x > y):
#     print('O primeiro eh maior que o segundo.')

# elif (x == y):
#     print('Numeros iguais.')
# 
# else:
#     print('Segundo maior que o primeiro')

# PAR OU IMPAR

# x = int(input('Digite um valor inteiro: '))
# 
# if (x % 2 == 0):
#     print('Numero par!')
# 
# else:
#     print('Numero impar!')

# m1 = float(input('Digite a nota da primeira materia: '))
# m2 = float(input('Digite a nota da segunda materia: '))
# m3 = float(input('Digite a nota da terceira materia: '))
# 
# if m1 >= 7 and m2 >= 7 and m3 >=7:
#     print('Aluno aprovado!');
# else:
#     print('Aluno nao aprovado!');


# print('Escolha o que deseja comprar: ')
# print('1 - Apple')
# print('2 - Orange')
# print('3 - Banana')

# produto = int(input('Qual sua escolha?'))
# qtd = int(input('Quantas unidades?'))

# if (produto == 1):
#     pagar = qtd * 2.3
#     print(f'Voce comprou {qtd} apples. Total a pagar: {pagar}')
# 
# elif (produto == 2):
#     pagar = qtd * 3.6
#     print(f'Voce comprou {qtd} oranges. Total a pagar: {pagar}')
# 
# elif (produto == 3):
#     pagar = qtd * 1.85
#    print(f'Voce comprou {qtd} bananas. Total a pagar: {pagar}')
# 
# else:
#     print('Produto inexistente!')


# nome = input('Qual seu nome?')
# 
# idade = int(input('Qual sua idade?'))
# 
# if nome == 'Vinicius':# 
#     print('Oi, Vinicius')
# 
# elif idade < 18:
#     print('Nao autorizado!')
# 
# elif idade > 100:
#     print('Idade nao existe, favor verificar!')


# idade = int(input('Qual sua idade?'))
# 
# if (idade > 60):
#     print('Voce tem direito aos beneficios.')

# dano = int(input('Qual o dano realizado?'))
# escudo = int(input('Qual seu escudo?'))
# 
# if (dano > 10 and escudo == 0):
#     print('Voce esta morto!')

# norte = True
# sul = False
# leste = False
# oeste = False
# 
# if (norte == True or sul == True or leste == True or oeste == True):
#     print('Voce escapou!')


# ano = int(input('Digite seu ano de nascimento:'))
# 
# if (ano % 4 == 0): 
#     print('Pode ser um ano bissexto')
# else:
#     print('Definitivamente nao eh um ano bissexto')

# cima = True
# baixo = False
# 
# if (cima == True and baixo == True):
#     print('Decida-se!')
# else:
#     print('Voce escolheu um caminho!')

# A = int(input('Digite o primeiro lado do triangulo:'))
# B = int(input('Digite o segundo lado do triangulo:'))
# C = int(input('Digite o terceiro lado do triangulo:')) 
# 
# if ((A > 0 and B > 0 and C > 0) and (A + B > C and A + C > B and B + C > A)):
#     # Se chegou ate aqui, pq o triangulo sera valido.
#     if (A != B and A!= C and B!= C):
#         print('Triangulo escaleno.')
#     else:
#         if (A == B and A == C and B == C):
#             print('Triangulo Equilatero!')
#         else:
#            print('Triangulo isosceles!')
# else:
#     print('Ao menos um dos valores indicados nao serve para a formacao de um triangulo.')

# print('+ Adicao')
# print('CALCULADORA')
# print('- Subtracao')
# print('* Multiplicacao')
# print('/ Divisao')
# print('Pressione qualquer outra tecla para sair.')
# 
# op = input('Qual operacao deseja realizar?')
# x = int(input('Digite o primeiro valor'))
# y = int(input('Digite o segundo valor'))
# 
# if (op == '+'):
#     res = x + y
#     print(f'Resultado: {x} + {y} = {res}')
# 
# elif (op == '-'):
#     res = x - y
#     print(f'Resultado: {x} - {y} = {res}')
# 
# elif (op == '*'):
#     res = x * y
#     print(f'Resultado: {x} * {y} = {res}')
# 
# elif (op == '/'):
#     res = x / y
#     print(f'Resultado: {x} / {y} = {res}')
# 
# else:
#     print('Encerrando o programa...')

# print('Conta energia eletrica:')
# print('Informe o tipo de conta:')
# print('R - Residencial')
# print('C - Comercial')
# print('I - Industrial')
# 
# 
# tipo = input('Qual tipo de conta voce possui?')
# kwh = int(input('Qual o consumo em kWh?'))
# 
# if (tipo == 'R' and kwh <= 500):
#     conta = kwh * 0.4
#     print(f'Sua conta foi de R$ {conta}')
# elif (tipo == 'R' and kwh > 500):
#     conta = kwh * 0.65
#     print(f'Sua conta foi de R$ {conta} ')
# 
# elif (tipo == 'C' and kwh <= 1000):
#     conta = kwh * 0.55
#     print(f'Sua conta foi de R$ {conta} ')
# 
# elif (tipo == 'C' and kwh > 1000):# 
#     conta = kwh * 0.60
#     print(f'Sua conta foi de R$ {conta} ')   
# 
# elif (tipo == 'I' and kwh <= 5000):
#    conta = kwh * 0.55
#     print(f'Sua conta foi de R$ {conta} ') 
# 
# elif (tipo == 'I' and kwh > 5000):
#     conta = kwh * 0.60
#     print(f'Sua conta foi de R$ {conta} ')  
# 
# else:
#     print('Erro encontrado, favor digitar novamente!')


# soma = 0
# cont = 1
# 
# while (cont <= 5):
#     x = float(input(f'Digite a {cont} nota: '))
#     soma += x
#     cont += 1
# media = soma / 5
# print(f'Media final: {media}')

# x = int(input('Digite um valor maior do que zero: '))
# while (x <= 0):
#     x = int(input('Digite um valor maior do que zero: '))
# print(f'Voce digitou {x}. Encerrando o programa.')

# print('Digite uma mensagem que irei repetir para voce:')
# print('Para encerrar escreva "sair".')
# 
# while True:
#     texto = input('')
#     print(texto)
#     if texto == 'sair':
#         break
# print('Encerrando o programa..')


# while True:
#     nome = input('Qual o seu nome ?')
#     if (nome != 'Lenhadorzinho'):
#         print('Usuario nao registrado, tente novamente.')
#        continue
# 
#    senha = input('Qual a sua senha?')
#     if (senha == '1234'):
#         break
# print('Acesso concedido.')

# nome = ''
# 
# while not nome:
#     # encererra o laco quando nome nao estiver vazio
#     nome = input('Digite seu nome:')
# 
# valor = int(input('Digite um numero qualquer: '))
# if valor: #Equivalente if valor !=0:
#     print('Voce digitou um valor diferente de zero.')
# else:
#     print('Voce digitou zero.')


# for i in range (6):
#     print(i)

# for i in range (0, 6, 1):   # Valor inicial 0, Valor final 6, passo do iterador 1.
#    print(i)

# for i in range (10, 0, -2):
#    print(i)

# frase = 'Logica de Programacao e Algoritmos'
# for i in range(0, len(frase), 1):
#    print(frase[i], end='')


# soma = 0
# qtd = 0
# for i in range (1, 101):
#     if (i % 2 == 0):
#         soma += i
#         qtd += 1
# media = soma / qtd
# print(f'A media dos pares de 0 ate 100 fica em: {media}')

######### ESTRUTURAS E REPETICAO ANINHADAS #########

# 2x while

# tabuada = 1
# while tabuada <= 10:
#     print(f'TABUADA DO {tabuada}:')
#     i = 1
#     while i <= 10:
#         print(f'{tabuada} x {i} = {tabuada * i}')
#         i += 1
#     tabuada += 1


#2x for

# for tabuada in range (1,11,1):
#     print(f'TABUADA DO {tabuada}: ')
#     i = 1
#     for i in range (1, 11, 1):
#         print(f'{tabuada} x {i} = {tabuada * i}')

#while + fir

# tabuada = 1
# while tabuada <= 10:
#     print(f'TABUADA DO  {tabuada}:')
#     for i in range (1, 11, 1):
#         print(f'{tabuada} x {i} = {tabuada * i}')
#     tabuada += 1


#for i in range (3,13,1):
 #   print(i)


# x = 3
# while (x <= 12):
#     print(x)
#     x += 1

# for i in range (0, 9, 2):
#     print(i)

# x = 0

# while (x < 9):
#     print(x)
#     x += 2

# print('LANCHONETE')
# print('1 - Coxinha R$ 5.00')
# print('2 - Pastel R$ 7.00')
# print('3 - Cafe R$ 4.00')
# print('4 - Suco R$ 6.00')
# print('5 - SAIR')

# total = 0
# while True:
#     op = int(input('Qual item gostaria de comprar?'))
#     
#     if (op == 1):
#         qtd = int(input('Quantas unidades quer comprar?'))
#         total = total + qtd * 5
# 
#    elif (op == 2):
#        qtd = int(input('Quantas unidades quer comprar?'))
#        total = total + qtd * 7
# 
#    elif (op == 3):
#         qtd = int(input('Quantas unidades quer comprar?'))
# 
#         total = total + qtd * 4
# 
#     elif (op == 4):
#         qtd = int(input('Quantas unidades quer comprar?'))
#         total = total + qtd * 6
# 
#     elif (op == 5):
#         break
# 
#     else:
#         print('Produto invalido, selecione novamente.')
# 
# print(f'Total a pagar sera de R$ {total}') 

""" valor = int(input('Digite o valor em R$ : '))

while True:
    if valor >= 100:
        cont100 = valor // 100
        valor = valor - cont100 *100
        print(f'Cedulas de 100: {cont100}')
        if not valor:
            break

    if valor >= 50:
        cont50 = valor // 50
        valor = valor - cont50 *50
        print(f'Cedulas de 50: {cont50}')
        if not valor:
            break


    if valor >= 20:
        cont20 = valor // 20
        valor = valor - cont20 *20
        print(f'Cedulas de 20: {cont20}')
        if not valor:
            break

    if valor >= 10:
        cont10 = valor // 10
        valor = valor - cont10 *10
        print(f'Cedulas de 10: {cont10}')
        if not valor:
            break

    if valor >= 5:
        cont5 = valor // 5
        valor = valor - cont5 *5
        print(f'Cedulas de 5: {cont5}')
        if not valor:
            break

    if valor:
        cont1 = valor    
        print(f'Cedulas de 1: {cont1}')
        break
 """
""" 
total = 0
dinheiro = 0
acc_idade = 0

while True:
    idade = int(input('Qual sua idade?'))
    if idade == 0:
        break

    total += 1
    acc_idade += idade
    if idade < 3:
        ingresso = 0
    
    else:
        if idade >= 12:
            ingresso = 30
        else:
            ingresso = 15

    dinheiro += ingresso

if total > 0:
    media = acc_idade / total
    print(f'Total de pessoas: {total}')  
    print(f'Total arrecadado: {dinheiro}')  
    print(f'Media arrecadada: {media}')  
 """

""" def realce():
    #corpo da funcao
    print('|', '__' * 10, '|')
    print('|', '__' * 10, '|')
#Programa Principal
realce()
print('          MENU')
realce()
 """

""" def sub2(x, y):
    res = x - y
    print(res)
sub2(5, 7) """


""" def borda(s1):
    tam = len(s1)

    if tam:
        print('+', '-' * tam, '+')
        print('|',s1, '|')
        print('+', '-' * tam, '+')

borda('Ola, mundo!')
borda('Logica de Porgramacao e Algoritmos') """

########## ESCOPO DE VARIAVEIS

""" def omelete():
    ovos = 12

omelete()
print(ovos) """

#####################################

""" def soma3(x = 0, y = 0, z = 0):
    res = x + y + z
    return res

retornado1 = soma3(1, 2, 3)
retornado2 = soma3(1, 2)
retornado3 = soma3()
print(f'Somatorios: {retornado1}, {retornado2} e {retornado3}') """


""" def valida_string(pergunta, min, max):
    s1 = input(pergunta)
    tam = len(s1)
    while ((tam <min) or (tam > max)):
        s1 = input(pergunta)
        tam = len(s1)
    return s1

    # Programa Principal

x = valida_string('Digite uma string: ', 10, 30)
print('Voce digitou a string: {}. \n Dado valido. Encerrando o programa...' .format(x))
 """


""" while True:
    try:
        x = int(input('Por favor digite um numero: '))
        break
    except ValueError:
        print('Oops! Numero invalido, Tente novamente!') """


""" i = 0
while True:
    try: 
        nome = input('Por favor digite os eu nome: ')
        ind = int(input('Digite um indice do seu nome digitado: '))
        print(nome[ind])
        break
    except ValueError:
        print('Oops! Nome invalido. Tente novamente...')
    except IndexError:
        print('Ooops! indice invalido. Tente novamente...')
    finally:
        print(f'Tentativa {i}')
        i += 1 """

""" def div():
    try:
        num1 = int(input('Digite um numero: '))
        num2 = int(input('Digite um numero: '))
        res = num1 / num2
    except ZeroDivisionError:
        print('Oops! Erro de divisao por zero...')
    except:
        print('Algo de errado aconteceu...')
    else:
        return res
    finally:
        print('Executara sempre!')


print(div())
 """


#### FUNCOES LAMBDA

""" res = lambda x: x * x
print(res(3))

 """

""" soma = lambda x, y: x + y
print(soma(3, 5))

calc = lambda a, b: (a + 5) * b
print(calc(5, 10))


 """

""" def soma3(x = 0, y = 0, z = 0):
    

    print(soma3(3, 2))
    help(soma3)
 """

""" def valida_int (pergunta, min, max):
    x = int(input(pergunta))
    while((x < min) or (x > max)):
        x = int(input(pergunta))

    return x

def fatorial (num):
    
    fat = 1
    if num == 0:
        return fat
    # esta parte so executa caso num > 0
    for i in range (1, num + 1, 1):
        fat *= i

    return fat

x = valida_int('Digite um valor para calcular a fatorial:', 0, 99999)
print(f'{x}! = {fatorial(x)}')
 """

#### tuplas #### Listas entre parentesis sem poder alterar.

""" mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate')

for item in mochila:
    print(f'Na minha mochila tem: {item}')
 """
""" 
mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate')
upgrade = ('Queijo', 'Canivete')
mochila_grande = mochila + upgrade
print(mochila)
print(upgrade)
print(mochila_grande)
 """

""" def soma(*num):
    acumulador = 0
    print(f'Tupla: {num}')
    for i in num:
        acumulador += i
    return acumulador

print(f'Resultado: {soma(1,2)}\n')
print(f'Resultado: {soma(1,2,3,4,5,6,7,8,9)}\n') """


""" mochila = ['Machado', 'Camisa', 'Laranja', 'Abacate']

mochila.append('Ovos') #adiciona ao final da lista
print('Lista: ', mochila)

mochila.insert(1, 'Canivete') #insere na posicao informada
print('Lista: ', mochila)

del mochila[1] #deleta do indice informado
print('Lista: ', mochila)

mochila.remove('Ovos') #deleta o dado informado
print('Lista: ', mochila) """



""" mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
print(mochila[0])
print(mochila[0][0])
print(mochila[2][2]) """

""" mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
for item in mochila:
    for letra in item:
        print(letra, end='')
    print() """

""" mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
for i in range(0,len(mochila),1):
    for j in range(0,len(mochila[i]),1):
        print(mochila[i][j], end='')
    print() """

#### Listas dentro de listas

""" mochila = [['Cebola', 0.39], ['Tomate', 0.49], ['Maca', 0.89]]
print(mochila[0][0][2]) """

""" item = []
mercado = []

for i in range (3):
    item.append(input('Digite o nome do item: '))
    item.apeend(int(input('Digite a quantidade: ')))
    item.appned(float(input('Digite o valor: ')))
    mercado.append(item[:])
    item.clear()
print(mercado) """

""" mercado = []

for i in range(3):
    nome = input('Digite o nome do item: ')
    qtd = int(input('Digite a quantidade: '))
    valor = float(input('Digite o valor: '))
    mercado.append([nome, qtd, valor])

print(mercado) 

soma = 0 
print('Lista de compras: ')
print('-' * 20)
print('item | quantidade | valor unitario | total do item ')
for item in mercado:
    print('{} | {} | {} | {}'.format(item[0], item[1], item[2], item[1] * item [2]))
    soma += item[1] * item[2]
print('-' *20)
print(f'Total a ser pago: {soma}')

 """

#### DICIONARIOS ####

""" game = {'nome': 'Super Mario',
        'desenvolvedora': 'Nintendo',
        'ano': 1990}
print(game)
print(game['nome'])
print(game['desenvolvedora'])
print(game['ano'])
print(game.values())
print(game.items())
for keys, values in game.items():
    print(f'{keys} = {values}')
 """


### LISTAS COM DICIONARIOS DENTRO ###

""" games = []

game1 = {'nome': 'Super Mario',
         'videogame': 'Super Nintendo',
         'ano': 1990}
game2 = {'nome': 'Zelda Ocarina of Time',
         'videogame': 'Nintendo 64',
         'ano': 1999}
game3 = {'nome': 'Pokemon Yellow',
         'videogame': 'Game Boy',
         'ano': 1999}

games = [game1, game2, game3]
print(games)
 """

""" games = {'nome': [], 'videogame': [], 'ano': []}
for i in range(3):
    nome = input('Qual o nome do jogo?')
    videogame = input('Para qual video game ele foi criado?')
    ano = int(input('Qual o ano de lancamento?'))
    games['nome'].append(nome)
    games['videogame'].append(videogame)
    games['ano'].append(ano)
print('-' * 20)
print(games) """

""" s1 = 'Logica de Programacao e Algoritmos'
print(s1.upper())
print(s1.lower())
s1.lower().count('a') """

""" from math import sqrt

print(sqrt(9))
 """

notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]

### a) Encontrar quantos alunos tiraram nota 7
### b) ALTERAR A ultima nota para 4

""" print(notas.count(7)) """
""" notas[-1] = 4
print(notas) """

### c) Encontrar a maior nota
""" print(max(notas)) """

### d) Ordenar a lista de notas.

""" notas.sort()
print(notas) """

### e) A media das notas
""" print(sum(notas) / len(notas)) """

### Exercicio 1 - 
### Escreva um algoritmo que crie uma tupla com 10 palavras. encontre dentro dessa tupla as vogais de cada palavra.
### Faca um print na tela com o nome da palavra e suas respectivas vogais.

""" palavras = ('Mario', 'Luigi', 'Peach', 'Yoshi', 'Bowser')

for palavra in palavras:
    print(f'\nPalavra: {palavra.upper()}. Vogais:')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra.upper(), end= ' ') """


### Crie um jogo de pedra, papel ou tesoura. Voce devera jogar contra o computador. Voce ira sempre escolher uma das opcoes:
### 1- pedra, 2- papel, 3- tesoura.
### O computador ira sempre sortear um numeo de 1 ate 3 para jogar.
### Armazene todos os resultados em uma lista e, no final, apresente o vencedor.
### Encerre o programa ao digitar zero.


""" import random

def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while((x < min) or (x > max)):
        x = int(input(pergunta))
    return x
    
def vencedor (jogador1, jogador2):
    global v1, v2, empate
    if jogador1 == 1:
        if jogador2 == 1:
            empate += 1
        elif jogador2 == 2:
            v2 += 1
        elif jogador2 == 3:
            v1 += 1
    elif jogador1 == 2:
        if jogador2 == 1:
            v1 += 1
        elif jogador2 == 2:
            empate += 1
        elif jogador2 == 3:
            v2 += 1
    elif jogador1 == 3:
        if jogador2 == 1:
            v2 += 1
        elif jogador2 == 2:
            v1 += 1
        elif jogador2 == 3:
            empate += 1

    resultados = [v1, v2, empate]
    return resultados


print('Pedra, Papel ou Tesoura')
print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')
print('0 - SAIR')

jogadas = []
resultados = []
v1 = 0
v2 = 0
empate = 0

while True:
    j1 = valida_int('Escolha sua jogada: ', 0, 3)
    if not j1:
        break
    j2 = random.randint(1,3)
    jogadas.append([j1, j2])
    resultados = vencedor(j1, j2)

for jogada in jogadas:
    for dado in jogada:
        print(dado, end=' ')
    print()

print(f'Numero de vitorias do Jogador1:{resultados[0]}')
print(f'Numero de vitorias do Jogador2:{resultados[1]}')
print(f'Numero de empates:{resultados[2]}') """

### Crie um programa para ler o nome, ano de nascimento e sexo de diferentes pessoas.
### Armaze os dados em um dicionario com lsitas
### Ao encerrar o cadastro, apresente:
### O total de cadastros efetuados
### A media das idades das pessoas
### Uma lista de mulheres com menos de 30 anos
## Uma lista de homens com idade acima da media

""" cadastro = {'nome':[],'Sexo':[], 'Ano':[]}

while True:
    terminar = input('Deseja cadastrar uma pessoa? [S/N]')
    if terminar.upper() in 'N':
        break
    if terminar.upper() not in 'S':
        print('Opcao invalida, tente novamente.')
        continue

    nome = input('Qual o nome?')
    sexo = input('Qual o sexo?')
    ano = int(input('Qual a idade?'))
    cadastro = ['nome'].append(nome)
    cadastro = ['sexo'].append(sexo.upper())
    cadastro = ['ano'].append(ano)

print(cadastro)
 """

### MATCH CASE

### Escreva um algoritmo em Python em que o usuasriop escolhe se ele quer comprar macas, laranjas ou bananas. 
### Devera ser apresentado, na tela, um menu com a opcao 1 para maca, 2 para laranja e 3 para banana.
### Depois de escolhida a fruta, deve-se digitar quantas unidades se quer comprar. O algoritmo deve calcular o preco total a pagar,
#### pelo produto escolhido e mostra-lo na tela.
### Considere que uma maca custa R$ 2.30, uma maca: R$ 3.60 e uma banana R$ 1.85

### COM ELIF

""" print('Escolhe oq ue deseja comprar: ')
print('1 - Maca')
print('2 - Laranja')
print('3 - Banana')
produto = int(input('Qual a sua escolha?'))
qtd = int(input('Quantas unidades?'))

if (produto == 1):
    pagar = qtd * 2.3
    print(f'Voce comprou {qtd} macas. Total a pagar: {pagar}')

elif (produto == 2):
    pagar = qtd * 3.6
    print(f'Voce comprou {qtd} laranjas. Total a pagar: {pagar}')

elif (produto == 3):
    pagar = qtd * 1.85
    print(f'Voce comprou {qtd} bananas. Total a pagar: {pagar}')    

else:
    print('Produto inexsitente.')

 """

### MATCH CASE

""" print('Escolhe oq ue deseja comprar: ')
print('1 - Maca')
print('2 - Laranja')
print('3 - Banana')
produto = int(input('Qual a sua escolha?'))
qtd = int(input('Quantas unidades?'))

match (produto):
    case 1:
        pagar = qtd * 2.3
        print(f'Voce comprou {qtd} macas. Total a pagar: {pagar}')

match (produto):
    case 2:
        pagar = qtd * 3.6
        print(f'Voce comprou {qtd} laranjas. Total a pagar: {pagar}')

match (produto):
    case 3:
        pagar = qtd * 1.85
        print(f'Voce comprou {qtd} bananas. Total a pagar: {pagar}')    

    case _:
        print('Produto inexsitente.') """


#### Match Case chegagem de dados

def checagem_tipo(dado):
    match dado:
        case str(dado):
            print('String:', dado)
        case int(dado):
            print('Inteiro:', dado)
        case float(dado):
            print('Float:', dado)
        case _:
            print('Tipo desconhecido de dado.')

dados = ['Python', 42, 3.14, 23, 'C']

for dado in dados:
    checagem_tipo(dado)



