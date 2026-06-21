# Calculadora de Juros Compostos

## Instalação

### Utilizaremos o UV por ser uma ferramenta moderna que substitui várias ferramentas tradicionais de uma só vez.
[Instalar uv](https://docs.astral.sh/uv/getting-started/installation/).

Instalando o Flet:

```bash
uv add 'flet[all]'
```

Criando a Estrutura do Projeto:

```bash
uv run flet create
```

Inicializando o Projeto:

```bash
uv run flet run
```

## Componentes e Ferramentas do Código

Cria uma caixinha de entrada para receber as informações digitadas pelo usuário
(Valor Inicial, Valor Final, Taxa de Juros, Período)

```bash
ft.TextField()
```

Cria uma caixinha com uma lista de opções para a escolha do usuário

```bash
ft.Dropdown()
```

Opções da caixa de seleção Dropdown
(mensal, anual, ano(s), mes(ses))

```bash
ft.DropdownOption()
```

Organiza outros componentes na horizontal, ou seja, um do lado do outro em uma linha

```bash
ft.Row()
```

Organiza outros componentes na vertical, ou seja, um abaixo do outro em uma coluna

```bash
ft.Column()
```

Serve para listar os componentes que ficarão organizados em determinada linha ou coluna

```bash
controls=[
```

Organiza os componentes em um container na tela

```bash
ft.Container()
```

Cria um botão

```bash
ft.Button()
```

Dá espaçamento máximo entre os componentes, deixando-os em pontas opostas na tela

```bash
alignment=ft.MainAxisAlignment.SPACE_BETWEEN
```
