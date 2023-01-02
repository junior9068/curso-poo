# Classes em Python

Classes proporcionam uma forma de organizar dados e funcionalidades juntos. Criar uma nova classe cria um novo “tipo” de objeto, permitindo que novas “instâncias” desse tipo sejam produzidas. Cada instância da classe pode ter atributos anexados a ela, para manter seu estado. Instâncias da classe também podem ter métodos (definidos pela classe) para modificar seu estado.

## Definição da uma classe

A forma mais simples de definir uma classe é:

    class NomeDaClasse:
        <statement-1>
        .
        .
        .
        <statement-N>

## Objetos de Classe

Objetos classe suportam dois tipos de operações: referências a atributos e instanciação.

Referências a atributos de classe utilizam a sintaxe padrão utilizada para quaisquer referências a atributos em Python: obj.nome. Nomes de atributos válidos são todos os nomes presentes dentro do espaço de nomes da classe, quando o objeto classe foi criado. Portanto, se a definição de classe tem esta forma:

    class MinhaClasse:
        """Aqui fica a documentação da classe"""
        i = 12345

        def f(self):
            return 'hello world'

    a = MinhaClasse()

MinhaClasse.i e MinhaClasse.f são referências a atributo válidas, retornando, respectivamente, um inteiro e um objeto da função. Atributos de classe podem receber valores, pode-se modificar o valor de MyClass.i num atribuição .__doc__ também é um atributo válido da classe, retornando a documentação associada: "A simple example class".

Para instanciar uma classe, usa-se a mesma sintaxe de invocar uma função. Exemplo:

    a = MinhaClasse()

A operação de instanciação (“invocar” um objeto classe) cria um objeto vazio. Muitas classes preferem criar novos objetos com um estado inicial predeterminado. 

## Método Construtor

Método especial para inicializar um objeto instanciado. Este método tem o poder de criar novos objetos com um estado inicial predeterminado.

Sintaxe:

    def __init__(self, [parâmetros])
        código do método construtor


Quando a classe inclui o método (que é uma função dentro da classe) `__init__`, ele é automaticamente invocado quando a classe é iniciada.

## O identificador self

Sintaticamente, o parâmetro `self` identifica a instância sobre a qual um método é invocado. Ou seja, é uma referência à instância atual da classe (objeto).

É usado para acessar os membros que pertencem à classe em si

Deve ser sempre o primeiro parâmetro usado na definição de um método. 

Sintaxe:

    class Gato:
        """Classe para trabalhar com gatos"""
        def __init__(self, nome):
            self.nome = nome
            print(f"Seu gato se chama {self.nome}")


    nome_gato = input("Nome do gato: ")
    g1 = Gato(nome_gato)

## Método

Lógica contida em uma classe para atribuir comportamentos (sequência de comandos), identificada por um nome. É similar a uma função. É recomendado que um método execute apenas uma operação.

Quando um método é executado dizemos que ele é invocado (chamado)

Exemplos de métodos: Na classe Pessoa pode ter os métodos: nascer(), comer() e morrer()

Sintaxe:

    def nome_do_metodo(self, [parametros]):
        instruções
        return = valor
### Métodos Utilitários

São métodos usados apenas pela classe e não faz parte da interface pública usada pelo código do cliente.

Devem preferencialmente ser nomeadas com um underscore como prefixo.

Sintaxe:

    def _nome_do_metodo(self):
        instruções
        return = valor

## Atributos ou propriedades

É uma característica particular de uma ocorrencia de uma classe, por exemplo o nome ou a altura de uma pessoa

Existem dois tipod principais de atributos ou variáveis:
* Variável de classe: Pertence à classe em si
* Variável de Instância: Pertence a cada objeto individualmente

## Objeto

Objeto é uma ocorrência específica de uma classe - "Instância de classe". O Objeto representa entidades do mundo real como carros, pessoas, contas correntes e outros conceitos como gráficos (círculos, quadrados, cones, esferas, etc)

O objeto tem características próprias (atributos) e executa ações (métodos), provenientes da classe que originou o objeto.

Sintaxe:

    nomeObjeto = NomeClasse(parametros)


## Métodos Getter Setter

Estes métodos servem para controlar os estados dos objetos da classe. Lembrando que são métodos criados dentro da pŕopria classe e que devem ser criados por boas práticas.

Método setter: Usado para alterar ou inserir valores nos membros de dados. Sintaxe:

    def get_valor(self):
        """ Método getter para retornar o valor do atributo x"""
        return self.x



Método getter: Usados para recuperar (ler) valores armazenados nos objetos: Sintaxe:


    def set_valor(self, v):
        """ Método setter para atribuir um novo o valor ao atributo x"""
        self.x = v

Como regra, um objeto só pode ter seus dados manipulados com o uso de setters e getters especificados




