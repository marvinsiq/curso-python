Projetos de exemplo de introdução a linguagem Python

* [Documentação - Python 3.8](https://docs.python.org/pt-br/3.8/index.html)
* [Tutorial](https://docs.python.org/pt-br/3.8/tutorial/index.html)

# Guia Rápido
## For

```python
for rodada in range(1,5):
    print(rodada)
```

Podemos definir um step, que é o intervalo entre os elementos, por padrão o step é 1. 
Definimos-o passando um terceiro parâmetro para a função:

```python
for rodada in range(1,10,2):
    print(rodada)
```

Podemos passar os valor manualmente:

```python
for rodada in [1,2,3,4,5]:
    print(rodada)
```


## String Interpolation

```python
rodada = 1
total_de_tentativas = 3
print("Tentativa {} de {}".format(rodada, total_de_tentativas))
```
## Definindo Funções

```python
def nome_da_funcao():
    # todo o código identado faz parte da função
    print("aprendendo funções")
```

## Importando um módulo (arquivo)

```python
# arquivo a.py
def executa():
    print("Executando a")
```

```python
# arquivo b.py
def executa():
    print("Executando b")
```

```python
# principal.py

import a
import b
```

## Importando um módulo dentro de um diretório
```python
from diretorio import arquivo
```

## Diferenciando um arquivo executado de um importado

*forca.py*
```python
def jogar():
    # código omitido

if (__name__ == "__main__"):
    jogar()
```