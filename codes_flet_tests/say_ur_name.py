import flet as ft

def main(page):
    def say_click(evnet):
        if not txt_name.value:
            txt_name.error_text = "Plese enter your name"
            page.update()
        else:
            name = txt_name.value
            page.clean()
            page.add(ft.Text(f"Hello, {name}!"))

    txt_name = ft.TextField(label = "Ur name")
    page.add(txt_name, ft.ElevatedButton("Say my name!", on_click=say_click))

ft.app(main)