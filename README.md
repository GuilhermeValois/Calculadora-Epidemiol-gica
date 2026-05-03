# 🧮 Calculadora Epidemiológica SEIR

## 📌 Objetivo

O objetivo deste programa é desenvolver uma **calculadora epidemiológica baseada no modelo SEIR**, capaz de simular o espalhamento de doenças infecciosas a partir de parâmetros definidos pelo usuário.

O sistema permite visualizar a evolução de uma epidemia ao longo do tempo por meio de gráficos gerados automaticamente.

---

## ⚙️ Funcionalidades

* Simulação de epidemia utilizando o modelo SEIR (Susceptíveis, Expostos, Infectados e Recuperados)
* Entrada de parâmetros personalizados pelo usuário
* Geração de gráfico com a evolução da doença ao longo do tempo
* Opção de incluir ou não a curva de suscetíveis (S) no gráfico

---

## 📥 Parâmetros de entrada

O programa solicita os seguintes dados:

* População total (N)
* Infectados iniciais (I₀)
* Número reprodutivo básico (R₀)
* Tempo infeccioso (dias)
* Tempo de incubação (dias)
* Redução percentual da transmissão (0 a 1)
* Dias de simulação

---

## 📤 Saída

* Gráfico de barras sobrepostas mostrando a evolução dos compartimentos do modelo SEIR ao longo do tempo
* Opção de visualizar ou não a curva de suscetíveis (S)

---

## 🧠 Modelo utilizado

O projeto utiliza o modelo epidemiológico **SEIR**, com os seguintes parâmetros:

* **β (beta):** taxa de transmissão da doença
* **σ (sigma):** taxa de progressão do estado exposto para infectado
* **γ (gamma):** taxa de recuperação

---

## 🗂️ Estrutura do projeto

```
Calculadora-Epidemiologica/
│
├── main.py                  # Código principal da simulação
├── README.md                # Documentação do projeto
├── artigo.pdf               # Artigo científico do projeto
├── IA_UTILIZADA.md         # Registro da IA e prompts utilizados
```

---

## 🚀 Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/GuilhermeValois/Calculadora-Epidemiol-gica.git
```

### 2. Acessar a pasta

```bash
cd Calculadora-Epidemiol-gica
```

### 3. Instalar dependências

O projeto utiliza principalmente Python e a biblioteca Matplotlib:

```bash
pip install matplotlib
```

---

### 4. Executar o programa

```bash
python main.py
```

---

## 🧰 Tecnologias utilizadas

* Python 3
* Matplotlib (para geração de gráficos)

---

## 📄 IA utilizada

As informações sobre o uso de inteligência artificial, incluindo prompts utilizados no desenvolvimento, estão documentadas no arquivo:

👉 `IA_UTILIZADA.md`

---

## 👤 Autor

Guilherme Vasconcellos Valois¹

## 🎓 Afiliação acadêmica

Universidade Federal Rural de Pernambuco (UFRPE)
Bacharelado em Sistemas de Informação

¹ Universidade Federal Rural de Pernambuco (UFRPE) — Bacharelado em Sistemas de Informação

---

## 📊 Observação

Este projeto foi desenvolvido com fins educacionais, com foco em modelagem epidemiológica e simulação computacional do modelo SEIR.
