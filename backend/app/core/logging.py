import logging
from rich.logging import RichHandler


class TerminalLogger:
    def __init__(self):
        # Создаем логгер с именем текущего модуля
        self._logger = logging.getLogger(__name__)

        # Создаем форматтер
        formatter = logging.Formatter(
            "%(asctime)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
        )

        # Настройка обработчика для терминала с подсветкой
        rich_handler = RichHandler(markup=True)
        rich_handler.setLevel(logging.DEBUG)  # Логирование от DEBUG и выше
        rich_handler.setFormatter(formatter) # Устанавливаем форматтер для обработчика

        file_handler = logging.FileHandler("app.log")
        file_handler.setLevel(logging.WARNING) # Логирование от WARNING и выше
        file_handler.setFormatter(formatter) # Устанавливаем форматтер для обработчика

        # Добавляем обработчик в логгер
        self._logger.addHandler(rich_handler)
        self._logger.addHandler(file_handler)
        self._logger.setLevel(
            logging.DEBUG
        )  # Устанавливаем уровень логирования для логгера

    def get_logger(self):
        # Возвращаем логгер
        return self._logger


logger = TerminalLogger().get_logger()
