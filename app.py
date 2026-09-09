from flask import Flask, render_template, request, redirect, url_for

from src.database import inicializar_banco
from src.tasks import (
    criar_tarefa,
    listar_tarefas,
    concluir_tarefa,
    excluir_tarefa
)


app = Flask(__name__)


@app.route("/")
def index():
    tarefas = listar_tarefas()
    return render_template("index.html", tarefas=tarefas)


@app.route("/adicionar", methods=["POST"])
def adicionar():
    titulo = request.form.get("title", "")
    descricao = request.form.get("description", "")

    try:
        criar_tarefa(titulo, descricao)
    except ValueError:
        return redirect(url_for("index"))

    return redirect(url_for("index"))


@app.route("/concluir/<int:task_id>", methods=["POST"])
def concluir(task_id):
    concluir_tarefa(task_id)
    return redirect(url_for("index"))


@app.route("/excluir/<int:task_id>", methods=["POST"])
def excluir(task_id):
    excluir_tarefa(task_id)
    return redirect(url_for("index"))


if __name__ == "__main__":
    inicializar_banco()
    app.run(debug=True)