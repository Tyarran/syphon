from configparser import ConfigParser


def read_config(file_like_object):
    defaults = {'default var': 'default value'}
    parser = ConfigParser(defaults=defaults)
    parser.read_file(file_like_object)
    return parser
