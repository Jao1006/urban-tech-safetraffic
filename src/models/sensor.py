"""
Módulo de modelos e entidades do domínio SafeTraffic.
Representa os sensores e estados do sistema semafórico.
"""

class Sensor:
    """Representa um sensor físico ou lógico no cruzamento (ex: S1, S2, Pedestre, Emergência)."""
    def __init__(self, nome: str, ativo: bool = False):
        self.nome = nome
        self.ativo = ativo

    def __str__(self):
        estado = "ATIVO" if self.ativo else "INATIVO"
        return f"Sensor {self.nome}: {estado}"


class EstadoSemaforo:
    """Representa o estado atual do semáforo e suas transições."""
    def __init__(self, estado_atual: str = "VERMELHO"):
        self.estado_atual = estado_atual