"""
Interface de Linha de Comando (CLI) para demonstração do SafeTraffic.
"""
from src.algorithms.motor_logico import avaliar_regras_semaforo

def main():
    print("=== Plataforma UrbanTech: SafeTraffic ===")
    print("Iniciando motor inteligente de controle semafórico...")
    
    # Exemplo simulado rápido
    resultado = avaliar_regras_semaforo(s1=True, s2=False, pedestre=False, emergencia=False)
    print(f"Decisão do motor para o cenário de teste: {resultado}")

if __name__ == "__main__":
    main()