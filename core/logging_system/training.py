import logging
import sys
from contextlib import contextmanager
from typing import Iterator

from .writer import LoggerWriter
from settings import LOG_DIR, LOG_TRAINING_INFO, LOG_TRAINING_DEBUG


class TrainingLogger:
    def __init__(self) -> None:
        self.logger = logging.getLogger("training")
        self._configure()

    def _configure(self) -> None:
        if self.logger.handlers:
            return

        LOG_DIR.mkdir(exist_ok=True)

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(
            self._create_handler(LOG_TRAINING_INFO, logging.INFO, formatter)
        )
        self.logger.addHandler(
            self._create_handler(LOG_TRAINING_DEBUG, logging.DEBUG, formatter)
        )

    @staticmethod
    def _create_handler(path, level, formatter):
        handler = logging.FileHandler(path, encoding="utf-8")
        handler.setLevel(level)
        handler.setFormatter(formatter)
        return handler

    def info(self, message, *args) -> None:
        self.logger.info(message, *args)

    def debug(self, message, *args) -> None:
        self.logger.debug(message, *args)

    def exception(self, message, *args) -> None:
        self.logger.exception(message, *args)

    @contextmanager
    def capture_output(self) -> Iterator[None]:
        original_stdout = sys.stdout
        original_stderr = sys.stderr

        sys.stdout = LoggerWriter(
            self.logger,
            logging.DEBUG,
        )
        sys.stderr = LoggerWriter(
            self.logger,
            logging.DEBUG,
        )

        try:
            yield
        finally:
            sys.stdout = original_stdout
            sys.stderr = original_stderr
