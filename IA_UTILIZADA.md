# 🤖 IA utilizada e prompts do projeto

Este documento registra as inteligências artificiais utilizadas no desenvolvimento do projeto, bem como os prompts principais empregados para a construção do artigo científico e do código da calculadora epidemiológica baseada no modelo SEIR.

---

## 🧠 IA utilizadas

* ChatGPT (OpenAI)
* Consensus (para busca e apoio de referências científicas)

---

## 📚 Prompt utilizado no Consensus (referências do artigo)

> Modelar doenças infectocontagiosas e seu espalhamento com o modelo SEIR

---

## 💬 Prompt utilizado no ChatGPT para elaboração do artigo

O artigo sobre um código em linguagem de programação à sua escolha, para modelar doenças infectocontagiosas e seu espalhamento deve conter:

* Resumo / Abstract
* Introdução
* Objetivo
* Fundamentação teórica
* Modelo matemático
* Metodologia
* Resultados
* Conclusão
* Referências

---

### 📝 Resumo fornecido

Este estudo evidencia o desenvolvimento de um programa capaz de produzir uma predição epidemiológica. Com a implementação baseada no modelo SEIR, são feitas projeções de como uma doença infecciosa se espalha a partir dos parâmetros inseridos e cálculos realizados com equações diferenciais.

O sistema exibe como resultado a visualização em gráfico de colunas sobrepostas, representando as populações suscetíveis, expostas, infectadas e recuperadas ao longo do tempo.

Os resultados mostram a aplicabilidade do programa para previsão de cenários epidemiológicos e mensuração do grau de dispersão de doenças infecciosas.

**Abstract:** versão em inglês do resumo, mantendo o mesmo significado.

---

### 📖 Introdução (diretriz do prompt)

Modelos epidemiológicos são propostos para analisar a propagação de doenças infecciosas dentro de uma população. Um dos modelos compartimentais é o modelo SEIR.

Neste modelo, os indivíduos são divididos em quatro compartimentos:

* Suscetíveis (S)
* Expostos (E)
* Infectados (I)
* Recuperados (R)

*A introdução também deve destacar a importância da modelagem matemática para previsão e controle de epidemias.

---

### 🎯 Objetivo

Desenvolver uma calculadora epidemiológica baseada no modelo SEIR, capaz de simular o espalhamento de doenças infecciosas a partir de parâmetros definidos pelo usuário, permitindo análise de cenários epidemiológicos.

---

### 📘 Fundamentação teórica (paráfrase)
Deve parafrasear:

O modelo SEIR (Suscetíveis – Expostos – Infecciosos – Recuperados) é um dos principais modelos matemáticos para descrever o espalhamento de doenças com período de incubação, como COVID-19 e influenza.

A população é dividida em quatro compartimentos: S, E, I e R, com transições sucessivas S → E → I → R.

A dinâmica é descrita por equações diferenciais com os seguintes parâmetros:

* β: taxa de infecção (contato eficaz)
* σ (ou ω): taxa de progressão de E para I (fim da incubação)
* γ: taxa de recuperação

Outros parâmetros importantes:

* R₀: 
* Tinf: 
* Tinc:


Relações utilizadas:

* β = R₀ / Tinf
* σ = 1 / Tinc
* γ = 1 / Tinf

*Explique cada sigla do SEIR; explique os parâmetros R₀, Tinf e Tinc; e considere a redução percentual da transmissão, representando medidas de controle ou mitigação.

---

### 📐 Equações diferenciais do modelo fornecidas

O sistema é descrito por:

* dS/dt = −βSI/N
* dE/dt = βSI/N − σE
* dI/dt = σE − γI
* dR/dt = γI

---

### ⚙️ Metodologia

O projeto foi desenvolvido em linguagem Python, utilizando a biblioteca Matplotlib para geração de gráficos de barras sobrepostas que representam a evolução do espalhamento da doença.

Apesar do modelo ser baseado em equações diferenciais contínuas, a implementação computacional utiliza discretização temporal, onde o sistema é calculado em passos (um passo por dia).

Quanto maior o número de passos, mais próximo o modelo se torna de uma solução contínua.

A inteligência artificial também foi utilizada para auxiliar na criação, compreensão e depuração do código e na interpretação dos resultados gráficos.

---

### 📊 Resultados

Foi possível implementar computacionalmente o modelo SEIR, permitindo simular o espalhamento epidemiológico a partir de parâmetros definidos pelo usuário.

O sistema possibilita acompanhar a transição da população entre os estados S, E, I e R ao longo do tempo.

O modelo adaptado para o ambiente computacional fornece uma representação aproximada e útil da dinâmica real de uma epidemia.

---

### ✅ Conclusão

Apesar das limitações decorrentes da discretização temporal, das simplificações do modelo e da imprevisibilidade real de doenças, o sistema desenvolvido segue corretamente o modelo SEIR.

Os resultados obtidos são satisfatórios para fins educacionais, contribuindo para o entendimento e análise de cenários epidemiológicos.

---

### 💬 Mensagem Final

Produza um Artigo Científico baseado nesse prompt, usano as informações dadas e complementando o que foi pedido para explicar e citar sem que o conteúdo fique muito resumido.

---

## 💻 Prompt utilizado para geração do código (ChatGPT)

Crie um código em Python para modelar doenças infectocontagiosas utilizando o modelo SEIR e suas equações diferenciais.

O programa deve receber como entrada:

* População total
* Infectados iniciais
* Número reprodutivo básico (R₀)
* Tempo infeccioso
* Tempo de incubação
* Redução percentual da transmissão
* Dias de simulação

O programa deve gerar um gráfico de barras empilhadas, onde cada barra representa os compartimentos S, E, I e R.

O código deve utilizar discretização temporal (um passo por dia).
