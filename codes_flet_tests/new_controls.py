import flet as ft
import time

def main(page: ft.Page):
    for i in range(10):
        page.add(ft.Text(f"Line {i}"))
        if i > 4:
            page.controls.pop(0)
        page.update()
        time.sleep(0.3)

ft.app(main)