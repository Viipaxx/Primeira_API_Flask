# Desafio proposto pelo professor

---

#### Criar um api para gerenciar cadastro de tarefas

- A API terá uma lista de tarefas que deverá ter os seguintes campos: id, responsável, tarefa e status;
- A API deverá permitir listar todas as tarefas e também incluir novas tarefas;
- A API deverá permitir consultar uma tarefa através do ID, alterar o status de uma tarefa e também excluir uma tarefa;
- Nenhuma outra alteração deverá ser permitida além do status da tarefa.

---

#### Rotas

<p>Rota principal:</p>

```
http://127.0.0.1:1001/ [ GET ]
```

<p>Rota para adicionar tarefa:</p>

```
http://127.0.0.1:1001/tarefa/ [ POST ]
```

<p>Rota para pegar, deletar e atualizar uma tarefa:</p>

```
http://127.0.0.1:1001/tarefa/<int:id>/ [ PUT, GET, DELETE ]
```