import flet as ft

def main(page: ft.Page):
    txt = ft.Text(value="Hello, flet", color="red")
    page.add(txt)

ft.app(main)

