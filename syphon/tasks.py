import types


class MisconfigurationError(Exception):
    pass


def task(name, target, require=None):
    if target is None:
        raise MisconfigurationError('You must specify a target')
    if require is None:
        require = []

    def wrapper(callable):
        context = {
            'settings': {},
            'target': target,
            'require': require,
        }
        if isinstance(callable, types.FunctionType):
            def wrapped(*args, **kwargs):
                args = args + (context, )
                callable(*args, **kwargs)
            return wrapped
        else:
            return callable(context)
    return wrapper
