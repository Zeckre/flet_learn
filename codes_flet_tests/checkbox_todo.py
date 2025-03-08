import flet as ft

def main(page):
    def check_click(event):
        output_text.value = (f"you have learned how to use a checkbox {todo_check.value}")
        page.update()

    output_text = ft.Text()
    todo_check = ft.Checkbox(label = "TODO: Learn how to use a checkbox", value=False, on_change=check_click)
    page.add(todo_check, output_text)

ft.app(main)