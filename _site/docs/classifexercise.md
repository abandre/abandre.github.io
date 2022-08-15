##  Exercício: Autenticação de Usuário


**Objetivo:** Desenvolver um programa de Machine Learning para autenticação de usuário através da biometria por dinâmica de digitação.


## Introdução

A dinâmica de digitação de senhas é um estudo para identificar se as pessoas podem ser distinguidas por seus ritmos de digitação, da mesma forma que a caligrafia é usada para identificar o autor de um texto escrito. As aplicações possíveis incluem atuar como uma impressão digital eletrônica ou em um mecanismo de controle de acesso. Uma impressão digital conectaria uma pessoa a um crime baseado em computador da mesma maneira que uma impressão digital física conecta uma pessoa à cena de um crime físico. O controle de acesso pode incorporar a dinâmica de pressionamento de tecla, exigindo que um usuário legítimo digite uma senha com o ritmo correto e autenticando continuamente esse usuário enquanto ele digita no teclado.

## Como os dados foram coletados

Foi construído um aparelho de coleta de dados de pressionamento de tecla que consiste em: (1) um laptop executando o Windows XP; (2) um aplicativo de software para apresentar estímulos aos sujeitos e para registrar suas teclas; e (3) um temporizador de referência externa para registrar a hora dessas teclas. O software apresenta ao usuário a senha a ser digitada. Conforme o usuário digita a senha, ela é verificada quanto à exatidão. Se o usuário cometer um erro tipográfico, o aplicativo solicitará que o usuário redigite a senha. Dessa forma, são gravados os timestamps de data/hora para 50 senhas digitadas corretamente em cada sessão.

Sempre que o usuário pressiona ou libera uma tecla, o aplicativo de software registra o evento (ou seja, keydown ou keyup), o nome da tecla envolvida e o timestamp de data/hora para o momento em que o evento de pressionamento de tecla ocorreu. Um relógio de referência externa foi usado para gerar os timestamps de data/hora altamente precisos. O relógio de referência demonstrou ser preciso em ± 200 microssegundos (usando um gerador de função para simular pressionamentos de tecla em intervalos fixos).

Foram recrutados 51 sujeitos (digitadores) de dentro de uma comunidade universitária; todos os sujeitos completaram totalmente o estudo - não descartamos nenhum sujeito. Todos os sujeitos digitaram a mesma senha e cada sujeito digitou a senha 400 vezes em 8 sessões (50 repetições por sessão). Eles esperaram pelo menos um dia entre as sessões, para capturar algumas das variações do dia a dia da digitação de cada sujeito. A senha **(.tie5Roanl)** foi escolhida para representar uma senha forte de 10 caracteres.

Os registros brutos de todos os pressionamentos de tecla e os timestamps de data/hora dos sujeitos foram analisados ​​para criar uma tabela de tempo de senha. A tabela de tempo de senha codifica os recursos de tempo para cada uma das 400 senhas que cada assunto digitou.

## Arquivo de Dados

Arquivo contendo as informações de digitação: <a href="KSPasswordData.csv" target="_blank">KSPasswordData.csv</a>

### Bibliotecas

Para a implementação do exercício você muito provavelmente irá precisar instalar as seguintes bibliotecas em python:

 - joblib
 - numpy
 - sklearn
 - pandas
 
### Exercício

Selecionar um algoritmo qualquer de classificação e escrever um código simples em python que realize as seguintes operações:

- Carregue os dados da planilha csv
- Divida os dados em conjuntos de treino/teste, na proporção de 20%
- Treine um modelo de um classificador a sua escolha
- Calcule a taxa de acerto resultante do modelo treinado
- Salve o modelo para uso posterior

<!-- , calculados na página <a href="https://keystroke-dash.herokuapp.com/" target="_blank">https://keystroke-dash.herokuapp.com/</a>. -->

### Conteúdo original

<a href="http://www.cs.cmu.edu/~keystroke/" target="_blank">http://www.cs.cmu.edu/~keystroke/</a>