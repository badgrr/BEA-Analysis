import pybea as api

config = configparser.ConfigParser()
config.read('config.ini')

USER_ID: str = config['KEYS']['USER_ID']