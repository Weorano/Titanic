from .template import SectionCommand
from notebooks.context import NotebookContext
from notebooks.templates.structural_elements.jupyter_cell import JupyterCellCreator


class MainInfoSection(SectionCommand):
    def __call__(self, ctx: NotebookContext) -> None:
        ctx.cells.append(
            JupyterCellCreator.create_markdown_cell(
                "# Общая информация"
            )
        )

        ctx.cells.append(
            JupyterCellCreator.create_markdown_cell(
                "**Название таблицы** "
            )
        )

        ctx.cells.append(
            JupyterCellCreator.create_code_cell(
                "overview.py.info()"
            )
        )

        ctx.cells.append(
            JupyterCellCreator.create_code_cell(
                "msno.matrix(\n"
                "    autos_data.sample(25000),\n"
                "    color=(0, 0.5, 0),\n"
                "    fontsize=18,\n"
                "    sparkline=False,\n"
                "    figsize=(20, 20)\n"
                ")\n"
                "\n"
                "plt.figure(figsize=(15,7))\n"
                "\n"
                "cmap = sns.cubehelix_palette(as_cmap=True, light=.9)\n"
                "\n"
                "sns.heatmap(\n"
                    "bulk_volume.isna().transpose(),\n"
                    "cmap=cmap,\n"
                    "cbar_kws={'label': 'Пропущенные значения'}\n"
                ");\n"
            )
        )

        ctx.cells.append(
            JupyterCellCreator.create_markdown_cell(
                "*Посмотрим есть ли зависимость между пропусками.*"
            )
        )

        ctx.cells.append(
            JupyterCellCreator.create_code_cell(
                "msno.heatmap(autos_data, cmap='Greens')"
            )
        )