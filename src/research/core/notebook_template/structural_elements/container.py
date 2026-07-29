from typing import List, Dict, Any

from .jupyter_cell import JupyterCellCreator
from ..style_components.custom_element_border import FrameStrategyFactory


class ContainerBuilder:
    def build(
        self,
        container_title: str,
        content_cells: List[Dict[str, Any]],
        frame_type: str = "default",
        reference_to_visualization: bool = False,
    ) -> List[Dict[str, Any]]:

        cells = [
            JupyterCellCreator.create_markdown_cell(
                self.get_upper_frame(
                    container_title,
                    frame_type,
                )
            )
        ]

        if reference_to_visualization:
            cells.append(
                JupyterCellCreator.create_markdown_cell(
                    self.get_reference_to_visualization()
                )
            )

        cells.extend(content_cells)

        cells.append(
            JupyterCellCreator.create_markdown_cell(
                self.get_lower_frame(frame_type)
            )
        )

        return cells

    # Убрать нахуй - теперь можем вставлять отдельно
    @staticmethod
    def get_reference_to_visualization() -> str:
        return (
            '<font color="green">'
            '**Вывод по гистограмме и "ящику с усами" 1 из раздела "Визуализация":**'
            '</font>'
        )

    @staticmethod
    def get_upper_frame(
            container_title: str,
            frame_type: str = 'default'
    ) -> str:
        strategy = FrameStrategyFactory.get_strategy(frame_type)

        size = 11 * len(container_title) + strategy.get_extra_size()
        title_tag = strategy.get_title_tag()
        border_color = strategy.get_border_color()

        return (
            f'<div class="border" style="'
            f'border: 2px solid {border_color};'
            f'width: 99%;'
            f'height: auto;'
            f'margin-top: 20px;'
            f'border-bottom: none;'
            f'"> '
            f'<{title_tag} class="legend" style="'
            f'margin-top: -8px;'
            f'margin-left: 10px;'
            f'padding-left: 15px;'
            f'background: white;'
            f'width: {size}px;'
            f'font-weight: 600;'
            f'">{container_title}</{title_tag}>'
            f'</div>'
        )

    @staticmethod
    def get_lower_frame(
            frame_type: str = 'default'
    ) -> str:
        border_color = '#D84315' if frame_type == 'pipline' else 'black'

        return (
            f'<div class="border" style="'
            f'border: 2px solid {border_color};'
            f'width: 99%;'
            f'height: 10px;'
            f'border-top: none;'
            f'"></div>'
        )