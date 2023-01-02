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

## Método format

Também é possível formatar strings utilizando o método .format. Veja o exemplo:

```
nome = "Edilson Junior"
print("Meu nome é {}".format(nome))
```

