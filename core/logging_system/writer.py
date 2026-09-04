import logging
from io import TextIOBase


class LoggerWriter(TextIOBase):
    def __init__(
        self,
        logger: logging.Logger,
        level: int,
    ) -> None:
        super().__init__()
        self.logger = logger
        self.level = level

    def write(self, message: str) -> int:
        message = message.strip()

        if message:
            self.logger.log(self.level, message)

        return len(message)

    def flush(self) -> None:
        pass