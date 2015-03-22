import subprocess
import tempfile
from optional_django import six
from .exceptions import ErrorInterrogatingEnvironment, MalformedVersionInput, MissingDependency, OutdatedDependency
from .conf import settings


def run_command(cmd_to_run):
    """
    Wrapper around subprocess that pipes the stderr and stdout from `cmd_to_run`
    to temporary files. Using the temporary files gets around subprocess.PIPE's
    issues with handling large buffers.

    Note: this command will block the python process until `cmd_to_run` has completed.

    Returns a tuple, containing the stderr and stdout as strings.
    """
    with tempfile.TemporaryFile() as stdout_file, tempfile.TemporaryFile() as stderr_file:

        # Run the command
        popen = subprocess.Popen(cmd_to_run, stdout=stdout_file, stderr=stderr_file)
        popen.wait()

        stderr_file.seek(0)
        stdout_file.seek(0)

        stderr = stderr_file.read()
        stdout = stdout_file.read()

        if six.PY3:
            stderr = stderr.decode()
            stdout = stdout.decode()

        return stderr, stdout


try:
    _stderr, _stdout = run_command((settings.PATH, settings.VERSION_COMMAND,))
    if _stderr:
        raise ErrorInterrogatingEnvironment(_stderr)
    node_installed = True
    node_version_raw = _stdout.strip()
except OSError:
    node_installed = False
    node_version_raw = None
node_version = None
if node_version_raw:
    node_version = settings.VERSION_FILTER(node_version_raw)


def _check_if_version_is_outdated(current_version, required_version):
    if not isinstance(required_version, tuple):
        raise MalformedVersionInput(
            'Versions must be tuples. Received {0}'.format(required_version)
        )
    if len(required_version) < 3:
        raise MalformedVersionInput(
            'Versions must have three numbers defined. Received {0}'.format(required_version)
        )
    for number in required_version:
        if not isinstance(number, six.integer_types):
            raise MalformedVersionInput(
                'Versions can only contain number. Received {0}'.format(required_version)
            )
    for i, number_required in enumerate(required_version):
        if number_required > current_version[i]:
            return True
        elif number_required < current_version[i]:
            return False
    return current_version != required_version


def _format_version(version):
    return '.'.join(map(six.text_type, version))


def raise_if_node_missing(required_version=None):
    if not node_installed:
        error = 'node is not installed or cannot be found at path "{path}"'.format(path=settings.PATH)
        if required_version:
            error += '. Version {required_version} or greater is required.'.format(
                required_version=_format_version(required_version)
            )
        raise MissingDependency(error)


def raise_if_node_version_less_than(required_version):
    if _check_if_version_is_outdated(node_version, required_version):
        raise OutdatedDependency(
            (
                'The installed node version is outdated. Version {current_version} is installed, but version '
                '{required_version} is required. Please update node.'
            ).format(
                current_version=_format_version(node_version),
                required_version=_format_version(required_version),
            )
        )