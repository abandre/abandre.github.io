% Processamento de Imagens com Python
% Amaury Bosso André
% &copy; 2019 Amaury Bosso André

<!-- Descrição
A completar
 -->


# Introdução

Como sabemos, o ser humano é dotado de cinco sentidos: audição, olfato, paladar, tato e visão. Esses sentidos são fundamentais para percebermos o mundo ao nosso redor, e o fazemos através de variados estímulos: ondas sonoras (audição), temperatura ou forma dos objetos (tato), cheiros e gostos (olfato e paladar), mas principamente através de estímulos luminosos (visão). 

Uma imagem é formada através da distribuição da energia luminosa em sua posição espacial. Na figura a seguir, podemos observar que a iluminação (solar neste exemplo), distribui sua energia sobre o objeto. Parte dessa energia é absorvida, parte dela é transmitida, dependendo da opacidade do objeto, e parte é refletida. Essa energia luminosa refletida que é captada pelo nosso olho ou por nossas câmeras.

![](data/luz.png)

No ser humano, o sentido mais poderoso é o da visão, cujo órgão responsável é o olho. Podemos ver que os raios luminosos incidem sobre a córnea, onde são refratados. O cristalino converge os raios incidentes diretamente na retina, que é uma das membranas que formam o globo ocular. É na retina que se concentram as células da visão, que convertem a intensidade luminosa incidida em impulsos elétricos. Esses impulsos elétricos são então transmitidos via o nervo óptico até o nosso cérebro.

![](data/olho.png)

Similar ao processo de formação da imagem em nosso olho, o dispositivo de aquisição mais utilizado atualmente é a câmera CCD (*Charge Couple Device*). Ela consiste em uma matriz de células semicondutoras fotossensíveis que atuam como capacitores, armazenando carga elétrica proporcional a energia luminosa incidente.

Uma câmera CCD monocromática possui um conjunto de lentes que focalizam a imagem sobre a área fotossensível do CCD. Para imagens coloridas, é necessário um conjunto de prismas e filtros de cor, que decompõem a energia luminosa incidida em suas componentes R (*red*: vermelho), G (*green*: verde) e B (*blue*: azul). Cada uma dessas componentes é capturada por uma célula independente do CCD.

![](data/ccd.png)

## Manipulando Imagens em Python

