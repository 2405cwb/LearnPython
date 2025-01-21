# author: cwb
# date: 2025/1/21
# author: cwb
# date: 2025/1/21
import logging

def log(str:'msg',level:'等级')->logging:
    logging.basicConfig(
        filename = 'log.txt',filemode='w',format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.DEBUG
    )
    for i in range(22):
        if level== logging.DEBUG:
            logging.debug(str)