from io import StringIO
from configparser import ConfigParser


CONFIG_FILE_CONTENT = """
[test]
var = value
second var = second %(var)s
[test2]
third var = third value
"""
CONFIG_FILE = StringIO(CONFIG_FILE_CONTENT)
CONFIG_FILE.seek(0)


def test_read_config():
    from syphon.config import read_config

    result = read_config(CONFIG_FILE)

    assert isinstance(result, ConfigParser)
    assert result.options('test') == ['var', 'second var', 'default var']
    assert result.get('test', 'var') == 'value'
    assert result.get('test', 'second var') == 'second value'
    assert result.get('test', 'default var') == 'default value'
    assert result.options('test2') == ['third var', 'default var']
    assert result.get('test2', 'third var') == 'third value'
    assert result.get('test2', 'default var') == 'default value'
