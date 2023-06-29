import logging

logging.basicConfig(filename='log.txt', level=logging.INFO, filemode='w', format='%(asctime)s:%(levelname)s:%(message)s')
logging.debug("This is debug message")
logging.info("This is info")
logging.warning("This is warning")
logging.error("This is error message")
logging.fatal("This is fatal message")