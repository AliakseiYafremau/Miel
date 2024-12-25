import logging
from rich.logging import RichHandler


class TerminalLogger:
    def __init__(self):
        # Создаем логгер с именем текущего модуля
        self._logger = logging.getLogger(__name__)

        # Настройка обработчика для терминала с подсветкой
        rich_handler = RichHandler()
        rich_handler.setLevel(logging.DEBUG)  # Логирование от DEBUG и выше
        formatter = logging.Formatter(
            "%(asctime)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
        )
        rich_handler.setFormatter(formatter)

        # Добавляем обработчик в логгер
        self._logger.addHandler(rich_handler)
        self._logger.setLevel(
            logging.DEBUG
        )  # Устанавливаем уровень логирования для логгера

    def get_logger(self):
        # Возвращаем логгер
        return self._logger


logger = TerminalLogger().get_logger()
