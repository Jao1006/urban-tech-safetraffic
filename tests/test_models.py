from src.algorithms.motor_logico import avaliar_regras_semaforo

def test_emergencia_prioridade():
    # Se a emergência estiver ativa, deve retornar EMERGENCIA independentemente dos outros
    resultado = avaliar_regras_semaforo(s1=True, s2=True, pedestre=True, emergencia=True)
    assert resultado == "EMERGENCIA"