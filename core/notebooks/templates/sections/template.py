from abc import abstractmethod, ABC
from notebooks.context import NotebookContext


class SectionCommand(ABC):
    @abstractmethod
    def __call__(self, ctx: NotebookContext) -> None:
        raise NotImplementedError