import logconf

logger = logconf.getLogger(__name__)
logger.setLevel(logconf.ERROR)

logger.log(logconf.DEBUG, 'DEBUG 訊息')
logger.log(logconf.INFO, 'INFO 訊息')
logger.log(logconf.WARNING, 'WARNING 訊息')
logger.log(logconf.ERROR, 'ERROR 訊息')
logger.log(logconf.CRITICAL, 'CRITICAL 訊息')


