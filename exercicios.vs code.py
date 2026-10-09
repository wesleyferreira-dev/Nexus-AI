# projeto NEXUS AI #
# =========================================
#              NEXUS AI
# =========================================

print("=======================================")
print("              NEXUS AI")
print("=======================================")

nome = input("Digite seu nome: ")

print(f"\nOlá, {nome}! Seja bem-vindo(a)!")
print(f"{nome}, vou usar você como cobaia para testar meus algoritmos de inteligência artificial.")
print("Vamos começar com algumas perguntas simples, ok?")

salario = float(input("Qual é o seu salário atual? R$ "))

print(f"Entendi! Seu salário atual é de R$ {salario:.2f}")

# DESPESAS
carro: float = 1500.00
computador: float = 280.00
cartao: float = 400.00
gasolina: float = 350.00
cabelo: float = 120.00
despesas_totais: float = carro + computador + cartao + gasolina + cabelo
sobrar: float = salario - despesas_totais
print(f"suas despesas mensais são de R$ {despesas_totais:.2f}")
print(f"sobrando R${sobrar:.2f} para voce gastar com oque quiser, {nome}!")

if sobrar >= 450.00:
    print(f" parabens! Voce tem uma boa maegem para investir ou guardar dinheiro!,{nome} ")
elif sobrar < 450.00 and sobrar > 300.00: 
    print(f" cuidado! voce tem uma margem pequena para investir ou guardar dinheiro!,{nome} ")
else:
    print(f" cuidado!, {nome} tente reduzir suas despesas mensais! ")
    
# SEPARANDO OS GASTOS
print(f"carro:R$ {carro:.2f}")
print(f"computador:R$ {computador:.2f}")
print(f"cartao:R$ {cartao:.2f}")
print(f"gasolina:R$ {gasolina:.2f}")
print(f"cabelo:R$ {cabelo:.2f}")
print(f"despesas totais:R$ {despesas_totais:.2f}")