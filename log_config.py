import logging

logger = logging.getLogger()
logging.getLogger('matplotlib').setLevel(logging.WARNING)



logger.setLevel(logging.DEBUG)

#logp will log all processes and loge will log all warnings and errors

logp = logging.FileHandler("logp.log", mode="w")
loge = logging.FileHandler("loge.log", mode ="w")

logp.setLevel(logging.DEBUG)
loge.setLevel(logging.WARNING)

logp.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
loge.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

logger.addHandler(logp)
logger.addHandler(loge)