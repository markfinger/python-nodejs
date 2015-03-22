class ErrorInterrogatingEnvironment(Exception):
    pass


class MissingDependency(Exception):
    pass


class OutdatedDependency(Exception):
    pass


class MalformedVersionInput(Exception):
    pass