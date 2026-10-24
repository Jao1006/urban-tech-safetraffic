from itertools import product


def ler_sensor(nome):
    """Lê um sensor e aceita somente 0 ou 1."""
    while True:
        valor = input(f"{nome} (0 = não, 1 = sim): ")

        if valor in ("0", "1"):
            return valor == "1"

        print("Entrada inválida. Digite 0 ou 1.")


def avaliar_sensores(principal, secundaria, pedestre, ambulancia):
    """Escolhe a prioridade com base nos sensores."""
    if ambulancia:
        return "Emergência"

    if pedestre:
        return "Travessia"

    if principal:
        return "Principal"

    if secundaria:
        return "Secundária"

    return "Alternar"


class ControladorSemaforico:
    """Controla uma simulação simplificada do cruzamento."""

    def __init__(self):
        self.estado = "VERMELHO"
        self.via_atual = "Secundária"
        self.historico = []

    def mudar_estado(self, novo_estado):
        """Atualiza e mostra o estado do semáforo."""
        self.estado = novo_estado
        print("Estado:", self.estado)

    def fechar_passagem(self):
        """Encerra a passagem atual antes de liberar outra."""
        if self.estado == "VERDE":
            self.mudar_estado("AMARELO")

        self.mudar_estado("VERMELHO")

    def executar(self, principal, secundaria, pedestre, ambulancia):
        """Avalia os sensores e executa uma sequência de estados."""
        decisao = avaliar_sensores(
            principal, secundaria, pedestre, ambulancia
        )

        print("\nDecisão:", decisao)
        self.fechar_passagem()

        if decisao == "Emergência":
            self.mudar_estado("EMERGENCIA")
            print("Passagem exclusiva para a ambulância.")
            self.mudar_estado("VERMELHO")

        elif decisao == "Travessia":
            self.mudar_estado("PEDESTRE")
            print("Veículos parados. Travessia liberada.")
            self.mudar_estado("VERMELHO")

        else:
            if decisao == "Alternar":
                if self.via_atual == "Principal":
                    self.via_atual = "Secundária"
                else:
                    self.via_atual = "Principal"
            else:
                self.via_atual = decisao

            self.mudar_estado("VERDE")
            print("Via liberada:", self.via_atual)

        registro = {
            "sensores": (
                principal, secundaria, pedestre, ambulancia
            ),
            "decisao": decisao,
            "estado_final": self.estado
        }

        self.historico.append(registro)

    def mostrar_historico(self):
        """Mostra as decisões registradas nesta execução."""
        if not self.historico:
            print("Nenhuma decisão registrada.")
            return

        for numero, registro in enumerate(self.historico, start=1):
            sensores = tuple(int(valor) for valor in registro["sensores"])

            print(
                f"{numero}. Sensores: {sensores} | "
                f"Decisão: {registro['decisao']} | "
                f"Estado final: {registro['estado_final']}"
            )


def mostrar_tabela():
    """Mostra todas as combinações de sensores e suas decisões."""
    print("\nS1 = principal | S2 = secundária")
    print("P = pedestre | A = ambulância\n")
    print("S1 S2 P A | Decisão")
    print("-" * 35)

    for principal, secundaria, pedestre, ambulancia in product(
        (False, True), repeat=4
    ):
        decisao = avaliar_sensores(
            principal, secundaria, pedestre, ambulancia
        )

        print(
            f"{int(principal)}  {int(secundaria)}  "
            f"{int(pedestre)} {int(ambulancia)} | {decisao}"
        )


def main():
    """Executa o menu principal do SafeTraffic."""
    controlador = ControladorSemaforico()

    while True:
        print("\n--- SafeTraffic ---")
        print("1 - Informar sensores e simular")
        print("2 - Mostrar tabela de combinações")
        print("3 - Mostrar histórico")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            principal = ler_sensor("Veículo na via principal")
            secundaria = ler_sensor("Veículo na via secundária")
            pedestre = ler_sensor("Pedestre esperando")
            ambulancia = ler_sensor("Ambulância detectada")

            controlador.executar(
                principal, secundaria, pedestre, ambulancia
            )

        elif opcao == "2":
            mostrar_tabela()

        elif opcao == "3":
            controlador.mostrar_historico()

        elif opcao == "0":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()