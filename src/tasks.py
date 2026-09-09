from src.database import conectar


def criar_tarefa(title, description=""):
    if not title or not title.strip():
        raise ValueError("O título da tarefa é obrigatório.")

    conexao = conectar()

    cursor = conexao.execute(
        """
        INSERT INTO tasks (title, description)
        VALUES (?, ?)
        """,
        (title.strip(), description.strip())
    )

    conexao.commit()

    tarefa_id = cursor.lastrowid

    conexao.close()

    return tarefa_id


def listar_tarefas():
    conexao = conectar()

    tarefas = conexao.execute(
        """
        SELECT id, title, description, completed
        FROM tasks
        ORDER BY id DESC
        """
    ).fetchall()

    conexao.close()

    return tarefas


def concluir_tarefa(task_id):
    conexao = conectar()

    conexao.execute(
        """
        UPDATE tasks
        SET completed = 1
        WHERE id = ?
        """,
        (task_id,)
    )

    conexao.commit()
    conexao.close()


def excluir_tarefa(task_id):
    conexao = conectar()

    conexao.execute(
        """
        DELETE FROM tasks
        WHERE id = ?
        """,
        (task_id,)
    )

    conexao.commit()
    conexao.close()