from .utils.conf import Conf

settings = Conf('NODE', {
    'PATH': 'node',
    'VERSION_COMMAND': '--version',
    'VERSION_FILTER': lambda version: tuple(map(int, (version[1:] if version[0] == 'v' else version).split('.'))),
})