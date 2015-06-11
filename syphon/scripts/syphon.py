import argparse

from syphon.config import read_config


def parse_arguments():
    parser = argparse.ArgumentParser(description='Syphon executor')
    parser.add_argument('config_file', metavar='config.ini', help='The configuration file')
    return parser.parse_args()


def main():
    args = parse_arguments()
    result = read_config(open(args.config_file, 'r'))
    for section in result.sections():
        print(section)
        print(result.options(section))
