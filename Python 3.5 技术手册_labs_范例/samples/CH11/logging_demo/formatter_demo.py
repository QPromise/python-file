import logconf, sys


formatter = logconf.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler = logconf.StreamHandler(sys.stderr)
handler.setFormatter(formatter)

logger = logconf.getLogger(__name__)
logger.addHandler(handler)
logger.log(logconf.ERROR, '發生了 XD 錯誤')