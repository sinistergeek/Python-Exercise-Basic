import logging

log_file = "my.log"

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

ch = logging.handlers.TimeRotatingFileHandler(log_file,when='M',backupCount=2)
ch.setLevel(logging.INFO)
ch.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)-10s - %(message)s'))
logger.addHandler(ch)

log = logging.getLogger(__name__)
log.debug('debug')
log.info('info')
log.warning('warning')
log.error('error')
log.critical('critical')

from name_function import get_formattted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name.")
    if last  == 'q':
        break
    formatted_name = get_formatted_name(first,last)
    print(f"\tNeatly formatted name:{formatted_name}.")
