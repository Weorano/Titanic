import textwrap

from .template import SectionCommand
from ..context import NotebookContext
from ..structural_elements.jupyter_cell import JupyterCellCreator
from ..structural_elements.templates import Templates


class HeaderSection(SectionCommand):
    def __call__(self, ctx: NotebookContext) -> None:
        datasets = ctx.config["datasets_paths"]

        data_info_markdown_blocks = []
        data_structure_markdown_lines = []

        for name, path in datasets.items():
            data_info_markdown_blocks.append(
                f"""
                **Предоставитель данных:** «ООО КОМПАНИЯ»  
                **Наименование:** данные о {name}  
                **Формат файла с данными:** csv  
                **Путь к файлу:** {path}  
                """.strip()
            )

        for df_name, dataframe in ctx.loaded_dataframes.items():
            data_structure_markdown_lines.append(
                f'- **{df_name}**'
            )

            for column in dataframe.columns:
                data_structure_markdown_lines.append(
                    f'- `{column}` — описание;'
                )

            data_structure_markdown_lines.append("<br><br>")

        data_info_markdown = "\n\n".join(data_info_markdown_blocks)
        data_structure_markdown = "\n".join(data_structure_markdown_lines)

        final_markdown = "\n\n".join([
            Templates.header_title(),
            Templates.header_project_description_examples(),
            Templates.header_goal_section(),
            Templates.header_source_data_section_title(),
            data_info_markdown,
            textwrap.dedent("""
                **Изначальная структура данных (без обработки):**
            """).strip(),
            data_structure_markdown,
            Templates.header_action_plan_section(),
        ])

        ctx.cells.append(
            JupyterCellCreator.create_markdown_cell(
                final_markdown
            )
        )