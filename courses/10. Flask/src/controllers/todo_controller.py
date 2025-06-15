from services.db_services import get_todos
from flask import blueprints, jsonify
from todo import ToDo

todo_blueprint = blueprints.Blueprint('todos', __name__)


@todo_blueprint.route('/todos', methods=['GET'])
def get_todos_list():
    todos = get_todos()
    json_data = [x.to_json_dict() for x in todos]
    return jsonify(json_data)

@todo_blueprint.route('/todo', methods=['POST'])
def add_todo(task):
    new_id = max([x.id for x in todos]) if len(todos) > 0 else 1
    new_todo = ToDo(new_id, task, False)
    todos.append(new_todo)
    return new_todo


def get_todo(id):
    for x in todos:
        if x.id == id:
            return x
    return None


def delete_todo(x):
    for x in todos:
        if x.id == id:
            deleted_todo = x
            todos.remove(x)
            return deleted_todo
    return None

@todo_blueprint.route('/todo', methods=['POST'])
def post_todo():
    todo = request.get_json()
    new_todo = add_todo(todo["task"])
    return jsonify(new_todo.to_json_dict())
