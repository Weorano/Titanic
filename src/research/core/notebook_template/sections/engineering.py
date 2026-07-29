import textwrap

from ..context import NotebookContext
from .template import SectionCommand
from ..structural_elements.jupyter_cell import JupyterCellCreator
from ..structural_elements import Templates


class EngineeringSection(SectionCommand):
    def __call__(self, ctx: NotebookContext) -> None:
        # Добавляем заголовок раздела
        ctx.cells.append(
            JupyterCellCreator.create_markdown_cell(
                "# Инженерия признаков (feature engineering)"
            )
        )

        # Добавляем блок `Единичная инженерия`
        ctx.cells.extend(
            ctx.container_builder.build(
                container_title="Единичная инженерия",
                content_cells=[
                    JupyterCellCreator.create_code_cell(
                        textwrap.dedent("""
                            print('Размер до трансформации', data.shape)
      
                            data.head(0)
    
                            data[[
                                'square_meter_price', 'day_week_publication', 'month_publication',
                                'year_publication', 'floor_type', 'cityCenters_nearest_km'
                            ]].sample(3)
                            
                            print('Размер после трансформации', data.shape)

                            data.head(0)
                        """).strip()
                    )
                ],
            )
        )

        # Добавляем блок `Масштабная инженерия`
        ctx.cells.extend(
            ctx.container_builder.build(
                container_title="Масштабная инженерия",
                content_cells=[
                    JupyterCellCreator.create_markdown_cell(
                        '*Соединим все таблицы в одну. Начнём с объёма сыпучих материалов:*'
                    ),
                    JupyterCellCreator.create_code_cell(
                        Templates.big_engineering()
                    ),
                    JupyterCellCreator.create_markdown_cell(
                        '<b style="color: green;">В данном коде мы использовали'
                        ' `left join` для того, чтобы была возможность проверить'
                        ' гипотезу о том, что 275 значений легировали без добавления'
                        ' сыпучих материалов вообще. Сойдёмся на таком исходе: если'
                        ' после соединения 275 значений не перестанут быть пустыми'
                        ' хотя бы в одной из ячеек проволочных материалов - удалим их.<b>'
                    ),
                ],
            )
        )


