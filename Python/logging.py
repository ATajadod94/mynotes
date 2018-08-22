import logging

logging.info('hi')
logging.warning('oh no')

logging.basicCongif()

FORMAT = '[%(actime)s] - [%(levelname)s] - [%(funcName)s] - %(message)s'
logging.basicCongif(
    level = logging.INFO() % all caps! (give us info and above)
    format = FORMAT
)
