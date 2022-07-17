import configparser

config = configparser.ConfigParser()
config.read(filenames='Configuration/config.ini')


def get_base_api_url() -> str:
    return config.get('common', 'BaseApiURL')


def get_base_web_url() -> str:
    return config.get('common', 'BaseWebURL')


def get_valid_user() -> str:
    return config.get('sauce_labs', 'ValidUserName')


def get_invalid_user() -> str:
    return config.get('sauce_labs', 'InvalidUserName')


def get_password() -> str:
    return config.get('sauce_labs', 'Password')
