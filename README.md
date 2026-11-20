# 🚦 SafeTraffic

### Sistema Inteligente de Controle Semafórico

🎓 Projeto Acadêmico desenvolvido na **UniFG (Centro Universitário dos Guararapes)**.

O SafeTraffic é uma simulação de um sistema inteligente de controle de tráfego capaz de analisar informações fornecidas por sensores de veículos, pedestres e ambulâncias, tomando decisões automáticas para gerenciar o fluxo em um cruzamento.

---

## 📖 Sobre o Projeto

O SafeTraffic foi desenvolvido para demonstrar conceitos de:

- Lógica de programação;
- Estruturas condicionais;
- Programação Orientada a Objetos (POO);
- Simulação de sistemas inteligentes;
- Controle e automação de processos.

O sistema analisa informações fornecidas por sensores e determina qual ação deve ser executada no cruzamento, sempre respeitando uma ordem de prioridade previamente definida.

---

## 🎯 Funcionalidades

✅ Leitura manual dos sensores

✅ Simulação do funcionamento do semáforo

✅ Priorização de ambulâncias em emergências

✅ Controle de travessia de pedestres

✅ Alternância automática entre vias com fluxo simultâneo

✅ Histórico das decisões tomadas

✅ Estatísticas de execução

✅ Simulação aleatória de cenários

✅ Tabela completa com todas as combinações possíveis dos sensores

---

## 🧠 Lógica de Prioridade

O sistema segue a seguinte ordem de decisão:

1. Ambulância detectada
2. Pedestre aguardando travessia
3. Veículos nas duas vias (alternância)
4. Veículo na via principal
5. Veículo na via secundária
6. Nenhum veículo detectado

### Fluxo simplificado

```text
Ambulância?
 └─ Sim → Emergência

Pedestre?
 └─ Sim → Travessia

Veículos nas duas vias?
 └─ Sim → Alternar

Veículo na principal?
 └─ Sim → Principal

Veículo na secundária?
 └─ Sim → Secundária

Nenhum sensor ativo
 └─ Nenhum veículo
```

---

## 📂 Estrutura do Projeto

```text
SafeTraffic/
│
├── .git/                # Controle de versão Git
├── .pytest_cache/       # Cache dos testes
├── .venv/               # Ambiente virtual Python
├── data/                # Dados utilizados no projeto
├── docs/                # Documentação do projeto
├── notebooks/           # Estudos e experimentos
├── report/              # Relatórios do projeto
├── src/                 # Código-fonte principal
├── tests/               # Testes automatizados
│
├── .gitignore
├── app.py               # Arquivo principal de execução
├── LICENSE
└── README.md
```

---

## 🛠️ Tecnologias Utilizadas

- Python 3
- Programação Orientada a Objetos (POO)
- Biblioteca `random`
- Biblioteca `itertools`

---

## 📋 Menu do Sistema

```text
1 - Informar sensores e simular
2 - Mostrar tabela de combinações
3 - Mostrar histórico
4 - Simular sensores aleatoriamente
5 - Mostrar estatísticas
0 - Sair
```

---

## 📸 Exemplo de Execução

```text
Veículo na via principal (0 = não, 1 = sim): 1
Veículo na via secundária (0 = não, 1 = sim): 0
Pedestre esperando (0 = não, 1 = sim): 0
Ambulância detectada (0 = não, 1 = sim): 0

Decisão: Principal
Estado: VERDE
Via liberada: Principal
```

---

## 📊 Possíveis Melhorias Futuras

- Interface gráfica (GUI)
- Persistência de dados em banco de dados
- Controle de múltiplos cruzamentos
- Temporização real dos semáforos
- Integração com sensores físicos (Arduino ou ESP32)
- Dashboard de monitoramento

---

## 🎓 Projeto Acadêmico

Este projeto foi desenvolvido como atividade acadêmica da **UniFG (Centro Universitário dos Guararapes)**, com o objetivo de aplicar os conhecimentos adquiridos nas disciplinas relacionadas à programação, modelagem de sistemas e automação.

---

## 👨‍💻 Autores

- João Alberto
- Miguel Soares
- Arthur Andrade
- Luiz Gabriel
- Marllon gabriel
- Lucas Fernandes

---

## 📄 Licença

Projeto desenvolvido para fins educacionais e acadêmicos.
