import flet as ft

def main(page):
    def button_click(event):
        output_text.value = f"Dropdown value is: {color_dropdown.value}"
        page.update()
    
    output_text = ft.Text()
    submit_button = ft.ElevatedButton("Submit", on_click=button_click)
    color_dropdown = ft.Dropdown(
        width=100,
        options=[
            ft.dropdown.Option("Red"),
            ft.dropdown.Option("Green"),
            ft.dropdown.Option("Blue"),
        ],
    )
    page.add(color_dropdown, submit_button, output_text)

ft.app(main)