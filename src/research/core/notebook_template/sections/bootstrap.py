import textwrap

from .template import SectionCommand
from ..context import NotebookContext
from ...researchers_tools.bootstrap import Bootstrap
from ..structural_elements import Templates
from ..structural_elements.jupyter_cell import JupyterCellCreator


class BootstrapSection(SectionCommand):
    def __call__(self, ctx: NotebookContext) -> None:
        ctx.cells.append(
            JupyterCellCreator.create_markdown_cell(
                "# Настройка инструментов"
            )
        )

        ctx.cells.extend(
            ctx.container_builder.build(
                container_title="Инициализация среды",
                content_cells=[
                    JupyterCellCreator.create_markdown_cell(
                        "*Импортируем библиотеки для работы с данными.*"
                    ),
                    JupyterCellCreator.create_code_cell(
                        Bootstrap.build_tools_for_working_bootstrap_cell()
                    )
                ]
            )
        )

        ctx.cells.extend(
            ctx.container_builder.build(
                container_title="Настройка визуализации",
                content_cells=[
                    JupyterCellCreator.create_markdown_cell(
                        "*Настройка визуализации.*"
                    ),
                    JupyterCellCreator.create_code_cell(
                        Bootstrap.build_graphical_visualization_bootstrap_cell()
                    )
                ]
            )
        )

        datasets = ctx.config["datasets_paths"]

        code_lines = []
        markdown_lines = []

        for name, path in datasets.items():
            code_lines.append(
                f'{name} = pd.read_csv("{path}")'
            )

            markdown_lines.append(
                f'**Наименование:** {name}.<br>'
                f'**Путь к файлу:** {path} <br><br>'
            )

        code = "\n".join(code_lines)
        markdown = "\n".join(markdown_lines)

        ctx.cells.extend(
            ctx.container_builder.build(
                container_title="Загрузка и настройка ресурсов",
                content_cells=[
                    JupyterCellCreator.create_markdown_cell(markdown),
                    JupyterCellCreator.create_code_cell(code),
                    JupyterCellCreator.create_markdown_cell(
                        Templates.load_data()
                    ),
                    JupyterCellCreator.create_markdown_cell(
                        '*Переименуем столбцы таблиц под описанную выше структуру.*'
                    ),
                    JupyterCellCreator.create_code_cell(
                        'data.head(0)'
                    ),
                    JupyterCellCreator.create_code_cell(
                        textwrap.dedent("""
                            data = data.rename(columns={
                                'Начало нагрева дугой': 'start_time',
                            })
                        
                            data.head(0)
                        """).strip()
                    )
                ]
            )
        )