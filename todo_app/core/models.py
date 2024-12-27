from dataclasses import dataclass

@dataclass
class TodoItem:
    id: str
    title: str
    completed: bool = False