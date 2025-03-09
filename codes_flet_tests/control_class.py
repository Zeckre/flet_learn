import flet as ft

class my_button(ft.ElevatedButton):
    def __init__(self, text):
        super().__init__()
        self.bgcolor = ft.Colors.BLACK54
        self.color = ft.Colors.WHITE
        self.text = text

def main(page):
    page.title = "Control Class"
    page.add(my_button("Hello World"), my_button("Bye World"))
    
ft.app(main)