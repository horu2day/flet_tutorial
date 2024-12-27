import flet as ft
from typing import Callable
from core.models import TodoItem

class TodoItemWidget(ft.UserControl):
    def __init__(self, todo_item: TodoItem, on_toggle: Callable, on_delete: Callable):
        super().__init__()
        self.todo_item = todo_item
        self.on_toggle = on_toggle
        self.on_delete = on_delete

    def build(self):
        return ft.Row(
            controls=[
                ft.Checkbox(
                    value=self.todo_item.completed,
                    on_change=lambda e: self.on_toggle(self.todo_item.id)
                ),
                ft.Text(
                    self.todo_item.title,
                    style=ft.TextThemeStyle.BODY_LARGE,
                    decoration=ft.TextDecoration.LINE_THROUGH if self.todo_item.completed else None,
                ),
                ft.IconButton(
                    icon=ft.icons.DELETE_OUTLINE,
                    on_click=lambda e: self.on_delete(self.todo_item.id)
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )