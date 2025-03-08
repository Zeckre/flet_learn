import flet as ft

def main(page):
    first_name = ft.TextField()
    last_name = ft.TextField()

    c = ft.Column(controls=[
        first_name,
        last_name,
    ])

    c.disabled = True
    page.add(c)

ft.app(main)
