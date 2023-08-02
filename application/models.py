from application import app, db

app.app_context().push()

class ToDoItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    isCompleted = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, title, description, isCompleted):
        self.title = title
        self.description = description
        self.isCompleted = isCompleted

db.create_all()
