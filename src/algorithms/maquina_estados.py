class MaquinaEstadosSemaforo:
    def __init__(self):
        # Estado inicial padrão do semáforo
        self.estado_atual = "VERMELHO"

    def obter_estado(self) -> str:
        """Retorna o estado atual do semáforo."""
        return self.estado_atual

    def transicionar(self, proximo_estado: str, emergencia: bool = False, pedestre_solicitou: bool = False) -> str:
        """
        Executa a transição de estado considerando as regras de prioridade e segurança.
        """
        # Regra universal: qualquer estado pode ir para emergência imediatamente[cite: 7, 11]
        if emergencia:
            self.estado_atual = "EMERGENCIA"
            return self.estado_atual

        # Regra de pedestre: prioriza a travessia se seguro[cite: 5, 11]
        if pedestre_solicitou and self.estado_atual in ["VERMELHO", "AMARELO"]:
            self.estado_atual = "PEDESTRE"
            return self.estado_atual

        # Mapeamento das transições normais permitidas[cite: 7, 11]
        transicoes_validas = {
            "VERDE": "AMARELO",
            "AMARELO": "VERMELHO",
            "VERMELHO": "VERDE",
            "PEDESTRE": "VERMELHO",
            "EMERGENCIA": "VERDE"  # Retorno ao ciclo normal após o fim da emergência
        }

        # Valida se a transição solicitada respeita o fluxo natural
        if transicoes_validas.get(self.estado_atual) == proximo_estado:
            self.estado_atual = proximo_estado
        else:
            raise ValueError(f"Transição inválida do estado '{self.estado_atual}' para '{proximo_estado}'.")

        return self.estado_atual