import configparser
import pygame


def get_config_value(section,key):

    config = configparser.ConfigParser()
    config.read('config.ini')
    return config.get(section, key)


def test():

    f = VALUE.find(',')
    if f > 0:
        r = VALUE.strip('(')
        r = r.strip(')')
        x = tuple(map(int, r.split(',')))


if __name__ == '__main__':
    VALUE = get_config_value('COLOURS', 'blue')
    print(VALUE)
    test()