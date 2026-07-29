# from typing import List
#
# from structural_elements.jupyter_cell import JupyterCellCreator


# class ContentCreator:
#     def __init__(self, shell):
#         self.cell_creator = JupyterCellCreator(shell)
#
#     def create(self, content: List[str]) -> None:
#         for item in reversed(content):
#             self.cell_creator.create_cell(code=item)