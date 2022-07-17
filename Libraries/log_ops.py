import logging

for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

logging.basicConfig(filename='Logs/Audit.log', level=logging.DEBUG)


def add_to_log(message:str):
    logging.debug(msg=message)
