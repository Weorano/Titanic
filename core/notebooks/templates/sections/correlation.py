from .template import SectionCommand
from notebooks.context import NotebookContext
from notebooks.templates.structural_elements.jupyter_cell import JupyterCellCreator
from notebooks.templates.structural_elements import Templates

class CorrelationSection(SectionCommand):
    def __call__(self, ctx: NotebookContext) -> None:
        # Добавляем название большого раздела
        ctx.cells.append(
            JupyterCellCreator.create_markdown_cell(
                "# Корреляционный анализ"
            )
        )

        # Добавляем блок `Heatmap`
        # Добавляем блок "после матрицы мы обратим детальное внимание на".
        ctx.cells.extend(
            ctx.container_builder.build(
                container_title='Heatmap по целевому признаку',
                content_cells=[
                    JupyterCellCreator.create_code_cell(
                        Templates.heatmap_code()
                    ),
                    JupyterCellCreator.create_markdown_cell(
                        "**Вывод:**"
                    ),
                    JupyterCellCreator.create_markdown_cell(
                        Templates.correlation_conclusion()
                    )
                ],
            )
        )

        # Добавляем блок-пример `Зависимость W1 от W2`
        ctx.cells.extend(
            ctx.container_builder.build(
                container_title=(
                    'DF @Коровы фермера зависимость '
                    '<code>fat_content_percent</code> '
                    'от <code>pasture_type</code>'
                ),
                content_cells=[
                    JupyterCellCreator.create_markdown_cell(
                        '*Scatter или hist*'
                    )
                ],
            )
        )