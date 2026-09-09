# TaskFlow — Sistema de Gerenciamento de Tarefas

## 1. Identificação do projeto

**Disciplina:** Integração DevOps
**Projeto:** TaskFlow - Gerenciador de Tarefas
**Instituição:** CEUB
**Etapa:** Entrega 1 — Integração Contínua (CI)

## 2. Integrantes

* Luísa Souza
* Isabella Sena
* Maria Eduarda Campelo

## 3. Descrição

O TaskFlow é uma aplicação web desenvolvida em Python com o objetivo de permitir o gerenciamento de tarefas de forma simples.

A aplicação permite ao usuário cadastrar, visualizar, concluir e excluir tarefas.

O projeto foi desenvolvido com foco na aplicação de práticas de Integração DevOps, incluindo versionamento de código, testes automatizados e integração contínua.

## 4. Objetivo

O objetivo do projeto é desenvolver uma aplicação funcional utilizando práticas de desenvolvimento e integração contínua, permitindo que alterações no código sejam automaticamente verificadas por meio de uma pipeline de CI.

## 5. Funcionalidades

* Cadastro de tarefas;
* Listagem de tarefas;
* Conclusão de tarefas;
* Exclusão de tarefas;
* Persistência dos dados em banco SQLite.

## 6. Tecnologias utilizadas

* Python 3.12
* Flask
* SQLite
* Pytest
* Git
* GitHub
* GitHub Actions
* Git Bash

## 7. Arquitetura do projeto

```text
taskflow-devops/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── src/
│   ├── __init__.py
│   ├── database.py
│   └── tasks.py
│
├── templates/
│   └── index.html
│
├── tests/
│   ├── __init__.py
│   └── test_tasks.py
│
└── .github/
    └── workflows/
        └── ci.yml
```

## 8. Banco de dados

A aplicação utiliza SQLite para persistência das tarefas.

A tabela `tasks` possui os seguintes campos:

| Campo       | Tipo    | Descrição                        |
| ----------- | ------- | -------------------------------- |
| id          | INTEGER | Identificador da tarefa          |
| title       | TEXT    | Título da tarefa                 |
| description | TEXT    | Descrição da tarefa              |
| completed   | INTEGER | Indica se a tarefa foi concluída |

## 9. Execução local

### Clonar o projeto

```bash
git clone https://github.com/IsabellaSenaa/ProjetoDevOps26.git
cd ProjetoDevOps26
```

### Criar ambiente virtual

```bash
python -m venv .venv
```

### Ativar o ambiente virtual

No Git Bash:

```bash
source .venv/Scripts/activate
```

### Instalar dependências

```bash
pip install -r requirements.txt
```

### Executar a aplicação

```bash
python app.py
```

A aplicação estará disponível localmente em:

```text
http://127.0.0.1:5000
```

## 10. Execução dos testes

Para executar a suíte de testes:

```bash
python -m pytest tests -v
```

Os testes verificam funcionalidades como:

* criação de tarefas;
* validação de título;
* conclusão de tarefas;
* exclusão de tarefas.

## 11. Estratégia de versionamento

O projeto utiliza uma estratégia baseada em Trunk-Based Development, com a branch `main` como linha principal de desenvolvimento e branches de curta duração para implementação de funcionalidades e configurações.

Exemplos:

```text
feature/aplicacao
feature/testes
feature/ci
```

As alterações são integradas à `main` por meio de Pull Requests.

## 12. Padrão de commits

Foi adotado um padrão baseado em tipos de alteração.

Exemplos:

```text
feat: implementa aplicacao inicial
test: adiciona testes das tarefas
ci: configura pipeline do GitHub Actions
docs: atualiza README
fix: corrige exclusao de tarefa
```

## 13. Integração Contínua

O projeto utiliza GitHub Actions para automatizar a execução dos testes.

A pipeline é executada em eventos de Push e Pull Request.

O fluxo é:

```text
Push / Pull Request
        ↓
GitHub Actions
        ↓
Checkout do código
        ↓
Configuração do Python
        ↓
Instalação das dependências
        ↓
Execução do Pytest
        ↓
Resultado da pipeline
```

Dessa forma, alterações no código são verificadas automaticamente antes da integração à branch principal.

## 14. Critérios de qualidade

A qualidade do projeto é apoiada por:

* testes automatizados;
* revisão por Pull Request;
* branch principal protegida;
* pipeline de integração contínua;
* histórico de commits padronizado.

## 15. Status da Entrega 01

A primeira etapa do projeto contempla:

* [x] Repositório Git estruturado;
* [x] Estratégia de branches definida;
* [x] Aplicação funcional;
* [x] Interface web;
* [x] Banco de dados SQLite;
* [x] Testes automatizados;
* [x] Pipeline de CI;
* [x] GitHub Actions;
* [x] Documentação inicial.
