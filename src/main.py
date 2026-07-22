import flet as ft
import pandas as pd
import matplotlib.pyplot as plt

def main(page: ft.Page):
    page.title = "Calculadora de Juros Compostos"
    page.scroll = ft.ScrollMode.AUTO
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
        value="mensal",
        options=[
            ft.DropdownOption("mensal"),
            ft.DropdownOption("anual"),
        ],
    )

    tipo_periodo = ft.Dropdown(
        width=160,
        value="mes(es)",
        options=[
            ft.DropdownOption("mes(es)"),
            ft.DropdownOption("ano(s)"),
        ],
    )
    
    resultado_texto_vtf = ft.Text(
        "R$",
        color="white",
        size=22,
        weight=ft.FontWeight.BOLD,
    )

    resultado_texto_vti = ft.Text(
        "R$",
        size=22,
        weight=ft.FontWeight.BOLD,
    )

    resultado_texto_juros = ft.Text(
        "R$",
        size=22,
        weight=ft.FontWeight.BOLD,
    )

    grafico = ft.Image(
        src="",
        width=850,
        height=400,
    )

    tabela = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Período")),
            ft.DataColumn(ft.Text("Valor Investido")),
            ft.DataColumn(ft.Text("Juros")),
            ft.DataColumn(ft.Text("Montante")),
        ],
        rows=[]
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
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
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
                                                    resultado_texto_vtf,
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
                                                resultado_texto_vti,
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
                                                resultado_texto_juros,
                                            ]
                                        )
                                    )
                                ]
                            ),

                            ft.Divider(),

                            ft.Text(
                                "Evolução do Investimento",
                                size=20,
                                weight=ft.FontWeight.BOLD,
                                color="#000080",
                            ),

                            grafico,

                            ft.Divider(),

                            ft.Text(
                                "Tabela de Evolução",
                                size=20,
                                weight=ft.FontWeight.BOLD,
                                color="#000080",
                            ),

                            ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    tabela,
                                ],
                            ),
                        ]
                    )
                )
    
    def calcular_clique(e):
        valor_inicial_real = float(valor_inicial.value)
        aporte = float(valor_mensal.value)
        taxa_real = float(taxa.value) / 100
        tempo = int(periodo.value)
        
        if tipo_taxa.value == "anual":
            taxa_real = (1 + taxa_real) ** (1 / 12) - 1
            
        if tipo_periodo.value == "ano(s)":
            tempo *= 12
        
        dados = []

        monte = valor_inicial_real

        dados.append({
        "Período": 0,
        "Valor Investido": valor_inicial_real,
        "Juros": 0,
        "Montante": monte
    })
        
        for mes in range(1, tempo + 1):

            monte *= (1 + taxa_real)  
            monte += aporte           
            
            valor_investido = valor_inicial_real + (aporte * mes)
        
            juros = monte - valor_investido
        
            dados.append({
            "Período": mes,
            "Valor Investido": valor_investido,
            "Juros": juros,
            "Montante": monte
        })
        
        df = pd.DataFrame(dados)
        
        valor_total_investido = df["Valor Investido"].iloc[-1]
        total_juros = df["Juros"].iloc[-1]
        montante_final = df["Montante"].iloc[-1]

        resultado_texto_vtf.value = f"R$ {montante_final:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

        resultado_texto_vti.value = f"R$ {valor_total_investido:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

        resultado_texto_juros.value = f"R$ {total_juros:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

        tabela.rows.clear()
    
        for _, linha in df.iterrows():
            tabela.rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(
                        ft.Text(str(int(linha["Período"])))
                    ),
                    ft.DataCell(
                        ft.Text(
                            f"R$ {linha['Valor Investido']:,.2f}"
                            .replace(",", "X")
                            .replace(".", ",")
                            .replace("X", ".")
                        )
                    ),
                    ft.DataCell(
                        ft.Text(
                            f"R$ {linha['Juros']:,.2f}"
                            .replace(",", "X")
                            .replace(".", ",")
                            .replace("X", ".")
                        )
                    ),
                    ft.DataCell(
                        ft.Text(
                            f"R$ {linha['Montante']:,.2f}"
                            .replace(",", "X")
                            .replace(".", ",")
                            .replace("X", ".")
                        )
                    ),
                ]
            )
        )

        plt.figure(figsize=(10, 5))

        plt.plot(
        df["Período"],
        df["Montante"],
        label="Montante"
    )

        plt.plot(
        df["Período"],
        df["Valor Investido"],
        label="Valor Investido"
    )

        plt.xlabel("Período")
        plt.ylabel("Valor (R$)")
        plt.title("Evolução do Investimento")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()

        plt.savefig("grafico_investimento.png")
        plt.close()

        grafico.src = "grafico_investimento.png"

        resultado_container.visible = True

        page.update()

    botao_calcular = ft.Button(
       "Calcular",
       on_click=calcular_clique,
       color="#000080"
    )

    def limpar(e):
        valor_inicial.value = ""
        valor_mensal.value = ""
        taxa.value = ""
        periodo.value = ""
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