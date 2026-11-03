import pytest
from src.algorithms.maquina_estados import MaquinaEstadosSemaforo

def test_ciclo_normal_semaforo():
    maquina = MaquinaEstadosSemaforo()
    assert maquina.obter_estado() == "VERMELHO"

    maquina.transicionar("VERDE")
    assert maquina.obter_estado() == "VERDE"

    maquina.transicionar("AMARELO")
    assert maquina.obter_estado() == "AMARELO"

    maquina.transicionar("VERMELHO")
    assert maquina.obter_estado() == "VERMELHO"

def test_regra_emergencia_universal():
    maquina = MaquinaEstadosSemaforo()
    maquina.transicionar("VERDE")
    
    # Aciona a emergência a partir do verde[cite: 7, 11]
    maquina.transicionar("EMERGENCIA", emergencia=True)
    assert maquina.obter_estado() == "EMERGENCIA"