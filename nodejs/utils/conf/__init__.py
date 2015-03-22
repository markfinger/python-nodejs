try:
    import django
    DJANGO_INSTALLED = True
except ImportError:
    DJANGO_INSTALLED = False


class ConfigurationError(Exception):
    pass


class Conf(object):
    _namespace = None
    _settings = None
    _has_been_configured = False
    _configured_from_django = False

    def __init__(self, namespace, defaults):
        self._namespace = namespace
        self._settings = defaults
        if DJANGO_INSTALLED:
            from django.conf import settings
            overrides = settings.get(namespace, None)
            if overrides:
                self._has_been_configured = True
                self._configured_from_django = True
                self._settings.update(overrides)

    def configure(self, overrides):
        if self._has_been_configured:
            raise ConfigurationError('{namespace} already configured'.format(namespace=self._namespace))
        self._has_been_configured = True
        self._settings.update(overrides)

    def get(self, name, default=None):
        if name in self._settings:
            return getattr(self, name)
        return default

    def __getattr__(self, name):
        if name in self._settings:
            return self._settings[name]
        raise ConfigurationError('setting "{name}" has not been defined'.format(name=name))
