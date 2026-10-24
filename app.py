"""
Interface de Linha de Comando (CLI) para demonstração do SafeTraffic.
"""
from src.algorithms.motor_logico import definir_saida

entradas = []
print("=== Plataforma UrbanTech: SafeTraffic ===")
for i in range(1,5):
    entrada = int(input(f"Digite S{i}: "))
    i+=1
    entradas.append(entrada)
entrada1, entrada2, entrada3, entrada4 = entradas
print("Iniciando motor inteligente de controle semafórico...")
print(f"\n===========\n{definir_saida(entrada1, entrada2, entrada3, entrada4)}\n===========")
    
  