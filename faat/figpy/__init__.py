"""This module provides a simple way to load configuration files.

Configuration files are defined in python syntax. All symbols defined
in UPPER_CASE are loaded from the configuration file. This way, your
configuration can calculate values dynamically, if you so desire.
"""

__version__ = '1.0.2'

import types
import importlib
import os
import argparse


def config_arg(path):
    try:
        result = load(path)
    except ConfigurationError as e:
        raise argparse.ArgumentTypeError(e.message)

    return result


def load(path, defaults=None, requires=None):
    """Loads configuration file from file.

    Args:
      path (string): The path of the file to load.
      default (dictionary): A dictionary of default setting values in case
        they are not defined in the configuration file.
      requires (list): A list of setting names that should be in the file.
        If any are not defined, an ConfigurationError is raised.

    Returns:
      The parsed configuration as an instance of Config.
    """
    if defaults is None:
        defaults = {}

    if requires is None:
        requires = []

    if not os.path.isfile(path):
        msg = f'Configuration file does not exist: {path}'
        raise ConfigurationError(msg)

    settings = Settings()
    settings.update(defaults)
    settings.update(load_py(path))

    missing_requirements = [k for k in requires if k not in settings]
    if missing_requirements:
        raise ConfigurationError('Missing requirements: %s' %
                                 ','.join(missing_requirements))
    return settings


def load_py(filename):
    d = types.ModuleType('config')
    d.__file__ = filename
    try:
        with open(filename, encoding="utf-8") as f:
            code = compile(f.read(), filename, 'exec')
        exec(code, d.__dict__)
    except Exception as e:
        msg = 'Invalid configuration file content: %s' % e
        raise ConfigurationError(msg)

    return {key: getattr(d, key) for key in dir(d) if key.isupper()}


class Settings(dict):
    def __getattr__(self, key):
        return self[key]

    def __setattr__(self, key, value):
        self[key] = value


class ConfigurationError(Exception):
    """Error raised when there's a problem with a configuration file."""
    def __init__(self, message):
        self.message = message
