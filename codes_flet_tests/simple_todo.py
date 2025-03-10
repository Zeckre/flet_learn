import flet as ft

def main(page):
    def add_click(event):
        page.add(ft.Checkbox(label = new_task.value))
        new_task.value = ""
        new_task.focus()
        new_task.update()

    new_task = ft.TextField(hint_text = "Whats needs to be done?", width = 300)
    page.add(ft.Row([new_task, ft.ElevatedButton("Add", on_click = add_click)]))

ft.app(main)