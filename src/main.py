import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora de Juros Compostos"
    result = ft.Text(value="0")

    page.add(
        ft.Column(
            controls=[
            ft.Text(value="Simulador de Juros Compostos"),
            ft.Row(
            controls=[
                ft.Text(value="Valor Inicial:"),
                ft.TextField(width=150),
                ft.Text(value="Valor Mensal:"),
                ft.TextField(width=150),
             ]
          ),
          ft.Row(
              controls=[
                  ft.Text(value="Taxa de Juros (%):"),
                  ft.TextField(width=150),
                  ft.Text(value="Período (meses):"),
                  ft.TextField(width=150),
              ]
          )
       ]
    )
)
    
ft.run(main)