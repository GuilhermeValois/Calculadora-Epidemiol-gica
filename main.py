import matplotlib.pyplot as plt

def seir_model(N, I0, R0_value, Tinf, Tinc, days):
    # Parâmetros derivados
    beta = (R0_value / Tinf) * (1 - reducao)
    sigma = 1 / Tinc
    gamma = 1 / Tinf

    # Condições iniciais
    S = N - I0
    E = 0
    I = I0
    R = 0

    S_list = [S]
    E_list = [E]
    I_list = [I]
    R_list = [R]

    # Simulação
    for _ in range(days):
        new_exposed = beta * S * I / N
        new_infected = sigma * E
        new_recovered = gamma * I

        S -= new_exposed
        E += new_exposed - new_infected
        I += new_infected - new_recovered
        R += new_recovered

        S_list.append(S)
        E_list.append(E)
        I_list.append(I)
        R_list.append(R)

    return S_list, E_list, I_list, R_list
    
    #Funções para ler int e float com tratamento de erros
def ler_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Valor inválido, tente novamente.")

def ler_float(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("Valor inválido, tente novamente.")

    # Função para validar a população total
def verif_N(valor):
    
    while True:
        if valor > 0:
            return valor
        else:
            print("Valor de população inválido. Deve ser um número positivo  maior que 0.")
            valor = ler_int("População total: ")

def verif_R0(valor):
    while True:
        if valor >= 0:
            return valor
        else:
            print("Valor de R0 inválido. Deve ser um número maior ou igual a 0.")
            valor = ler_float("Número reprodutivo básico (R0): ")

def verif_IO(valorinfectados,valorpopulacao):
    while True:
        if 0 <= valorinfectados <= valorpopulacao:
            return valorinfectados
        else:
            print("Valor de infectados iniciais inválido. Deve ser entre 0 e a população total.")
            valorinfectados = ler_int("Infectados iniciais: ")

def verif_Tinf(valor):
    while True:
        if valor > 0:
            return valor
        else:
            print("Valor de tempo infeccioso inválido. Deve ser um número maior ou igual a 0.")
            valor = ler_float("Tempo infeccioso (dias): ")

def verif_Tinc(valor):
    while True:
        if valor > 0:
            return valor
        else:
            print("Valor de tempo de incubação inválido. Deve ser um número positivo maior que 0.")
            valor = ler_float("Tempo de incubação (dias): ")

def verif_days(valor):
    while True:
        if valor > 0:
            return valor
        else:
            print("Valor de dias inválido. Deve ser um número positivo.")
            valor = ler_int("Dias de simulação: ")

    # Função para validar a redução percentual da transmissão
def verif_reducao(valor):
    
    while True:
        if 0 <= valor <= 1:
            return valor
        else:
            print("Valor de redução inválido. Deve ser entre 0 e 1.")
            valor = ler_float("Redução percentual da transmissão (0 a 1): ")
        

# =========================
# INPUT DO USUÁRIO
# =========================
N = verif_N(ler_int("População total: "))
I0 = verif_IO(ler_int("Infectados iniciais: "), N)
R0_value = verif_R0(ler_float("Número reprodutivo básico (R0): "))
Tinf = verif_Tinf(ler_float("Tempo infeccioso (dias): "))
Tinc = verif_Tinc(ler_float("Tempo de incubação (dias): "))
reducao = verif_reducao(ler_float("Redução percentual da transmissão (0 a 1): "))
days = verif_days(ler_int("Dias de simulação: "))
        
    
# =========================
# EXECUÇÃO
# =========================
S, E, I, R = seir_model(N, I0, R0_value, Tinf, Tinc, days)

dias = list(range(len(S)))

# =========================
# GRÁFICO DE BARRAS EMPILHADAS
# =========================

while True:
    pergunta = input("\nDeseja visualizar o parâmetro S(Suscetíveis)? (s/n): ")
    if pergunta.lower() == "s":
        break
    elif pergunta.lower() == "n":
        break
    else:
        print("Resposta inválida. Por favor, digite 's' para sim ou 'n' para não.")

if pergunta.lower() == "n":
    plt.figure(figsize=(10, 6))

    plt.bar(dias, E, label="Expostos")
    plt.bar(dias, I, bottom=E, label="Infectados")
    plt.bar(dias, R, bottom=[E[i] + I[i] for i in range(len(E))], label="Recuperados")

else:
    plt.figure(figsize=(10, 6))

    plt.bar(dias, E, label="Expostos")
    plt.bar(dias, I, bottom=E, label="Infectados")
    plt.bar(dias, R, bottom=[E[i] + I[i] for i in range(len(E))], label="Recuperados")
    plt.bar(dias, S, bottom=[E[i] + I[i] + R[i] for i in range(len(E))], label="Suscetíveis")



plt.xlabel("Dias")
plt.ylabel("Número de pessoas")
plt.title("Simulação Epidemiológica - Modelo SEIR")
plt.legend()

plt.tight_layout()
plt.show()