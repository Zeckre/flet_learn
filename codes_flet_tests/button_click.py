import flet as ft

def main(page: ft.Page):
    def button_click(event):
        page.add(ft.Text("Clicked!"))

    page.add(ft.TextButton(text = "CLick me", on_click=button_click))

ft.app(main)