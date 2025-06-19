import logging
import pandas as pd
from time import time 

# create logger

logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# create file handler which logs even debug messages
log_file_name = pd.Timestamp('today').strftime('%Y-%m-%d') + "_" + str(round(time())) + ".log"

fh = logging.FileHandler(log_file_name)
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter) # Add formatter to the handlers
logger.addHandler(fh) # add the handlers to the logger

logger.info("Info logged.")
logger.debug("Debugging log.")