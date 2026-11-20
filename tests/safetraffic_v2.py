import random
from itertools import product


def ler_sensor(nome):
    """Lê um sensor e aceita somente 0 ou 1."""
    while True:
        valor = input(f"{nome} (0 = não, 1 = sim): ")

        if valor in ("0", "1"):
            return valor == "1"

        print("Entrada inválida. Digite 0 ou 1.")


def avaliar_sensores(principal, secundaria, pedestre, ambulancia):
    """Define a prioridade do cruzamento com base nos sensores."""
    if ambulancia:
        return "Emergência"

    if pedestre:
        return "Travessia"

    if principal and secundaria:
        return "Alternar"

    if principal:
        return "Principal"

    if secundaria:
        return "Secundária"

    return "Nenhum veículo"


class ControladorSemaforico:
    """Controla uma simulação simplificada do cruzamento."""

    def __init__(self):
        self.estado = "VERMELHO"
        self.via_atual = "Secundária"
        self.historico = []

    def mudar_estado(self, novo_estado):
        """Atualiza e mostra o estado atual do semáforo."""
        self.estado = novo_estado
        print("Estado:", self.estado)

    def fechar_passagem(self):
        """Fecha a passagem atual antes de liberar outra."""
        if self.estado != "VERMELHO":
            self.mudar_estado("AMARELO")

        self.mudar_estado("VERMELHO")

    def executar(self, principal, secundaria, pedestre, ambulancia):
        """Avalia os sensores e executa o ciclo do semáforo."""
        decisao = avaliar_sensores(
            principal, secundaria, pedestre, ambulancia
        )

        print("\nDecisão:", decisao)
        self.fechar_passagem()

        if decisao == "Emergência":
            self.mudar_estado("EMERGENCIA")
            print("Passagem exclusiva para a ambulância.")

        elif decisao == "Travessia":
            self.mudar_estado("PEDESTRE")
            print("Veículos parados. Travessia liberada.")

        elif decisao == "Nenhum veículo":
            print("Nenhuma via precisa ser liberada.")

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

    def simular_aleatorio(self):
        """Gera várias simulações aleatórias de sensores."""
        while True:
            try:
                quantidade = int(
                    input("Quantas gerações você deseja simular? ")
                )

                if quantidade > 0:
                    break

                print("Digite um número maior que zero.")

            except ValueError:
                print("Entrada inválida. Digite um número inteiro.")

        for numero in range(1, quantidade + 1):
            print(f"\n--- Geração {numero} de {quantidade} ---")

            principal = random.choice([False, True])
            secundaria = random.choice([False, True])
            pedestre = random.choice([False, True])
            ambulancia = random.choice([False, True])

            print("Veículo na via principal:", int(principal))
            print("Veículo na via secundária:", int(secundaria))
            print("Pedestre esperando:", int(pedestre))
            print("Ambulância detectada:", int(ambulancia))

            self.executar(
                principal, secundaria, pedestre, ambulancia
            )

        print(f"\n{quantidade} geração(ões) simulada(s) com sucesso.")

    def mostrar_historico(self):
        """Mostra as decisões registradas nesta execução."""
        if not self.historico:
            print("Nenhuma decisão registrada.")
            return

        for numero, registro in enumerate(self.historico, start=1):
            sensores = tuple(
                int(valor) for valor in registro["sensores"]
            )

            print(
                f"{numero}. Sensores: {sensores} | "
                f"Decisão: {registro['decisao']} | "
                f"Estado final: {registro['estado_final']}"
            )

    def mostrar_estatisticas(self):
        """Mostra quantas vezes cada decisão foi tomada."""
        if not self.historico:
            print("Nenhuma decisão registrada.")
            return

        contagem = {}

        for registro in self.historico:
            decisao = registro["decisao"]
            contagem[decisao] = contagem.get(decisao, 0) + 1

        print("\n--- Estatísticas ---")

        for decisao, quantidade in contagem.items():
            print(f"{decisao}: {quantidade} vez(es)")


def mostrar_tabela():
    """Mostra todas as combinações de sensores e suas decisões."""
    print("\nS1 = principal | S2 = secundária")
    print("P = pedestre | A = ambulância\n")
    print("S1 S2 P A | Decisão")
    print("-" * 40)

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
        print("4 - Simular sensores aleatoriamente")
        print("5 - Mostrar estatísticas")
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

        elif opcao == "4":
            controlador.simular_aleatorio()

        elif opcao == "5":
            controlador.mostrar_estatisticas()

        elif opcao == "0":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()