from typing import List, Callable
import uuid
from .models import TodoItem

class TodoState:
    def __init__(self):
        self._items: List[TodoItem] = []
        self._listeners: List[Callable] = []

    def add_listener(self, listener: Callable):
        self._listeners.append(listener)

    def notify_listeners(self):
        for listener in self._listeners:
            listener()

    @property
    def items(self) -> List[TodoItem]:
        return self._items

    def add_item(self, title: str):
        self._items.append(TodoItem(id=str(uuid.uuid4()), title=title))
        self.notify_listeners()

    def toggle_item(self, item_id: str):
        for item in self._items:
            if item.id == item_id:
                item.completed = not item.completed
                break
        self.notify_listeners()

    def delete_item(self, item_id: str):
        self._items = [item for item in self._items if item.id != item_id]
        self.notify_listeners()