from .template import SectionCommand
from ..context import NotebookContext
from ..structural_elements.jupyter_cell import JupyterCellCreator


class InDepthPreprocessingSection(SectionCommand):
    def __call__(self, ctx: NotebookContext) -> None:
        # Заголовок секции
        ctx.cells.append(
            JupyterCellCreator.create_markdown_cell(
                "# Углубленная предобработка данных"
            )
        )

        for df_name, dataframe in ctx.loaded_dataframes.items():
            for column in dataframe.columns:
                # Заголовок колонки
                ctx.cells.append(
                    JupyterCellCreator.create_markdown_cell(
                        f"## DF @{df_name} `{column}`."
                    )
                )

                # Устранение пропусков
                ctx.cells.extend(
                    ctx.container_builder.build(
                        container_title="Устранение пропусков",
                        reference_to_visualization=True,
                        content_cells=[
                            JupyterCellCreator.create_markdown_cell("Устранение")
                        ],
                    )
                )

                # Устранение аномалий
                ctx.cells.extend(
                    ctx.container_builder.build(
                        container_title="Устранение аномалий",
                        reference_to_visualization=True,
                        content_cells=[
                            JupyterCellCreator.create_markdown_cell("Устранение")
                        ],
                    )
                )

                # Устранение выбросов
                ctx.cells.extend(
                    ctx.container_builder.build(
                        container_title="Устранение выбросов",
                        reference_to_visualization=True,
                        content_cells=[
                            JupyterCellCreator.create_markdown_cell("Устранение")
                        ],
                    )
                )

                # Поиск аномалий
                ctx.cells.extend(
                    ctx.container_builder.build(
                        container_title="Поиск аномалий",
                        reference_to_visualization=True,
                        content_cells=[
                            JupyterCellCreator.create_markdown_cell("Поиск")
                        ],
                    )
                )