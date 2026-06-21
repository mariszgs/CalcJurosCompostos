import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora de Juros Compostos"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

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

    resultado_container = ft.Container(
                    width=900,
                    padding=30,
                    bgcolor="#DCDCDC",
                    border_radius=10,
                    alignment=ft.Alignment.CENTER,
                    visible=False,

                    content=ft.Column(
                        spacing=25,
                        controls=[

                            ft.Text(
                                "Resultado",
                                size=24,
                                weight=ft.FontWeight.BOLD,
                                color="#000080",
                            ),

                            ft.Row(
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                controls=[
                                    #1
                                    ft.Container(
                                        width=250,
                                        height=100,
                                        bgcolor="#000080",
                                        border_radius=8,
                                        alignment=ft.Alignment.CENTER,

                                        content=ft.Column(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                            controls=[
                                                ft.Text(
                                                    "Valor Total Final",
                                                    color="white",
                                                    weight=ft.FontWeight.BOLD,
                                                ),
                                                ft.Text(
                                                    "R$ 00,00",
                                                    color="white",
                                                    size=22,
                                                    weight=ft.FontWeight.BOLD,
                                                )
                                            ]
                                        )
                                    ),
                                    #2
                                    ft.Container(
                                        width=250,
                                        height=100,
                                        bgcolor="white",
                                        border_radius=8,
                                        alignment=ft.Alignment.CENTER,

                                        content=ft.Column(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                            controls=[
                                                ft.Text(
                                                    "Valor Total investido",
                                                    weight=ft.FontWeight.BOLD,
                                                ),
                                                ft.Text(
                                                    "R$00,00",
                                                    size=22,
                                                    color="#000080",
                                                    weight=ft.FontWeight.BOLD,
                                                ),
                                            ]
                                        )
                                    ),
                                    #3
                                    ft.Container(
                                        width=250,
                                        height=100,
                                        bgcolor="white",
                                        border_radius=8,
                                        alignment=ft.Alignment.CENTER,

                                        content=ft.Column(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                            controls=[
                                                ft.Text(
                                                    "Total em Juros",
                                                    weight=ft.FontWeight.BOLD,
                                                ),
                                                ft.Text(
                                                    "R$00,00",
                                                    size=22,
                                                    color="black",
                                                    weight=ft.FontWeight.BOLD,
                                                )
                                            ]
                                        )

                                    )
                                ]
                            )
                        ]
                    )
                )
    
    def calcular(e):
        resultado_container.visible = True
        page.update()

    botao_calcular = ft.Button(
       "Calcular",
       on_click=calcular,
       color="#000080"
    )

    def limpar(e):
        resultado_container.visible = False
        page.update()

    botao_limpar = ft.Button(
        "Limpar",
        on_click=limpar,
        color="#8B0000"
    )


    page.add(
        ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
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
                  botao_calcular,
                  botao_limpar
                                ],
                            ),
                        ]
                    ),
                ),
                resultado_container
            ],
        )
    )
    
ft.run(main)