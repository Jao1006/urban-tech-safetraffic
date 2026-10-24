
# Tabela-verdade / Casos de Teste — A.10
# ----------------------------------------------------------------
# Cenário     | S1 | S2 | Pedestre | Emergência | Resultado
# ----------------------------------------------------------------
# Normal      | 1  | 0  | 0        | 0          | Principal
# Secundária  | 0  | 1  | 0        | 0          | Secundária
# Pedestre    | 1  | 1  | 1        | 0          | Travessia
# Emergência  | 1  | 1  | 1        | 1          | Emergência
# ----------------------------------------------------------------
def definir_saida(S1, S2, S3, S4,):
    match (S1, S2, S3, S4):
        case (_, _, _, 1):
            saida = "Emergência"
        case (_, _, 1, 0):
            saida = "Travessia"
        case (1, _, 0, 0):
            saida = "Principal"
        case (0, 1, 0, 0):
            saida = "Secundária"
        case(0, 0, 0, 0):
            saida = "Alternar"
        case _:
            saida = "entrada inválida"
    return saida

