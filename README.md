# Curso de Python 3 do Básico Ao Avançado (com projetos reais)

## Função print

Exemplo com separadores:

No exemplo abaixo o separador será o default (espaço) e no final da linha terá o '#'

`print(12, 34, 1011, sep="", end='#')`

No exemplo abaixo o separador será o hífem e no final da linha terá uma quebra de linha

`print(56, 78, sep='-', end='\n')`


## Tipos de dados

str -> Tudo que está entre aspas duplas ou aspas simples são strings. Ex `"edilson"`

int -> O tipo int representa qualquer número inteiro  positivo ou negativo. int sem sinal é considerado positivo. Ex 10

float -> Número com ponto flutuante. POde ser negativo ou positivo. Ex -10

bool -> Tipo booleano. Retorna sempre True ou False. Ex `10 == 10` neste caso será retornado True

A função type mostra o tipo. Ex `print(type('Qualquer coisa'))`

# Coerção de tipos

É o ato de converter um tipo de dados em outro tipo. Ex `int('1')`. Este exemplo está convertendo o dado de string para inteiro.

# Variáveis

Variáveis são usadas para salvar algo na memória do computador. Para atribuir um valor à uma varável devemos usar o =. Ex: `nome = "Edilson"`

Por padrão (segundo o PEP8) o nome das variáveis deve ser iniciado com letra minúscula que pode ser seguido de um número. Também pode-se utilizar o underline. Ex: `idade_pessoa = 30`

# Operadores aritiméticos

```
adicao = 10 + 10
print('Adição', adicao)

subtracao = 10 - 5
print('Subtração', subtracao)

multiplicacao = 10 * 10
print('Multiplicação', multiplicacao)

divisao = 10 / 3  # float
print('Divisão', divisao)

divisao_inteira = 10 // 3
print('Divisão inteira', divisao_inteira)

exponenciacao = 2 ** 10
print('Exponenciação', exponenciacao)

modulo = 55 % 2  # resto da divisão
print('Módulo', modulo)
```

# Precedência entre operadores aritiméticos

Num cáuculo aritimético, há uma ordem que é respeitada para a resolução do problema:

1. O que está entre parênteses () 
2. Exponenciação **
3. Multiplicação *, divisão /,  divisão inteira //, módulo de divisão %
4. Soma +, subtração -

Veja o exemplo a seguir: `conta = 1 + (2 * 8) / 2`

Neste caso o resultado será 9. Eis a solução:

O que está entre parêntese deve ser resolvido primeiro: 2 * 8 = 16
Em seguida deve ser resolvido a divisão = 16 / 2 = 8
E por fim resolve-se a soma: 8 + 1 = 9

# Introdução a formatação de strings

##  f-strings 

No python, é possível formatar strings de diversas maneiras. Uma delas é com f-strings
Trata-se de invocar o valor de uma variável dentro de uma string. A sintaxe se resume em colocar a letra f no início de uma string e o nome da variável entre chaves. Ex: f"Sua string {sua_variavel}"

```
nome = "Edilson Junior"
print(f"Meu nome é {nome}")
```
Uma coisa interessante: se usarmos o sinal de igual dentro de uma f-string, é impresso o nome da variável junto com o seu valor. EX:

```
nome = "Edilson"
print(f"{nome=}")

#Saida:
nome='Edilson'
```
## Método format

Também é possível formatar strings utilizando o método .format. Veja o exemplo:

```
nome = "Edilson Junior"
print("Meu nome é {}".format(nome))
```

# Função input - Coletar dados do usuário

A função input é utilizada para coletar dados digitados pelo usuário. Estes dados podem ser salvos em variáveis. Ex: `nome = input("Digite seu nome: ")`

# Estruturas condicionais - IF / ELIF / ELSE

As estruturas condicionais servem para executar trechos de códigos de acordo com a condição determinada. Tais estruturas utilizam os operadores boleanos, `True / False` para criar uma condição. Veja o exemplo abaixo:

```
nome = "edilson"
if nome == "edilson":
    print("Seu nome é Edilson")
elif nome == "joao"
    print("Seu nome é Joao")
else:
print("Seu nome não é Edilson nem João")
```
No exemplo acima a condição é verdadeira (True) e o código que será executado será o `print("Seu nome é Edilson")`.

# Operadores de comparação (relacionais) em Python

```
Operadores de comparação (relacionais)
OP      Significado         Exemplo (True)
>       maior               2 > 1
>=      maior ou igual      2 >= 2
<       menor               1 < 2
<=      menor ou igual      2 <= 2
==      igual               'a' == 'a'
!=      diferente           'a' != 'b'
```

## Interessante...

Há a possibilidade de utilizarmos no python o modo interativo que carrega as variáveis de um arquivo .py (módulo) e pode-se ficar chamando essas variáveis no próprio shell do python que será carregado. EX: ` python3 -i arquivo.py`

# Operador Lógico "and", "or" e "not"

## and

Todas as condições precisam ser verdadeiras.
Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor falso.

São considerados falso `0, 0.0, '' e False`<br>
Também existe o tipo `None` que é usado para representar um não valor<br>
Exemplo:
```
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')
```
## or

Qualquer condição verdadeira avalia toda a expressão como verdadeira.
Se qualquer valor for considerado verdadeiro, a expressão inteira será avaliada naquele valor.

