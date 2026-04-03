from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Lista simples para guardar as tarefas
tarefas = []

# O visual do site (HTML)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meu Checklist</title>
    <style>
        body { font-family: sans-serif; max-width: 600px; margin: 40px auto; padding: 20px; }
        input[type="text"] { padding: 8px; width: 70%; }
        button { padding: 8px 15px; background: #28a745; color: white; border: none; cursor: pointer; }
        ul { list-style-type: none; padding: 0; }
        li { padding: 10px; background: #f4f4f4; margin-bottom: 5px; display: flex; justify-content: space-between; }
        a { color: red; text-decoration: none; font-weight: bold; }
    </style>
</head>
<body>
    <h1>📋 Meu Checklist</h1>
    <form action="/adicionar" method="POST">
        <input type="text" name="tarefa" placeholder="Digite uma nova tarefa..." required>
        <button type="submit">Adicionar</button>
    </form>
    <ul>
        {% for tarefa in tarefas %}
            <li>
                {{ tarefa }}
                <a href="/remover/{{ loop.index0 }}" title="Remover">X</a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, tarefas=tarefas)

@app.route('/adicionar', methods=['POST'])
def adicionar():
    tarefa = request.form.get('tarefa')
    if tarefa:
        tarefas.append(tarefa)
    return redirect(url_for('index'))

@app.route('/remover/<int:tarefa_id>')
def remover(tarefa_id):
    if 0 <= tarefa_id < len(tarefas):
        tarefas.pop(tarefa_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
