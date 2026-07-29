from abc import abstractmethod, ABC
from src.research.core.notebook_template.context import NotebookContext


class SectionCommand(ABC):
    @abstractmethod
    def __call__(self, ctx: NotebookContext) -> None:
        raise NotImplementedError