```
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

Avaliação de curto circuito
senha = input('Senha: ') or 'Sem senha'
print(senha)
```
## not

Usado para inverter expressões
not True = False
not False = True
```
senha = input('Senha: ')
print(not True)  # False
print(not False)  # True
```
## in, not in

Strings são iteráveis
```
 0 1 2 3 4 5 6
 E d i l s o n
-7-6-5-4-3-2-1
```
```
nome = 'Edilson'
pint(nome[2])
print(nome[-4])
print('dil' in nome)
print('zero' in nome)
print(10 * '-')
print('vio' not in nome)
print('zero' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
```

# Interpolação de String com %

Interpolação básica de strings

s - string <br>
d e i - int <br>
f - float <br>
x e X - Hexadecimal (ABCDEF0123456789)
```
nome = 'Edilson'
preco = 1000.925
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %08X' % (1500, 1500))
```
# Formatação de String com f-strings
f-strings é a maneira mais nova, até o momento, e mais fácil de formatar uma string no python. Veja o exemplo:
```
variavel = 'ABC'
print(f'O valor da variável é {variavel}')
```
Há diversos recursos que envolvem o f-strings. Alguns desses recursos são muito interessantes.

Por exemplo: para imprimir um número quebrado (float) com apenas duas casas decimais podemos utilizar `f"{100.21337:.2f}"`

Outros recursos:

Converer para Hexadecimal (x para minúsculo e X para maiúsculo): `f"{variavel:X}"`

Centralizar a string (><^)(quantidade): `f"{variavel:^10}"`

Posicionar a string à esquerda (>) - `f"{variavel:>10}"`

Posicionar a string à direita (<) - `f"{variavel:<10}"`


Conversion flags (será explicado depois dentro do curso)- 


`!r` Invoca o método `__repr__` 

`!s` Invoca o método `__str__` 

`!a` Invoca o método `__ascii__` 

PAD - Colocar uma largura fixa na string caso ela não atinja a quantidade de caracteres que é pedido. EX: `print(f"{variavel: >10}")`
# Fatiamento de Strings

No python há a possibilidade de fatiar uma string utilizando o seguinte padrão: [inicio:fim:passo]. EX: 
```
variavel = 'Olá mundo'
print(variavel[::-1])
```
# Introdução ao try e except

O try except é utilizado para tratamento de erros. Basicamente, este recurso captura uma exceção caso ocorra um erro. Ex:

```
numero_str = input(
    'Vou dobrar o número que vc digitar: '
)

try:
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')
```

# Constantes e complexidade de código

Constante = Variável que não vai mudar no código. No python uma constante pode ser alterada, diferente de outras linguagens que isto não é possível. (todas as letras maiúsculas)

É bom evitar a complexidade do código. Por exemplo: Muitas condições no mesmo IF não é bom; uma função com muito código não é bom, etc.

É muito interessante colocar as confições de um IF em variáveis para o código ficar mais limpo. EX:
```
#Verifica se a soma de um número é maior que 10

a = 2
b = 3
soma = (a + b) > 10

if soma:
    print("A soma é maior que 10")
else:
    print("A soma é menor que 10")

```

# A identidade (ID) do valor que está na memória

Cada variável na memória do computador recebe um ID, identidade, que pode ser utilizada pelo python para inúmeras situações. Para ver o ID de uma variável use a função id(). EX:

```
variavel = 'edilson'
print(id(variavel))
```
Se o valor da variável for igual, o python irá atribuir o mesmo ID para as duas variáveis.

#  Flags, is, is not e None

Flag (Bandeira) - Marcar um local

None = Não valor

is e is not = é ou não é (tipo, valor, identidade)

id = Identidade

EX:
```
condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')


if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')
```

# Tipos built-in, documentação, tipo imutáveis, métodos de string

Documentação do Python: https://docs.python.org/pt-br/3/

É interessante salientar que string, int, float, bool são imutáveis no python. Caso seja necessário mudar um valor destes tipos acima, temos que criar uma nova variável e fazer a alteração.

#  While e break - Estrutura de repetição (Parte 1)

O `While` executa uma condição quando uma ação for verdadeira. Temos que tomar cuidado com o loop infinito que acontece quando não há mudança na condição para falsa. O `break`  para o loop e continua a execução do código a baixo. Ex:

```
condicao = True

while condicao:
    nome = input('Qual o seu nome: ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break

print('Acabou')

```

# while - Condição em detalhes

É interessante ter sempre um contador para iterar com o while para o loop ter um fim. EX:

```
contador = 0

while contador <= 10:
    contador = contador + 1
    print(contador)

print('Acabou')
```

#  Operadores de atribuição com operadores aritméticos

Abaixo estão os operadores de atribuição:

+= SOMA

-= SUBTRAÇÃO

*= MULTIPLICAÇÂO    

/= DIVISÃO

//= DIVISÃO INTEIRA

**= POTENCIAÇÃO

%= MÓDULO

```
contador = 10

contador += 5
print(contador)
```

# while + continue - pulando alguma repetição

Dentro do while, o `continue` serve para pular aquela iteração. EX:

```
contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        continue

    print(contador)
```
No exemplo acima o loop não imprimiu o número 6, pois justamente nesta iteração do loop tinha o `continue`

# while aninhado (laços internos)

