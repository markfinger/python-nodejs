from .conf import settings
from .interrogate import (
    node_installed, node_version, node_version_raw, raise_if_node_missing, raise_if_node_version_less_than, run_command
)


def ensure_node_installed():
    raise_if_node_missing()


def ensure_node_version_gte(required_version):
    ensure_node_installed()
    raise_if_node_version_less_than(required_version)


def node_run(*args):
    ensure_node_installed()
    return run_command((settings.PATH,) + tuple(args))