from .template import SectionCommand
from ..context import NotebookContext
from ..structural_elements import Templates
from ..structural_elements.jupyter_cell import JupyterCellCreator


class PreprocessingSection(SectionCommand):
    def __call__(self, ctx: NotebookContext) -> None:
        # Добавляем название большого раздела
        ctx.cells.append(
            JupyterCellCreator.create_markdown_cell(
                "# Поверхностная предобработка данных"
            )
        )

        for df_name, dataframe in ctx.loaded_dataframes.items():
            for column in dataframe.columns:
                # Добавляем название секции
                ctx.cells.append(
                    JupyterCellCreator.create_markdown_cell(
                        f"## DF @{df_name} `{column}`."
                    )
                )

                # Добавляем блок `Общий вывод`
                ctx.cells.extend(
                    ctx.container_builder.build(
                        container_title='Общий вывод',
                        content_cells=[
                            JupyterCellCreator.create_markdown_cell(
                                Templates.general_conclusion()
                            )
                        ]
                    )
                )

                # Добавляем блок `Визуализация`
                ctx.cells.extend(
                    ctx.container_builder.build(
                        container_title='Визуализация данных',
                        content_cells=[
                            JupyterCellCreator.create_markdown_cell(
                                '**Гистограмма и "ящик с усами" 1**'
                            ),
                            JupyterCellCreator.create_code_cell(
                                ctx.visualization_code_structurer.get_chart_code(
                                    table_name=df_name,
                                    table_column_name=column,
                                    data_for_chart=dataframe[column]
                                )
                            ),
                        ],
                    )
                )

                # Добавляем блок `Метрики`
                content_cells = []

                if "id" in column:
                    content_cells.append(
                        JupyterCellCreator.create_code_cell(
                            Templates.metrics_for_id_parameter(df_name)
                        )
                    )
                else:
                    content_cells.append(
                        JupyterCellCreator.create_code_cell(
                            Templates.metrics_for_digit_parameter(df_name, column)
                        )
                    )
                    content_cells.append(
                        JupyterCellCreator.create_code_cell(
                            Templates.metrics_for_timeseries_parameter(df_name, column)
                        )
                    )

                ctx.cells.extend(
                    ctx.container_builder.build(
                        container_title="Метрики",
                        content_cells=content_cells,
                    )
                )

                # Добавляем блок `Устранение пропусков`
                ctx.cells.extend(
                    ctx.container_builder.build(
                        container_title="Устранение пропусков",
                        reference_to_visualization=True,
                        content_cells=[
                            JupyterCellCreator.create_markdown_cell(
                                '*Как видно из графика, здесь и сейчас сложно'
                                'проанализировать данный параметр, потому что'
                                'можно принять не осторожное решение, следовательно,'
                                'постараемся изучить этот параметр более детально в'
                                'разделе EDA.*'
                            )
                        ],
                    )
                )

                # Добавляем блок `Устранение дубликатов`
                ctx.cells.extend(
                    ctx.container_builder.build(
                        container_title="Устранение дубликатов",
                        content_cells=[
                            JupyterCellCreator.create_markdown_cell(
                                '*Обработка*'
                            )
                        ],
                    )
                )

                # Добавляем блок `Устранение аномалий`
                ctx.cells.extend(
                    ctx.container_builder.build(
                        container_title="Устранение аномалий",
                        reference_to_visualization=True,
                        content_cells=[
                            JupyterCellCreator.create_markdown_cell(
                                '*Здесь и сейчас сложно проанализировать возможные'
                                'аномалии, потому что нужно смотреть параметр более'
                                'детально. Перенесём в раздел EDA.*'
                            )
                        ],
                    )
                )

        # Добавляем блок `Оптимизация данных`
        ctx.cells.extend(
            ctx.container_builder.build(
                container_title='Оптимизация данных',
                frame_type="title",
                content_cells=[
                    JupyterCellCreator.create_markdown_cell(
                        Templates.data_optimization()
                    )
                ]
            )
        )
