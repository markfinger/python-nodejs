from optional_django.conf import Conf

settings = Conf('NODEJS', {
    'PATH': 'node',
    'VERSION_COMMAND': '--version',
    'VERSION_FILTER': lambda version: tuple(map(int, (version[1:] if version[0] == 'v' else version).split('.'))),
})