"""Utilities and helper functions."""


def load_class(class_path):
    try:
        module_name, class_name = class_path.rsplit('.', 1)
    except ValueError:
        raise ImportError('Invalid class path %(class_path)r' %
                          {"class_path": class_path})
    module = __import__(module_name, fromlist=class_name)
    return getattr(module, class_name)
