# from typing import List
#
# from structural_elements.jupyter_cell import JupyterCellCreator
# from style_components.custom_element_border import FrameStrategyFactory
#
#
# class BlockStructurer:
#     def get_block(
#             self,
#             block_title: str,
#             frame_type: str = 'default',
#             content_template: str = None,
#             block_content: str = None,
#             reference_to_visualization: bool = False,  # Отвечает за пометку "Вывод по гистограмме"
#     ) -> List[str]:
#         block_items = [
#             JupyterCellCreator.create_markdown_cell(
#                 self.get_upper_frame(block_title, frame_type)
#             )
#         ]
#
#         if reference_to_visualization:
#             block_items.append(
#                 JupyterCellCreator.create_markdown_cell(
#                     self.get_reference_to_visualization()
#                 )
#             )
#
#         if reference_to_visualization:
#             block_items.append(self.get_reference_to_visualization())
#
#         if content_template:
#             block_items.extend(
#                 self.get_body_with_template(
#                     template_name=content_template
#                 )
#             )
#         else:
#             block_items.append(block_content)
#
#         block_items.append(self.get_lower_frame())
#
#         return block_items
#
#     @staticmethod
#     def get_reference_to_visualization() -> str:
#         return (
#             '<font color="green">'
#             '**Вывод по гистограмме и "ящику с усами" 1 из раздела "Визуализация":**'
#             '</font>'
#         )
#
#     @staticmethod
#     def get_upper_frame(
#             block_title: str,
#             frame_type: str = 'default'
#     ) -> str:
#         strategy = FrameStrategyFactory.get_strategy(frame_type)
#
#         size = 11 * len(block_title) + strategy.get_extra_size()
#         title_tag = strategy.get_title_tag()
#         border_color = strategy.get_border_color()
#
#         return (
#             f'<div class="border" style="'
#             f'border: 2px solid {border_color};'
#             f'width: 99%;'
#             f'height: auto;'
#             f'margin-top: 20px;'
#             f'border-bottom: none;'
#             f'"> '
#             f'<{title_tag} class="legend" style="'
#             f'margin-top: -8px;'
#             f'margin-left: 10px;'
#             f'padding-left: 15px;'
#             f'background: white;'
#             f'width: {size}px;'
#             f'font-weight: 600;'
#             f'">{block_title}</{title_tag}>'
#             f'</div>'
#         )
#
#     @staticmethod
#     def get_lower_frame(
#             frame_type: str = 'default'
#     ) -> str:
#         border_color = '#D84315' if frame_type == 'pipline' else 'black'
#
#         return (
#             f'<div class="border" style="'
#             f'border: 2px solid {border_color};'
#             f'width: 99%;'
#             f'height: 10px;'
#             f'border-top: none;'
#             f'"></div>'
#         )
#
#     @staticmethod
#     def get_body_with_template(template_name: str = None) -> List[str]:
#         if template_name == 'general_conclusion':
#             return [
#                 '**Аномалии:** \n'
#                 '- Не обнаружены \n'
#                 '\n'
#                 '**Причины:** \n'
#                 '- a. \n'
#                 '\n'
#                 '**Методы устранения:** \n'
#                 '- a \n'
#                 '--- \n'
#                 '\n'
#                 '**Дубликаты:** \n'
#                 '- Отсутствуют \n'
#                 '\n'
#                 '**Причины:** \n'
#                 '- a \n'
#                 '\n'
#                 '**Методы устранения:** \n'
#                 '- a \n'
#             ]
#         elif template_name == 'data_optimization':
#             return [
#                 'Обработка',
#                 '**Почему типы данных были изменены?**',
#                 '- `total_images` - никто не будет добавлять огромное количество'
#                 'фотографий к недвижимости, поэтому мы ограничились 255 фотографиями.'
#                 'Само количество фотографий не может быть отрицательным;'
#             ]
#         else:
#             return []