import flet as ft

class my_button(ft.ElevatedButton):
    def __init__(self, text, on_click):
        super().__init__()
        self.bgcolor = ft.Colors.BLACK54
        self.color = ft.Colors.WHITE
        self.text = text
        self.on_click = on_click

def main(page):

    def click_okey(event):
        print("okey click")

    def click_cancel(event):
        print("cancel click")

    page.add(
        my_button("ok", on_click=click_okey),
        my_button("cancel", on_click=click_cancel)
    )

ft.app(main)