from application import app, db
from application.models import ToDoItem
from flask import request, jsonify


def format_todo(todo):
    return {
        "id": todo.id,
        "title": todo.title,
        "description": todo.description,
        "isCompleted": todo.isCompleted,
    }


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/todo", methods=["GET", "POST"], strict_slashes=False)
def todos():
    if request.method == "GET":
        todos = ToDoItem.query.all()
        todo_list = []
        for todo in todos:
            todo_list.append(format_todo(todo))
        return todo_list
    elif request.method == "POST":
        data = request.json
        todo = ToDoItem(data["title"], data["description"], data["isCompleted"])
        db.session.add(todo)
        db.session.commit()
        return format_todo(todo)


@app.route("/todo/<id>", methods=["GET", "PATCH", "DELETE"], strict_slashes=False)
def todo(id):
    if request.method == "GET":
        todo = ToDoItem.query.filter_by(id=id).first()
        return format_todo(todo)
    elif request.method == "DELETE":
        todo = ToDoItem.query.filter_by(id=id).first()
        db.session.delete(todo)
        db.session.commit()
        return "Deleted!"
    elif request.method == "PATCH":
        todo = ToDoItem.query.get(id)
        data = request.json
        todo.title = data.get("title", todo.title)
        todo.description = data.get("description", todo.description)
        todo.isCompleted = data.get("isCompleted", todo.isCompleted)
        db.session.commit()
        return format_todo(todo)