Neste capítulo iremos abordar os primeiros passos para abrir, manipular e salvar imagens de forma simples em [Python 3](https://www.python.org/downloads/release/python-350/). Para isso usaremos a biblioteca [*Pillow*](https://pillow.readthedocs.io/en/stable/index.html). Ela é um fork da biblioteca PIL (*Python Image Library*), que é a biblioteca básica de manipulação de imagens com suporte a Python 3.

Caso seja necessário fazer a instalação da biblioteca no seu sistema, é possível fazer através do comando:

```bash
$ pip install Pillow
```

A classe `Image` é implementada na biblioteca e definida no módulo de mesmo nome. Com ela, é possível criar instâncias de imagens de duas formas distintas: carregando imagens de arquivos, processando outras imagens, ou criando imagens do zero.

Para abrir uma imagem, pré-existente, usamos o método `open()` do módulo Imagem. Mas pra isso, é necessário importar o módulo em nosso script python, como a seguir:

```python
>>> from PIL import Image
>>> img = Image.open("teste.png")
```
O código irá abrir a imagem "teste.png", que deve estar salva no mesmo diretório em que o terminal de python está executando. Caso a imagem esteja em outro diretório, deve-se passar como parâmetro do método `open()` o caminho completo da imagem no sistema.

Note que não é necessário informar o tipo da imagem, a biblioteca determina automaticamente qual o formato do arquivo, baseado somente em seu conteúdo.

Executado o código anterior, a imagem do arquivo "teste.png" será carregado e o objeto na memória será atribuido a variável `img` do código. Esse objeto possui alguns atributos interessantes, entre eles:

- **.format** - o formato da imagem original.
- **.mode** - uma string que especifica a codificação de cores dos pixels usados na imagem, podendo ser "L", "RGB", ou "CMYK", entre outros. 
- **.size** - o tamanho da imagem em pixels. É retornado um vetor com os valores de largura e altura respectivamente.
- **.width** - a largura da imagem em pixels.
- **.height** - a altura da imagem em pixels.

Dessa forma, podemos calcular a resolução (que corresponde ao número de pixels da imagem), através da multiplicação do número de linhas pelo número de colunas:

```python
>>> from PIL import Image
>>> img = Image.open("teste.png")
>>> print(img.format)
PNG
>>> print(img.mode)
RGB
>>> w,h = img.size
>>> print("Resolucao: "+str(w*h)+" pixels")
Resolucao: 202500 pixels
```

Para salvar uma imagem, usa-se o método `save()`, assim como no exemplo a seguir:

```python
>>> img.save("teste2.jpg")
```

Observe que assim como no método `load()` é necessário informar apenas o nome do arquivo. Neste caso, informei o nome com a extensão `.jpg` e automaticamente a biblioteca irá converter meu objeto `img` para o formato desejado e salvá-lo no diretório corrente. Se quisesse salvar em outro diretório, bastaria passar o caminho completo do diretório no sistema.

# Conceitos Fundamentais

Os primeiros conceitos a serem abordados em processamento de imagens é com relação a representação de imagens em si. Para isso abordaremos os seguintes assuntos:

- amostragem
- quantificação
- representação de cores

## Amostragem

Como definido na introdução, a imagem é formada na retina do nosso olho, ou no CCD de uma câmera digital, através da captação da informação luminosa refletida do objeto original.

A amostragem está diretamente relacionada com a quantidade de células fotossensíveis presente nos dispositivos de captação. A grandeza diretamente relacionada com a amostragem de uma imagem é a **resolução**.

A **resolução** da imagem, nada mais é que o número total de células utilizadas na grade de amostragem de uma determinada imagem. Ou seja, para a grade de `64x64` pontos, temos uma resolução de `4096` pontos, por exemplo.

Quanto maior a resolução da imagem, mais células teremos na grade de amostragem e mais detalhes seremos capazes de observar da imagem real. Ou seja, o processo de amostragem está diretamente ligado com a quantidade de informação que se deseja guardar. Quanto maior a amostragem, mais detalhes teremos e consequentemente maior será o espaço necessário para o armazenamento. 

Para exemplificar o processo de amostragem, vamos imaginar a imagem a seguir, como sendo a imagem real, e posteriormente iremos usar grids de diferentes tamanhos para reamostragem, simulando câmeras com cada vez menos resolução.

```python
from PIL import Image

img = Image.open("orig.png")
w,h = img.size
print("Size: w="+str(w)+" h="+str(h))
print("Resolucao: "+str(w*h)+" pixels")

down = img.resize((64,64))
up = down.resize((w,h))
up.save("orig-64.png")

down = img.resize((128,128))
up = down.resize((w,h))
up.save("orig-128.png")

down = img.resize((256,256))
up = down.resize((w,h))
up.save("orig-256.png")
```

![](data/orig-amostragem.png)



## Quantificação

Faz parte do processo de amostragem de uma imagem, a quantificação do nível da intensidade de luz incidindo sobre uma determinada célula da grade, como visto na seção anterior. 

Cada célula amostra uma média da intensidade de luz que nela incide. Porém, esse nível pode variar infinitamente entre preto (ausência completa de luz) e o branco (intensidade máxima de luz). No entanto, para o armazenamento de imagens digitais, temos de quantificar essa luminosidade em um número finito de níveis. Para exemplificar, veja a função unidimensional `f(t)`:
 

A cada passo amostrado da função, representado por $\Delta t$, é preciso quantizar o seu valor. Na figura, são utilizados 6 níveis de quantização. Dessa forma, o valor médio da função `f(t)`, dentro do intervalo delta, é arredondado para o nível mais próximo. Assim, a função amostrada e quantizada nos 6 níveis possíveis, pode ser vista na figura. 

## Cores

# Processamento Ponto a Ponto

## Histograma

## Mapeamento Funcional

# Convolução

## Filtro Box

## Filtro Gaussiano

## Filtro Laplaciano 

## Detecção de Bordas

# Frequência

## Filtro Passa Baixa

## Filtro Passa Alta

# Conclusão