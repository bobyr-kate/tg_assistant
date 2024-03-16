import logging

my_logger = logging.getLogger('my_logger')

# Настройки для лога
logging.basicConfig(
    level = logging.INFO,
    format = '%(name)s => %(levelname)s => %(message)s => %(asctime)s => %(filename)s => %(lineno)d',
    datefmt = '%d.%m.%Y %H:%M:%S',
    filename = 'my_first_log',
    filemode = 'a'
)

# Настройка форматирования для обработчика
my_formatter = logging.Formatter(
    'Информирую, что тут ошибка: %(name)s => %(levelname)s => %(message)s => %(asctime)s => %(filename)s'
)
# Создаем обработчик
my_handler = logging.StreamHandler()
# Определяем уровень, с которого начинаем перехватывать сообщения
my_handler.setLevel(logging.ERROR)
# Применяем свое форматирование к обработчику
my_handler.setFormatter(my_formatter)

# Добавляем обработчика к логированию
my_logger.addHandler(my_handler)


class My_Filter(logging.Filter):
    """Base class to filter whether or not message should be logged """

    def filter(self, record):
        """Returns False if battle finished with a draw"""
        return not (record.msg.lower().startswith('test'))

# Добавляем фильтр к логированию
my_logger.addFilter(My_Filter())


# Тест сообщений
my_logger.critical('CRITICAL ERROR')
my_logger.error("first error")
my_logger.warning("warning")
my_logger.info("info")
my_logger.debug("debug")
my_logger.error("second error")
my_logger.error("test error")

try:
    result = 5 / 0 
except ZeroDivisionError as e:
    my_logger.error(f'Error {e}')


