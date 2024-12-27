import flet as ft
from core.state import TodoState
from .widgets.todo_item import TodoItemWidget

class TodoApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.state = TodoState()
        self.setup_page()
        self.setup_state()

    def setup_page(self):
        self.page.title = "Todo 앱"
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.window_width = 400
        self.page.window_height = 600
        self.page.window_resizable = False
        self.page.padding = 20

        # Input field
        self.new_task = ft.TextField(
            hint_text="할 일을 입력하세요",
            expand=True,
            on_submit=self.add_task
        )
        
        # Task list
        self.tasks = ft.Column(scroll=ft.ScrollMode.AUTO)

        # Main layout
        self.page.add(
            ft.Text("오늘의 할 일", style=ft.TextThemeStyle.HEADLINE_MEDIUM),
            ft.Row(
                controls=[
                    self.new_task,
                    ft.IconButton(
                        icon=ft.icons.ADD_CIRCLE,
                        on_click=self.add_task
                    )
                ]
            ),
            self.tasks
        )

    def setup_state(self):
        self.state.add_listener(self.update_ui)

    def add_task(self, e):
        if self.new_task.value:
            self.state.add_item(self.new_task.value)
            self.new_task.value = ""
            self.page.update()

    def update_ui(self):
        self.tasks.controls = [
            TodoItemWidget(
                todo_item=item,
                on_toggle=self.state.toggle_item,
                on_delete=self.state.delete_item
            )
            for item in self.state.items
        ]
        self.page.update()