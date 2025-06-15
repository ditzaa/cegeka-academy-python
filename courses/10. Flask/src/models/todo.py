class ToDo:
    def __init__(self, id, task="None", done=False):
        self.id = id
        self.task = task
        self.done = done

    def __str__(self):
        return f"{self.id} {self.task}"

    def to_json_dict(self):
        return {
            "id": self.id,
            "task": self.task,
            "done": self.done
        }
