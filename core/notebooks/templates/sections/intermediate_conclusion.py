from notebooks.context import NotebookContext
from .template import SectionCommand
from notebooks.templates.structural_elements.jupyter_cell import JupyterCellCreator
from notebooks.templates.structural_elements import Templates


class IntermediateConclusionSection(SectionCommand):
    def __init__(self, conclusion_after_which: str):
        self.research_step = conclusion_after_which

    def __call__(self, ctx: NotebookContext) -> None:
        # Заголовок раздела
        ctx.cells.append(
            JupyterCellCreator.create_markdown_cell(
                "# Промежуточный вывод"
            )
        )

        # Основной блок вывода (ОДНА ячейка)
        ctx.cells.append(
            JupyterCellCreator.create_markdown_cell(
                Templates.intermediate_conclusion(self.research_step)
            )
        )
