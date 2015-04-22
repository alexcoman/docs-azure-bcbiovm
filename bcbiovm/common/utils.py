"""Utilities and helper functions."""

import types

import six


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
