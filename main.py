import flet as ft
from ui.app import TodoApp

def main(page: ft.Page):
    TodoApp(page)

if __name__ == '__main__':
    ft.app(target=main)