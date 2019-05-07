import logconf

logconf.basicConfig(filename ='openhome.log')

logger = logconf.getLogger(__name__)
logger.addHandler(logconf.FileHandler('errors.log'))

logger.log(logconf.ERROR, 'ERROR 訊息')


