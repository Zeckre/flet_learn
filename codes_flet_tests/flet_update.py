import flet as ft
import time

def main(page: ft.Page):
    txt = ft.Text()
    page.add(txt) #page.add is a shortcut for page.controls.append() and the page.update()

    for i in range(10):
        txt.value = f"step {i}"
        page.update()
        time.sleep(1)

ft.app(main)