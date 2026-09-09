import sqlite3

import pytest

import src.database as database

from src.tasks import (
    criar_tarefa,
    listar_tarefas,
    concluir_tarefa,
    excluir_tarefa
)


@pytest.fixture
def banco_teste(tmp_path, monkeypatch):

    caminho_banco = tmp_path / "test.db"

    monkeypatch.setattr(
        database,
        "DATABASE",
        str(caminho_banco)
    )

    conexao = sqlite3.connect(str(caminho_banco))

    conexao.execute("""
        CREATE TABLE tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            completed INTEGER NOT NULL DEFAULT 0
        )
    """)

    conexao.commit()
    conexao.close()

    yield


def test_criar_tarefa(banco_teste):

    tarefa_id = criar_tarefa(
        "Estudar Python",
        "Revisar Flask"
    )

    tarefas = listar_tarefas()

    assert tarefa_id == 1
    assert len(tarefas) == 1
    assert tarefas[0]["title"] == "Estudar Python"


def test_criar_tarefa_sem_titulo(banco_teste):

    with pytest.raises(ValueError):

        criar_tarefa("", "Descrição")


def test_concluir_tarefa(banco_teste):

    tarefa_id = criar_tarefa(
        "Fazer teste",
        "Testar conclusão"
    )

    concluir_tarefa(tarefa_id)

    tarefas = listar_tarefas()

    assert tarefas[0]["completed"] == 1


def test_excluir_tarefa(banco_teste):

    tarefa_id = criar_tarefa(
        "Excluir tarefa",
        "Tarefa para teste"
    )

    excluir_tarefa(tarefa_id)

    tarefas = listar_tarefas()

    assert len(tarefas) == 0

