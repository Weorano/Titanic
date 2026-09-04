from .template import SectionCommand
from notebooks.context import NotebookContext
from notebooks.templates.structural_elements.jupyter_cell import JupyterCellCreator


class EdaSection(SectionCommand):
    def __call__(self, ctx: NotebookContext) -> None:
        # Заголовок раздела
        ctx.cells.append(
            JupyterCellCreator.create_markdown_cell(
                "### Исследовательский анализ (EDA)"
            )
        )

        for df_name, dataframe in ctx.loaded_dataframes.items():
            # Заголовок колонки (через единый инструмент)
            ctx.cells.append(
                JupyterCellCreator.create_markdown_cell(
                    f"#### Анализ DF @{df_name} `column`."
                )
            )

            # Контейнер блока анализа
            ctx.cells.extend(
                ctx.container_builder.build(
                    container_title="Исследование",
                    content_cells=[
                        JupyterCellCreator.create_code_cell(
                            "print('TODO: исследование')"
                        )
                    ],
                )
            )
