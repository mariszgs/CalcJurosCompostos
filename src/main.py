import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora de Juros Compostos"

    valor_inicial = ft.TextField(
        width=340
    )
    valor_mensal = ft.TextField(
        width=340
    )
    taxa = ft.TextField(
        width=180
    )
    periodo = ft.TextField(
        width=170
    )

    tipo_taxa = ft.Dropdown(
        width=160,
        value="anual",
        options=[
            ft.DropdownOption("mensal"),
            ft.DropdownOption("anual"),
        ]
    )

    tipo_periodo = ft.Dropdown(
        width=160,
        value="ano(s)",
        options=[
            ft.DropdownOption("mes(es)"),
            ft.DropdownOption("ano(s)"),
        ]
    )

    page.add(
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Container(
                width=900,
                padding=30,
                bgcolor="#DCDCDC",
                border_radius=10,
                
        content=ft.Column(
            controls=[
            ft.Text(value="Simulador de Juros Compostos",
            size=25,
            weight=ft.FontWeight.BOLD,
            color="#000080"
        ),

            ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Column(
                        controls=[
                            ft.Text("Valor Inicial"),
                            valor_inicial,
                        ]
                    ),
                    ft.Column(
                        controls=[
                            ft.Text("Valor Mensal:"),
                            valor_mensal,
                        ]
                    )
                ]
            ),

            ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Column(
                    controls=[
                        ft.Text("Taxa de Juros:"),
                        ft.Row(
                            controls=[
                                taxa,
                                tipo_taxa,
                            ]
                        )
                    ]
                ),
                ft.Column(
                    controls=[
                        ft.Text("Período:"),
                        ft.Row(
                            controls=[
                                periodo,
                                tipo_periodo,
                            ]
                        )
                    ]
                )
             ]
          ),

          ft.Row(
              alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
              controls=[
                  ft.Button(
                    content="Calcular",
                    color="#000080"
                    ),
                  ft.Button(
                    content="Limpar",
                    color="#8B0000"
                    ),
                                ],
                            ),
                        ]
                    ),
                )
            ],
        )
    )
    
ft.run(main)