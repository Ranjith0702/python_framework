from configparser import ConfigParser


def config_read(category, key):
    config = ConfigParser()
    config.read("configurations/config.ini")
    return config.get(category, key)
