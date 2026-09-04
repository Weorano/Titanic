import textwrap

from .template import SectionCommand
from notebooks.context import NotebookContext
from notebooks.templates.structural_elements.jupyter_cell import JupyterCellCreator


class ManualSection(SectionCommand):
    def __call__(self, ctx: NotebookContext) -> None:
        ctx.cells.append(
            JupyterCellCreator.create_markdown_cell(
                "ЕСЛИ КОЛОНКИ ТАБЛИЦЫ В НУЖНОМ ФОРМАТЕ ЗАПУСТИТЕ "
                "~/pipilines/create_preprocessing_body.py"
            ),
        )
        ctx.cells.append(
            JupyterCellCreator.create_code_cell(
                textwrap.dedent("""
                    pipline_stage_body_create = PreprocessingBodyPipeline()
                    
                    pipline_stage_body_create.run(
                        loaded_dataframes = {
                            'df_name': dataframe,
                        }
                    )
                """)
            ),
        )

