import logging, logconf
import logging.config

logging.config.dictConfig(logconf.LOGGING_CONFIG)

# 建立logger
logger = logging.getLogger('simple_example')

# 應用程式的程式碼
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')
