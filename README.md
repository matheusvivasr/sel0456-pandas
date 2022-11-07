# SEL0456(2022) - Pandas

## Índice
1. [Data Types](#DT)
    1. [Series](#Series)
    2. [DataFrame](#DataFrame)
2. [Git](#git)
    1. [Manipulação de Repositório](#repository)
    2. [Manipulação dos Ramos](#branch)
    3. [Fusão dos Ramos](#merge)



## <a id = "DT"></a> Pandas

Pandas, por padrão quase universal, é importada como `pd`

```
import pandas as pd
```


### <a id = "Series"></a> Series

Uma `Serie` é uma lista com apenas uma coluna e terá o tipo `pandas.core.series.Series`.
Por padrão é indexada a partir do 0 até o n-1 de uma série com n elementos, mas o index pode ser persinalizado se passado como segundo argumento.

```
a = pd.Series([1,2,3,4,5],index=["a","b","c","d","e"])
```

O argumento da série também pode ser um dicionário;
Ao passar como dicionário, a ordem pode ser rearrumada(inclusive inserindo itens) ao definir os indexs.

```
dict = {"a":1,"b":2,"c":3,"d":4,"e":5}
b = pd.Series(dict, index=["c","b","x","a","d","e"])
```


Os elementos podem ser acessados por index, posição ou selecionando uma parte da série.
```
a[2]    #terceiro item                      (posição)

a["c"]  #item de index "c"                  (index)

a[:2]   #dois primeiros elementos de 'a'    (Parte superior da lista )
a[-2:]  #dois últimos elementos de 'a'      (      inferior          )
```



### <a id = "DataFrame"></a> Função Recursiva

Foi implementada uma função `fibo()` que funciona analogamente.



## <a id = "git"></a> Git
A ferramenta de versionamento de código


###  <a id = "repository"></a> Manipulação de Repositório

Foram utilizados os seguintes comandos para o manuseio das versões em um único ramo do código:
```
$git status
$git add .
$git commit -a
$git push
```
Ao usar `status` verificamos se algum arquivo foi alterado, quais arquivos e uma breve descrição da alteração.

Usando `add` você escolhe quais arquivos vão ser adicionados a essa nova versão a ser salva. O ponto colocado logo depois siginifica que serão todos os arquivos que sofreram alteração.

Ao usar o `commit` foi necessário escrever um comentário sobre as atualizações feitas naquela determinada versão ou `snapshot`.

Ao usar o `push` foi necessária uma autenticação da minha conta do Github.


### <a id = "branch"></a> Manipulação dos Ramos

Para a criação de um novo ramo ou `branch` foi utilizado o comando:
```
$git checkout -b <nova_branch>
```

Que além de criar um novo ramo com nome `nova_branch`, já me colocou nela, ou seja, quaisquer alterações nos arquivos que eu fizer a seguir, serão salvas e versionadas nessa `nova_branch`, um ramo paralelo a main mas que não interfere em seu andamento.

Para retornar ao ramo `main`(que é o nome convencionado para o ramo principal), basta usar o comando:
```
$git checkout main
```

Sendo necessária essa troca de ramos, basta trocar o nome `main` pelo nome do ramo que você criou:
```
$git checkout nova_branch
```


### <a id = "merge"></a> Fusão dos Ramos
Para fundir o ramo `main` com o ramo `nova_branch` você deve conferir se está no ramo `main` e então usar o comando merge:

```
$git checkout main
$git merge nova_branch
```
Se não houverem arquivos conflituosos, a fusão terá ocorrido com sucesso.