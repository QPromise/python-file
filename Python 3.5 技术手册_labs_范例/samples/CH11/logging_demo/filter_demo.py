import logconf, sys

logger = logconf.getLogger(__name__)
logger.addFilter(lambda record: 'Orz' in record.msg)

logger.log(logconf.ERROR, '發生了 XD 錯誤')
logger.log(logconf.ERROR, '發生了 Orz 錯誤')