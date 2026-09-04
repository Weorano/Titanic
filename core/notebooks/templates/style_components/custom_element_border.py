from abc import ABC, abstractmethod

class FrameTypeStrategy(ABC):
    @abstractmethod
    def get_border_color(self) -> str:
        pass

    @abstractmethod
    def get_title_tag(self) -> str:
        pass

    @abstractmethod
    def get_extra_size(self) -> int:
        pass


class DefaultFrameStrategy(FrameTypeStrategy):
    def get_border_color(self) -> str:
        return 'black'

    def get_title_tag(self) -> str:
        return 'p'

    def get_extra_size(self) -> int:
        return 0


class TitleFrameStrategy(FrameTypeStrategy):
    def get_border_color(self) -> str:
        return 'black'

    def get_title_tag(self) -> str:
        return 'h4'

    def get_extra_size(self) -> int:
        return 45


class PipelineFrameStrategy(FrameTypeStrategy):
    def get_border_color(self) -> str:
        return '#D84315'

    def get_title_tag(self) -> str:
        return 'p'

    def get_extra_size(self) -> int:
        return 0


class FrameStrategyFactory:
    @staticmethod
    def get_strategy(frame_type: str) -> FrameTypeStrategy:
        strategies = {
            'default': DefaultFrameStrategy(),
            'title': TitleFrameStrategy(),
            'pipeline': PipelineFrameStrategy(),
        }

        return strategies.get(frame_type, DefaultFrameStrategy())