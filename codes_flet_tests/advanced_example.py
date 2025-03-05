import flet as ft

def main(page: ft.Page):
    def add_click(event):
        page.add(ft.Checkbox(label = new_task.value))
        new_task.value = ""
        new_task.focus()
        new_task.update()

    new_task = ft.TextField(hint_text = "What's needs to be done?", width = 300)
    page.add(new_task, ft.ElevatedButton("Add", on_click = add_click))

ft.app(main)