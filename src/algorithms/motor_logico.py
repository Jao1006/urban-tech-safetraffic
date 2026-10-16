"""
Núcleo matemático e algorítmico do SafeTraffic.
Responsável por avaliar regras booleanas, tabelas-verdade e máquina de estados.
"""

def avaliar_regras_semaforo(s1: bool, s2: bool, pedestre: bool, emergencia: bool) -> str:
    """
    Avalia as regras de decisão lógica do semáforo com base nas entradas dos sensores.
    Retorna o estado ou direção prioritária correspondente.
    """
    # Esqueleto inicial da lógica de decisão citada no documento do projeto
    if emergencia:
        return "EMERGENCIA"
    elif pedestre:
        return "TRAVESSIA_PEDESTRE"
    elif s1:
        return "VIA_PRINCIPAL"
    elif s2:
        return "VIA_SECUNDARIA"
    else:
        return "ALTERNAR"