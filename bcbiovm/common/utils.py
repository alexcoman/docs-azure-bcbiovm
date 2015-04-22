"""Utilities and helper functions."""

import logging
import sys
import types

import six

from bcbiovm.common import constant


def expose(function=None, alias=None):
    """
    Expose the function, optionally providing an alias or set of aliases.

    This decorator will be use to expose to the API the custom methods.
    Examples:
    ::
        @expose
        def compute_something(self):
            # ...
            pass

        @expose(alias="something")
        def compute_something(self):
            # ...
            pass

        @expose(alias=["something", "do_something"])
        def compute_something(self):
            # ...
            pass

        @expose(["something", "do_something"]):
        def compute_something(self):
            # ...
            pass
    """

    def get_alias():
        if alias is None:
            return ()
        elif isinstance(alias, six.string_types):
            return (alias)
        else:
            return tuple(alias)

    def wrapper(func):
        func.exposed = True
        func.alias = get_alias()
        return func

    if isinstance(function, (types.FunctionType, types.MethodType)):
        function.exposed = True
        function.alias = get_alias()
        return function

    elif function is None:
        return wrapper

    else:
        alias = function
        return wrapper


def load_class(class_path):
    try:
        module_name, class_name = class_path.rsplit('.', 1)
    except ValueError:
        raise ImportError('Invalid class path %(class_path)r' %
                          {"class_path": class_path})
    module = __import__(module_name, fromlist=class_name)
    return getattr(module, class_name)


def get_logger(name=constant.LOG.NAME, format_string=None):
    """Obtain a new logger object.

    :param name:          the name of the logger
    :param format_string: the format it will use for logging.

    If it is not given, the the one given at command
    line will be used, otherwise the default format.
    """
    logger = logging.getLogger(name)
    formatter = logging.Formatter(
        format_string or constant.LOG.FORMAT)

    if not logger.handlers:
        # If the logger wasn't obtained another time,
        # then it shouldn't have any loggers

        if constant.LOG.FILE:
            file_handler = logging.FileHandler(constant.LOG.FILE)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        stdout_handler = logging.StreamHandler(sys.stdout)
        stdout_handler.setFormatter(formatter)
        logger.addHandler(stdout_handler)

    logger.setLevel(constant.LOG.LEVEL)
    return logger
